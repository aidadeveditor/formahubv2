/* Formahub — synthèse vocale Microsoft Azure Speech (Cloudflare Pages Function)
 *
 * La clé Azure ne quitte jamais le serveur : elle vit dans les secrets du
 * projet Cloudflare Pages, jamais dans le code ni dans le navigateur.
 *
 *   AZURE_SPEECH_KEY     clé de la ressource Speech (secret)
 *   AZURE_SPEECH_REGION  région de la ressource, ex. « francecentral » ou « westeurope »
 *
 * GET  /api/tts  → { enabled, voices: [...] }  (voix utilisables en français)
 * POST /api/tts  → audio/mpeg
 *      corps JSON : { text, voice, style?, degree?, pitch?, rate? }
 *
 * Chaque extrait déjà synthétisé est mis en cache côté Cloudflare (30 jours) :
 * réécouter un module ne reconsomme pas de caractères Azure.
 * La vitesse d'écoute (jusqu'à 2×) est appliquée par le lecteur du navigateur,
 * elle ne change donc pas le fichier et ne casse pas le cache.
 */

const MAX_CHARS = 2500;
const OUTPUT_FORMAT = 'audio-24khz-48kbitrate-mono-mp3';
const VOICES_TTL = 24 * 3600;
const AUDIO_TTL = 30 * 24 * 3600;

const VOICE_RE = /^[a-z]{2,3}-[A-Z]{2}-[A-Za-z0-9]+(?::[A-Za-z0-9]+)?$/;
const STYLE_RE = /^[a-z][a-z-]{1,39}$/i;
const PERCENT_RE = /^[+-]?\d{1,2}%$/;

function json(body, status = 200, extra = {}) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'no-store',
      'X-Content-Type-Options': 'nosniff',
      ...extra
    }
  });
}

function configured(env) {
  return !!(env.AZURE_SPEECH_KEY && env.AZURE_SPEECH_REGION);
}

function region(env) {
  return String(env.AZURE_SPEECH_REGION).trim().toLowerCase().replace(/[^a-z0-9]/g, '');
}

/* Seules les pages du site peuvent consommer le quota Azure. */
function sameOrigin(request) {
  const self = new URL(request.url);
  const origin = request.headers.get('Origin') || request.headers.get('Referer');
  if (!origin) return false;
  try {
    const o = new URL(origin);
    if (o.host === self.host) return true;
    return o.hostname === 'localhost' || o.hostname === '127.0.0.1';
  } catch (e) {
    return false;
  }
}

function escapeXml(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

/* Construit le SSML. Exporté pour les tests. */
export function buildSsml({ text, voice, style, degree, pitch, rate }) {
  let inner = escapeXml(text);

  const prosody = [];
  if (pitch && pitch !== '0%' && pitch !== '+0%') prosody.push(`pitch="${pitch}"`);
  if (rate && rate !== '0%' && rate !== '+0%') prosody.push(`rate="${rate}"`);
  if (prosody.length) inner = `<prosody ${prosody.join(' ')}>${inner}</prosody>`;

  // Voix multilingue d'une autre langue : on lui demande de parler français
  if (!/^fr-/i.test(voice)) inner = `<lang xml:lang="fr-FR">${inner}</lang>`;

  if (style) {
    const deg = degree ? ` styledegree="${degree}"` : '';
    inner = `<mstts:express-as style="${style}"${deg}>${inner}</mstts:express-as>`;
  }

  return '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" ' +
    'xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="fr-FR">' +
    `<voice name="${voice}">${inner}</voice></speak>`;
}

export function validate(body) {
  if (!body || typeof body !== 'object') return 'corps illisible';
  const text = typeof body.text === 'string' ? body.text.trim() : '';
  if (!text) return 'texte vide';
  if (text.length > MAX_CHARS) return 'texte trop long';
  if (typeof body.voice !== 'string' || !VOICE_RE.test(body.voice)) return 'voix invalide';
  if (body.style && !STYLE_RE.test(body.style)) return 'style invalide';
  if (body.pitch && !PERCENT_RE.test(body.pitch)) return 'hauteur invalide';
  if (body.rate && !PERCENT_RE.test(body.rate)) return 'débit invalide';
  if (body.degree != null) {
    const d = Number(body.degree);
    if (!(d >= 0.01 && d <= 2)) return 'intensité invalide';
  }
  return null;
}

async function sha256(s) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s));
  return [...new Uint8Array(buf)].map(b => b.toString(16).padStart(2, '0')).join('');
}

