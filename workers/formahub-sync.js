/* ============================================================
   Formahub — Worker « formahub-sync » : voix Microsoft Azure Speech
   ------------------------------------------------------------
   La clé Azure vit UNIQUEMENT ici, en Secret Cloudflare. Elle n'est
   ni dans le dépôt GitHub (public), ni dans le navigateur : l'appli
   appelle ce Worker, qui ajoute la clé et relaie vers Azure.

   ── INSTALLATION ─────────────────────────────────────────────
   1. dash.cloudflare.com → Workers & Pages → Create → Worker
        Nom : formahub-sync   (exactement ce nom : l'appli le déduit)
        puis Deploy
   2. Edit code → colle ce fichier en entier → Deploy
   3. Settings → Variables and Secrets → Add
        AZURE_KEY     = ta clé Azure Speech        ← type « Secret »
      Facultatif :
        AZURE_REGION  = francecentral (déjà la valeur par défaut)
        ALLOWED_ORIGINS = https://mon-domaine.fr   (si le site passe
                          un jour sur un domaine perso ; plusieurs
                          adresses séparées par des virgules)

   ── API ──────────────────────────────────────────────────────
   GET  /tts  → { enabled, voices: [...] }  voix utilisables en français
   POST /tts  → audio/mpeg
        corps JSON : { text, voice, style?, degree?, pitch?, rate? }

   Seules les pages Formahub peuvent l'appeler (contrôle d'origine) :
   les adresses *.workers.dev du même compte, localhost, et
   ALLOWED_ORIGINS. La vitesse (jusqu'à 2×) est appliquée par le
   lecteur du navigateur : elle ne coûte aucun caractère Azure.
   ============================================================ */

const DEFAULT_REGION = 'francecentral';
const MAX_CHARS = 2500;
const OUTPUT_FORMAT = 'audio-24khz-48kbitrate-mono-mp3';
const VOICES_TTL = 24 * 3600;
const AUDIO_TTL = 30 * 24 * 3600;

const VOICE_RE = /^[a-z]{2,3}-[A-Z]{2}-[A-Za-z0-9]+(?::[A-Za-z0-9]+)?$/;
const STYLE_RE = /^[a-z][a-z-]{1,39}$/i;
const PERCENT_RE = /^[+-]?\d{1,2}%$/;

function configured(env) {
  return !!env.AZURE_KEY;
}

function region(env) {
  return String(env.AZURE_REGION || DEFAULT_REGION).trim().toLowerCase().replace(/[^a-z0-9]/g, '');
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
function buildSsml({ text, voice, style, degree, pitch, rate }) {
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

function validate(body) {
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


/* ---------- CORS : qui a le droit d'appeler ce Worker ---------- */

function allowedOrigin(request, env) {
  const origin = request.headers.get('Origin');
  if (!origin) return null;
  let o;
  try { o = new URL(origin); } catch (e) { return null; }

  const extra = String(env.ALLOWED_ORIGINS || '')
    .split(',').map(s => s.trim().replace(/\/+$/, '')).filter(Boolean);
  if (extra.includes(o.origin)) return o.origin;

  if (o.hostname === 'localhost' || o.hostname === '127.0.0.1') return o.origin;

  // Même compte Cloudflare : formahub-sync.<compte>.workers.dev
  // accepte formahubv2.<compte>.workers.dev (et tout Worker du compte)
  const self = new URL(request.url).hostname;
  const m = self.match(/^[^.]+\.([^.]+\.workers\.dev)$/);
  if (m && o.protocol === 'https:' && o.hostname.endsWith('.' + m[1])) return o.origin;

  // Déploiement Cloudflare Pages éventuel : formahub*.pages.dev
  if (o.protocol === 'https:' && /^([a-z0-9-]+\.)?formahub[a-z0-9-]*\.pages\.dev$/.test(o.hostname)) return o.origin;

  return null;
}

function corsHeaders(origin) {
  if (!origin) return {};
  return {
    'Access-Control-Allow-Origin': origin,
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Expose-Headers': 'Retry-After, X-Formahub-Cache',
    'Access-Control-Max-Age': '86400',
    'Vary': 'Origin'
  };
}

function json(body, status, cors, extra) {
  return new Response(JSON.stringify(body), {
    status: status || 200,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'no-store',
      'X-Content-Type-Options': 'nosniff',
      ...(cors || {}),
      ...(extra || {})
    }
  });
}

/* ---------- GET /tts : état + voix françaises ---------- */

async function listVoices(env, cors) {
  if (!configured(env)) return json({ enabled: false, error: 'Secret AZURE_KEY absent du Worker.' }, 200, cors);

  const cache = caches.default;
  const key = new Request(`https://formahub-tts.internal/voices/${region(env)}/v2`);
  const hit = await cache.match(key);
  if (hit) return json({ enabled: true, voices: await hit.json() }, 200, cors);

  let list;
  try {
    const res = await fetch(
      `https://${region(env)}.tts.speech.microsoft.com/cognitiveservices/voices/list`,
      { headers: { 'Ocp-Apim-Subscription-Key': env.AZURE_KEY } }
    );
    if (!res.ok) {
      return json({ enabled: false, error: `Azure a refusé la demande (${res.status}) — vérifiez la clé et la région.` }, 200, cors);
    }
    list = await res.json();
  } catch (e) {
    return json({ enabled: false, error: 'Azure injoignable' }, 200, cors);
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
    .sort((a, b) => rank(a) - rank(b) || a.label.localeCompare(b.label, 'fr'));

  await cache.put(key, new Response(JSON.stringify(voices), {
    headers: { 'Content-Type': 'application/json', 'Cache-Control': `public, max-age=${VOICES_TTL}` }
  }));
  return json({ enabled: true, voices }, 200, cors);
}

function rank(v) {
  if (v.locale === 'fr-FR') return v.multilingual ? 1 : 0;
  if (/^fr-/i.test(v.locale)) return 2;
  return 3;
}

/* ---------- POST /tts : synthèse d'un extrait ---------- */

async function synthesize(request, env, ctx, cors) {
  if (!configured(env)) return json({ error: 'Azure non configuré (secret AZURE_KEY absent)' }, 503, cors);

  let body;
  try {
    body = await request.json();
  } catch (e) {
    return json({ error: 'corps illisible' }, 400, cors);
  }
  const err = validate(body);
  if (err) return json({ error: err }, 400, cors);

  const ssml = buildSsml({
    text: body.text.trim(),
    voice: body.voice,
    style: body.style || '',
    degree: body.degree != null ? Number(body.degree).toFixed(2) : '',
    pitch: body.pitch || '',
    rate: body.rate || ''
  });

  // Cache Cloudflare (actif sur domaine perso ; sans effet sur *.workers.dev,
  // où le cache du navigateur « fhtts-v1 » prend le relais)
  const cache = caches.default;
  const key = new Request(`https://formahub-tts.internal/audio/${await sha256(ssml)}`);
  const hit = await cache.match(key);
  if (hit) {
    const r = new Response(hit.body, hit);
    for (const [k, v] of Object.entries(cors)) r.headers.set(k, v);
    r.headers.set('X-Formahub-Cache', 'HIT');
    return r;
  }

  let res;
  try {
    res = await fetch(`https://${region(env)}.tts.speech.microsoft.com/cognitiveservices/v1`, {
      method: 'POST',
      headers: {
        'Ocp-Apim-Subscription-Key': env.AZURE_KEY,
        'Content-Type': 'application/ssml+xml',
        'X-Microsoft-OutputFormat': OUTPUT_FORMAT,
        'User-Agent': 'formahub'
      },
      body: ssml
    });
  } catch (e) {
    return json({ error: 'Azure injoignable' }, 502, cors);
  }

  if (res.status === 429) {
    return json({ error: 'quota Azure momentanément atteint' }, 429, cors,
      { 'Retry-After': res.headers.get('Retry-After') || '5' });
  }
  if (!res.ok) return json({ error: `Azure a répondu ${res.status}` }, 502, cors);

  const audio = await res.arrayBuffer();
  const base = {
    'Content-Type': 'audio/mpeg',
    'Cache-Control': `public, max-age=${AUDIO_TTL}`,
    'X-Content-Type-Options': 'nosniff'
  };
  ctx.waitUntil(cache.put(key, new Response(audio.slice(0), { headers: base })));
  return new Response(audio, { headers: { ...base, ...cors, 'X-Formahub-Cache': 'MISS' } });
}

/* ---------- Routeur ---------- */

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname.replace(/\/+$/, '') || '/';
    const origin = allowedOrigin(request, env);
    const cors = corsHeaders(origin);

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: origin ? 204 : 403, headers: cors });
    }

    if (path === '/') {
      return json({ ok: true, service: 'formahub-sync', azure: configured(env), region: region(env), routes: ['/tts'] }, 200, cors);
    }

    if (path === '/tts') {
      if (!origin) return json({ error: 'origine refusée' }, 403);
      if (request.method === 'GET') return listVoices(env, cors);
      if (request.method === 'POST') return synthesize(request, env, ctx, cors);
      return json({ error: 'méthode non autorisée' }, 405, cors, { Allow: 'GET, POST, OPTIONS' });
    }

    return json({ error: 'route inconnue' }, 404, cors);
  }
};