/* ---------- GET : état + voix françaises disponibles ---------- */

export async function onRequestGet(context) {
  const { env, request } = context;
  if (!configured(env)) return json({ enabled: false });

  const cache = caches.default;
  const key = new Request(`https://formahub-tts.internal/voices/${region(env)}/v2`);
  const hit = await cache.match(key);
  if (hit) return json({ enabled: true, voices: await hit.json() });

  let list;
  try {
    const res = await fetch(
      `https://${region(env)}.tts.speech.microsoft.com/cognitiveservices/voices/list`,
      { headers: { 'Ocp-Apim-Subscription-Key': env.AZURE_SPEECH_KEY } }
    );
    if (!res.ok) {
      return json({ enabled: false, error: `Azure a refusé la demande (${res.status}) — vérifiez la clé et la région.` });
    }
    list = await res.json();
  } catch (e) {
    return json({ enabled: false, error: 'Azure injoignable' });
  }

  const voices = list
    .filter(v => {
      const secondary = v.SecondaryLocaleList || [];
      return /^fr-/i.test(v.Locale) || secondary.some(l => /^fr-/i.test(l));
    })
    .map(v => ({
      name: v.ShortName,
      label: v.LocalName || v.DisplayName || v.ShortName,
      locale: v.Locale,
      gender: v.Gender,
      styles: v.StyleList || [],
      multilingual: !/^fr-/i.test(v.Locale) || /Multilingual/i.test(v.ShortName),
      hd: /DragonHD|:.*HD/i.test(v.ShortName)
    }))
    // Français de France d'abord, puis autres francophonies, puis multilingues
    .sort((a, b) => rank(a) - rank(b) || a.label.localeCompare(b.label, 'fr'));

  await cache.put(key, new Response(JSON.stringify(voices), {
    headers: { 'Content-Type': 'application/json', 'Cache-Control': `public, max-age=${VOICES_TTL}` }
  }));
  return json({ enabled: true, voices });
}

function rank(v) {
  if (v.locale === 'fr-FR') return v.multilingual ? 1 : 0;
  if (/^fr-/i.test(v.locale)) return 2;
  return 3;
}

/* ---------- POST : synthèse d'un extrait ---------- */

export async function onRequestPost(context) {
  const { env, request } = context;
  if (!configured(env)) return json({ error: 'Azure non configuré' }, 503);
  if (!sameOrigin(request)) return json({ error: 'origine refusée' }, 403);

  let body;
  try {
    body = await request.json();
  } catch (e) {
    return json({ error: 'corps illisible' }, 400);
  }
  const err = validate(body);
  if (err) return json({ error: err }, 400);

  const ssml = buildSsml({
    text: body.text.trim(),
    voice: body.voice,
    style: body.style || '',
    degree: body.degree != null ? Number(body.degree).toFixed(2) : '',
    pitch: body.pitch || '',
    rate: body.rate || ''
  });

  const cache = caches.default;
  const key = new Request(`https://formahub-tts.internal/audio/${await sha256(ssml)}`);
  const hit = await cache.match(key);
  if (hit) {
    const r = new Response(hit.body, hit);
    r.headers.set('X-Formahub-Cache', 'HIT');
    return r;
  }

  let res;
  try {
    res = await fetch(`https://${region(env)}.tts.speech.microsoft.com/cognitiveservices/v1`, {
      method: 'POST',
      headers: {
        'Ocp-Apim-Subscription-Key': env.AZURE_SPEECH_KEY,
        'Content-Type': 'application/ssml+xml',
        'X-Microsoft-OutputFormat': OUTPUT_FORMAT,
        'User-Agent': 'formahub'
      },
      body: ssml
    });
  } catch (e) {
    return json({ error: 'Azure injoignable' }, 502);
  }

  if (res.status === 429) {
    return json({ error: 'quota Azure momentanément atteint' }, 429,
      { 'Retry-After': res.headers.get('Retry-After') || '5' });
  }
  if (!res.ok) {
    return json({ error: `Azure a répondu ${res.status}` }, 502);
  }

  const audio = await res.arrayBuffer();
  const out = new Response(audio, {
    headers: {
      'Content-Type': 'audio/mpeg',
      'Cache-Control': `public, max-age=${AUDIO_TTL}`,
      'X-Content-Type-Options': 'nosniff'
    }
  });
  context.waitUntil(cache.put(key, out.clone()));
  out.headers.set('X-Formahub-Cache', 'MISS');
  return out;
}
