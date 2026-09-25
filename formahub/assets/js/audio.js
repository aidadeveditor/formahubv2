/* ============================================================
   Formahub — écoute audio des modules et podcasts (V8)

   Deux moteurs de voix, choisis dans la liste « Voix » :
     • Azure Speech (voix neuronales Microsoft) — passe par le
       Worker Cloudflare « formahub-sync », la clé reste côté serveur
       (jamais dans ce fichier, jamais dans le dépôt) ;
     • la synthèse vocale du navigateur (Web Speech API), en secours
       hors ligne ou si Azure n'est pas configuré.

   Réglages : voix, ton (tons prédéfinis + styles propres à la voix
   Azure choisie), vitesse de 0,75× à 2×.

   Deux lecteurs partagent le même moteur :
     • « Écouter le module »  — lit le cours section par section ;
     • « Podcast du module »  — joue le dialogue de podcast.json.
   Un seul parle à la fois.
   ============================================================ */

(function () {
  'use strict';

  var SUPPORTED = typeof window !== 'undefined' &&
    'speechSynthesis' in window && 'SpeechSynthesisUtterance' in window;

  var POS_KEY = 'formahub-audio-pos';
  var PREF_KEY = 'formahub-audio-prefs';

  var SELF = document.currentScript;
  var ROOT = (function () {
    if (SELF && SELF.src) return SELF.src.replace(/assets\/js\/audio\.js.*$/, '');
    return new URL('.', location.href).toString();
  })();

  /* Adresse du relais Azure (Worker « formahub-sync »).
     Laisser vide tant que le site est sur *.workers.dev : l'adresse est
     déduite toute seule (formahubv2.<compte>.workers.dev →
     formahub-sync.<compte>.workers.dev). À renseigner seulement si le site
     passe un jour sur un domaine perso, ex. 'https://formahub-sync.xxx.workers.dev'.
     Ce n'est pas un secret : la clé Azure, elle, reste dans le Worker. */
  var TTS_WORKER = '';

  var TTS_URL = (function () {
    if (TTS_WORKER) return TTS_WORKER.replace(/\/+$/, '') + '/tts';
    var m = location.hostname.match(/^[^.]+\.([^.]+\.workers\.dev)$/);
    if (m) return 'https://formahub-sync.' + m[1] + '/tts';
    return ROOT + 'api/tts';     // localhost / Pages : fonction locale functions/api/tts.js
  })();

  var RATES = [0.75, 0.9, 1, 1.1, 1.25, 1.5, 1.75, 2];

  var TONE_PRESETS = [
    { id: 'neutre', label: 'Neutre', pitch: 0, rate: 0 },
    { id: 'pose', label: 'Posé', pitch: -3, rate: -6 },
    { id: 'chaleureux', label: 'Chaleureux', pitch: 3, rate: -2 },
    { id: 'dynamique', label: 'Dynamique', pitch: 5, rate: 8 },
    { id: 'grave', label: 'Plus grave', pitch: -8, rate: 0 },
    { id: 'aigu', label: 'Plus aigu', pitch: 8, rate: 0 }
  ];

  var STYLE_LABELS = {
    cheerful: 'Enjoué', sad: 'Triste', calm: 'Calme', gentle: 'Doux',
    friendly: 'Amical', excited: 'Enthousiaste', serious: 'Sérieux',
    hopeful: 'Optimiste', empathetic: 'Empathique', whispering: 'Chuchoté',
    newscast: 'Journal télévisé', 'newscast-casual': 'Journal détendu',
    'newscast-formal': 'Journal formel', 'narration-professional': 'Narration pro',
    'narration-relaxed': 'Narration détendue', 'documentary-narration': 'Documentaire',
    'customerservice': 'Service client', assistant: 'Assistant', chat: 'Conversation',
    affectionate: 'Affectueux', lyrical: 'Lyrique', shy: 'Timide',
    embarrassed: 'Gêné', fearful: 'Inquiet', terrified: 'Effrayé',
    angry: 'Fâché', unfriendly: 'Froid', disgruntled: 'Mécontent',
    depressed: 'Abattu', envious: 'Envieux', shouting: 'Crié',
    'advertisement-upbeat': 'Publicité', 'sports-commentary': 'Commentaire sportif',
    'sports-commentary-excited': 'Commentaire sportif enthousiaste', poetry: 'Poésie',
    story: 'Conte', 'live-commercial': 'Direct commercial'
  };

  /* ---------- Stockage tolérant ---------- */

  function readStore(key, fallback) {
    try {
      var raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : fallback;
    } catch (e) { return fallback; }
  }

  function writeStore(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); } catch (e) { /* ignore */ }
  }

  var prefs = readStore(PREF_KEY, {}) || {};

  function savePrefs() {
    writeStore(PREF_KEY, prefs);
    // La page Paramètres recalcule les audios à télécharger pour ces voix
    try { window.dispatchEvent(new CustomEvent('formahub-audio-prefs')); } catch (e) { /* ignore */ }
    // La sauvegarde par code secret, si elle est active, reprend la main
    if (typeof window.formahubQueueBackup === 'function') window.formahubQueueBackup();
  }

  function clamp(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }

  function rateLabel(r) { return String(r).replace('.', ',') + '×'; }

  function nearestRate(r) {
    r = parseFloat(r) || 1;
    var best = 1;
    RATES.forEach(function (x) { if (Math.abs(x - r) < Math.abs(best - r)) best = x; });
    return best;
  }

  /* ============================================================
     1. Azure Speech — état, voix, cache local des extraits
     ============================================================ */

  /* enabled : le relais répond. cachedOnly : hors ligne, mais la liste
     des voix est connue (mémorisée) — les extraits téléchargés restent
     alors jouables avec la voix Azure choisie. */
  var Azure = { enabled: false, cachedOnly: false, voices: [], error: null };
  var VOICES_KEY = 'formahub-azure-voices';

  function azureUsable() { return Azure.enabled || Azure.cachedOnly; }

  function azureInit() {
    if (location.protocol === 'file:') return Promise.resolve(Azure);
    var ctrl = ('AbortController' in window) ? new AbortController() : null;
    var timer = setTimeout(function () { if (ctrl) ctrl.abort(); }, 5000);
    return fetch(TTS_URL, { cache: 'no-store', signal: ctrl ? ctrl.signal : undefined })
      .then(function (r) { return r.ok ? r.json() : { enabled: false }; })
      .then(function (d) {
        Azure.enabled = !!(d && d.enabled && d.voices && d.voices.length);
        Azure.voices = (d && d.voices) || [];
        Azure.error = (d && d.error) || null;
        if (Azure.error && window.console) console.warn('[Formahub audio] Azure :', Azure.error);
        if (Azure.enabled) writeStore(VOICES_KEY, Azure.voices);
        return Azure;
      })
      .catch(function () { return Azure; })
      .then(function (a) {
        if (!Azure.enabled) {
          var known = readStore(VOICES_KEY, null);
          if (known && known.length) {
            Azure.voices = known;
            Azure.cachedOnly = true;
          }
        }
        return a;
      })
      .then(function (a) { clearTimeout(timer); return a; });
  }

  function azureVoice(name) {
    for (var i = 0; i < Azure.voices.length; i++) {
      if (Azure.voices[i].name === name) return Azure.voices[i];
    }
    return null;
  }

  function defaultAzureVoice(gender) {
    var fr = Azure.voices.filter(function (v) { return v.locale === 'fr-FR' && !v.multilingual; });
    var pool = fr.length ? fr : Azure.voices;
    var preferred = gender === 'Male' ? 'fr-FR-HenriNeural' : 'fr-FR-DeniseNeural';
    if (azureVoice(preferred)) return preferred;
    var g = pool.filter(function (v) { return !gender || v.gender === gender; });
    return (g[0] || pool[0] || {}).name || null;
  }

  /* Cache local : chaque extrait déjà écouté reste dans le navigateur,
     il se réécoute sans réseau ni caractère Azure consommé. */
  var TTS_CACHE = 'fhtts-v1';          // nom hors du préfixe « formahub- » purgé par sw.js
  var TTS_DL_CACHE = 'fhtts-dl-v1';    // audios téléchargés depuis Paramètres : jamais purgés
  var TTS_CACHE_MAX = 500;
  var putsSincePrune = 0;

  function hashString(str) {
    // cyrb53 — condensé rapide, suffisant pour une clé de cache
    var h1 = 0xdeadbeef, h2 = 0x41c6ce57;
    for (var i = 0, ch; i < str.length; i++) {
      ch = str.charCodeAt(i);
      h1 = Math.imul(h1 ^ ch, 2654435761);
      h2 = Math.imul(h2 ^ ch, 1597334677);
    }
    h1 = Math.imul(h1 ^ (h1 >>> 16), 2246822507) ^ Math.imul(h2 ^ (h2 >>> 13), 3266489909);
    h2 = Math.imul(h2 ^ (h2 >>> 16), 2246822507) ^ Math.imul(h1 ^ (h1 >>> 13), 3266489909);
    return (h2 >>> 0).toString(16) + (h1 >>> 0).toString(16);
  }

  function cacheGet(key) {
    if (!('caches' in window)) return Promise.resolve(null);
    return caches.open(TTS_DL_CACHE)
      .then(function (c) { return c.match(key); })
      .then(function (r) {
        return r || caches.open(TTS_CACHE).then(function (c) { return c.match(key); });
      })
      .then(function (r) { return r ? r.blob() : null; })
      .catch(function () { return null; });
  }

  function dlHas(key) {
    if (!('caches' in window)) return Promise.resolve(false);
    return caches.open(TTS_DL_CACHE)
      .then(function (c) { return c.match(key); })
      .then(function (r) { return !!r; })
      .catch(function () { return false; });
  }

  function dlPut(key, blob) {
    return caches.open(TTS_DL_CACHE).then(function (c) {
      return c.put(key, new Response(blob, { headers: { 'Content-Type': 'audio/mpeg' } }));
    });
  }

  function cachePut(key, blob) {
    if (!('caches' in window)) return;
    caches.open(TTS_CACHE).then(function (c) {
      return c.put(key, new Response(blob, { headers: { 'Content-Type': 'audio/mpeg' } })).then(function () {
        putsSincePrune += 1;
        if (putsSincePrune < 40) return;
        putsSincePrune = 0;
        return c.keys().then(function (keys) {
          var extra = keys.length - TTS_CACHE_MAX;
          for (var i = 0; i < extra; i++) c.delete(keys[i]);
        });
      });
    }).catch(function () { /* stockage plein ou indisponible : on s'en passe */ });
  }

  function wait(ms) { return new Promise(function (res) { setTimeout(res, ms); }); }

  function fmtPct(n) {
    n = Math.round(n || 0);
    if (!n) return '';
    return (n > 0 ? '+' : '') + n + '%';
  }

  function azureBody(item) {
    var body = { text: item.text, voice: item.azVoice };
    if (item.style) body.style = item.style;
    if (fmtPct(item.pitchPct)) body.pitch = fmtPct(item.pitchPct);
    if (fmtPct(item.ratePct)) body.rate = fmtPct(item.ratePct);
    return body;
  }

  function clipKey(item) {
    return ROOT + '__tts-cache/' + hashString(JSON.stringify(azureBody(item)));
  }

  /* keep = true : téléchargement pour l'écoute hors ligne (cache non purgé) */
  function fetchClip(item, attempt, keep) {
    attempt = attempt || 0;
    var payload = JSON.stringify(azureBody(item));
    var key = clipKey(item);
    return cacheGet(key).then(function (blob) {
      if (blob) {
        if (keep) return dlPut(key, blob).then(function () { return blob; });
        return blob;
      }
      return fetch(TTS_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: payload
      }).then(function (r) {
        if (r.status === 429 && attempt < 4) {
          var after = parseInt(r.headers.get('Retry-After'), 10);
          return wait((after > 0 ? after : 2 * (attempt + 1)) * 1000)
            .then(function () { return fetchClip(item, attempt + 1, keep); });
        }
        if (!r.ok) {
          return r.json().catch(function () { return {}; }).then(function (d) {
            throw new Error(d.error || ('erreur ' + r.status));
          });
        }
        return r.blob().then(function (b) {
          if (keep) return dlPut(key, b).then(function () { return b; });
          cachePut(key, b);
          return b;
        });
      });
    });
  }

  /* ============================================================
     2. Le moteur de parole (Azure ou navigateur, extrait par extrait)
     ============================================================ */

  var Engine = {
    voices: [],
    queue: [],          // items : voir makeItem()
    index: 0,
    playing: false,
    paused: false,
    current: null,
    onProgress: null,   // (meta, indexDansLaQueue, total) -> void
    onDone: null,
    onError: null,      // (message, index) -> void
    watchdog: null,
    keepAlive: null
  };

  var AZ = { audio: null, gen: 0, clips: {}, urls: [], loaded: -1 };

  function loadVoices() {
    var list = [];
    try { list = window.speechSynthesis.getVoices() || []; } catch (e) { list = []; }
    Engine.voices = list;
    return list;
  }

  function whenVoicesReady(cb) {
    if (!SUPPORTED) { cb([]); return; }
    var list = loadVoices();
    if (list.length) { cb(list); return; }
    var done = false;
    function fire() {
      if (done) return;
      done = true;
      cb(loadVoices());
    }
    try { window.speechSynthesis.addEventListener('voiceschanged', fire, { once: true }); }
    catch (e) { window.speechSynthesis.onvoiceschanged = fire; }
    // Certains navigateurs ne déclenchent jamais l'événement : on n'attend pas indéfiniment
    setTimeout(fire, 1600);
  }

  function frenchVoices() {
    var fr = Engine.voices.filter(function (v) {
      return /^fr(-|_|$)/i.test(v.lang || '');
    });
    // Voix locales d'abord : ce sont les seules à fonctionner hors ligne
    fr.sort(function (a, b) {
      if (!!a.localService === !!b.localService) return (a.name || '').localeCompare(b.name || '');
      return a.localService ? -1 : 1;
    });
    return fr.length ? fr : Engine.voices.slice();
  }

  function voiceByName(name) {
    if (!name) return null;
    for (var i = 0; i < Engine.voices.length; i++) {
      if (Engine.voices[i].name === name) return Engine.voices[i];
    }
    return null;
  }

  function webAvailable() { return SUPPORTED && Engine.voices.length > 0; }
  function anyVoice() { return azureUsable() || webAvailable(); }

  /* Clés de voix : « az:<ShortName> » ou « web:<nom système> » */
  function isAzureKey(k) { return typeof k === 'string' && k.indexOf('az:') === 0; }
  function keyName(k) { return String(k || '').replace(/^(az|web):/, ''); }

  function validVoiceKey(k) {
    if (!k) return false;
    if (isAzureKey(k)) return azureUsable() && !!azureVoice(keyName(k));
    return webAvailable() && !!voiceByName(keyName(k));
  }

  function defaultVoiceKey(gender) {
    if (azureUsable()) {
      var n = defaultAzureVoice(gender);
      if (n) return 'az:' + n;
    }
    var fr = frenchVoices();
    return fr.length ? 'web:' + fr[0].name : null;
  }

  function webFallbackKey() {
    var fr = frenchVoices();
    return (SUPPORTED && fr.length) ? 'web:' + fr[0].name : null;
  }

  /* Ton : « p:<preset> » (tous moteurs) ou « s:<style Azure> » */
  function resolveTone(toneKey, voiceKey) {
    toneKey = toneKey || 'p:neutre';
    if (toneKey.indexOf('s:') === 0) {
      var style = toneKey.slice(2);
      var v = isAzureKey(voiceKey) ? azureVoice(keyName(voiceKey)) : null;
      if (v && (v.styles || []).indexOf(style) !== -1) return { style: style, pitch: 0, rate: 0 };
      return { style: '', pitch: 0, rate: 0 };
    }
    var id = toneKey.slice(2);
    for (var i = 0; i < TONE_PRESETS.length; i++) {
      if (TONE_PRESETS[i].id === id) {
        return { style: '', pitch: TONE_PRESETS[i].pitch, rate: TONE_PRESETS[i].rate };
      }
    }
    return { style: '', pitch: 0, rate: 0 };
  }

  function makeItem(text, voiceKey, toneKey, rate, meta, extraPitch) {
    var t = resolveTone(toneKey, voiceKey);
    var item = { text: text, rate: rate || 1, meta: meta, voiceKey: voiceKey };
    if (isAzureKey(voiceKey)) {
      item.engine = 'azure';
      item.azVoice = keyName(voiceKey);
      item.style = t.style;
      item.pitchPct = t.pitch;
      item.ratePct = t.rate;
    } else {
      item.engine = 'web';
      item.voice = voiceByName(keyName(voiceKey));
      item.pitch = clamp((extraPitch || 1) * (1 + t.pitch / 50), 0.3, 1.8);
      item.toneRate = 1 + t.rate / 100;
    }
    return item;
  }

  /* Découpe un texte en fragments courts.
     Web Speech : Chrome interrompt une énonciation qui dépasse ~15 s,
     on reste donc sous ~210 caractères. Azure accepte bien plus long. */
  function chunkText(text, limit) {
    var max = limit || 210;
    var clean = String(text || '').replace(/\s+/g, ' ').trim();
    if (!clean) return [];
    var sentences = clean.match(/[^.!?…:;]+[.!?…:;]*\s*/g) || [clean];
    var out = [];
    var buf = '';

    sentences.forEach(function (s) {
      var piece = s.trim();
      if (!piece) return;
      // Une phrase seule trop longue est coupée sur les virgules
      if (piece.length > max) {
        if (buf) { out.push(buf); buf = ''; }
        var parts = piece.split(/,\s*/);
        var sub = '';
        parts.forEach(function (p, i) {
          var withComma = p + (i < parts.length - 1 ? ',' : '');
          if ((sub + ' ' + withComma).trim().length > max) {
            if (sub) out.push(sub.trim());
            sub = withComma;
          } else {
            sub = (sub + ' ' + withComma).trim();
          }
        });
        if (sub) out.push(sub.trim());
        return;
      }
      if ((buf + ' ' + piece).trim().length > max) {
        out.push(buf.trim());
        buf = piece;
      } else {
        buf = (buf + ' ' + piece).trim();
      }
    });
    if (buf) out.push(buf.trim());
    return out;
  }

  /* Prononciation : quelques normalisations qui évitent les lectures absurdes */
  function speakable(text) {
    return String(text || '')
      .replace(/\u00a0/g, ' ')
      .replace(/([0-9])\s*%/g, '$1 pour cent')
      .replace(/([0-9])\s*€/g, '$1 euros')
      .replace(/\bK€/g, 'kilo-euros')
      .replace(/\bN°/gi, 'numéro ')
      .replace(/\b1er\b/g, 'premier')
      .replace(/\b(\d+)e\b/g, '$1ème')
      .replace(/\bSERP\b/g, 'sèrpe')
      .replace(/\bCTR\b/g, 'C.T.R.')
      .replace(/\bROI\b/g, 'R.O.I.')
      .replace(/\bKPI\b/g, 'K.P.I.')
      .replace(/\bURL\b/g, 'U.R.L.')
      .replace(/\bSEO\b/g, 'S.E.O.')
      .replace(/\bSEA\b/g, 'S.E.A.')
      .replace(/\bCRM\b/g, 'C.R.M.')
      .replace(/\bRSE\b/g, 'R.S.E.')
      .replace(/\bIA\b/g, 'I.A.')
      .replace(/\s+/g, ' ')
      .trim();
  }

  function clearTimers() {
    if (Engine.watchdog) { clearTimeout(Engine.watchdog); Engine.watchdog = null; }
    if (Engine.keepAlive) { clearInterval(Engine.keepAlive); Engine.keepAlive = null; }
  }

  /* ---------- Élément <audio> partagé pour Azure ---------- */

  function azAudio() {
    if (!AZ.audio) {
      var a = new Audio();
      a.preload = 'auto';
      // La vitesse ne doit pas transformer la voix en voix de dessin animé
      a.preservesPitch = true;
      a.mozPreservesPitch = true;
      a.webkitPreservesPitch = true;
      AZ.audio = a;
    }
    return AZ.audio;
  }

  /* iOS n'autorise un <audio> qu'une fois « débloqué » par un geste :
     on joue un silence dans le clic de l'utilisatrice. */
  var SILENCE = (function () {
    var n = 800, bytes = new Uint8Array(44 + n);
    var dv = new DataView(bytes.buffer);
    function s(o, str) { for (var i = 0; i < str.length; i++) bytes[o + i] = str.charCodeAt(i); }
    s(0, 'RIFF'); dv.setUint32(4, 36 + n, true); s(8, 'WAVE'); s(12, 'fmt ');
    dv.setUint32(16, 16, true); dv.setUint16(20, 1, true); dv.setUint16(22, 1, true);
    dv.setUint32(24, 8000, true); dv.setUint32(28, 8000, true);
    dv.setUint16(32, 1, true); dv.setUint16(34, 8, true); s(36, 'data'); dv.setUint32(40, n, true);
    for (var i = 44; i < bytes.length; i++) bytes[i] = 128;
    var bin = '';
    for (var j = 0; j < bytes.length; j++) bin += String.fromCharCode(bytes[j]);
    return 'data:audio/wav;base64,' + btoa(bin);
  })();

  function azUnlock() {
    var a = azAudio();
    if (a.dataset && a.dataset.unlocked) return;
    try {
      a.src = SILENCE;
      var p = a.play();
      if (p && p.catch) p.catch(function () { /* ignore */ });
      if (a.dataset) a.dataset.unlocked = '1';
    } catch (e) { /* ignore */ }
  }

  function azReset(keepClips) {
    AZ.gen += 1;
    AZ.loaded = -1;
    if (AZ.audio) {
      AZ.audio.onended = null;
      AZ.audio.onerror = null;
      try { AZ.audio.pause(); } catch (e) { /* ignore */ }
    }
    if (!keepClips) {
      AZ.urls.forEach(function (u) { try { URL.revokeObjectURL(u); } catch (e) { /* ignore */ } });
      AZ.urls = [];
      AZ.clips = {};
    }
  }

  function clipUrl(i) {
    if (AZ.clips[i]) return AZ.clips[i];
    var item = Engine.queue[i];
    if (!item || item.engine !== 'azure') return Promise.resolve(null);
    var p = fetchClip(item).then(function (blob) {
      var u = URL.createObjectURL(blob);
      AZ.urls.push(u);
      return u;
    });
    p.catch(function () { if (AZ.clips[i] === p) delete AZ.clips[i]; });
    AZ.clips[i] = p;
    return p;
  }

  function prefetch(from) {
    for (var k = from; k < Math.min(Engine.queue.length, from + 2); k++) {
      if (Engine.queue[k].engine === 'azure') clipUrl(k).catch(function () { /* traité à la lecture */ });
    }
  }

  function fail(message) {
    var handler = Engine.onError;
    var at = Engine.index;
    engineStop();
    if (handler) handler(message, at);
  }

  function engineStop() {
    clearTimers();
    azReset(false);
    Engine.queue = [];
    Engine.index = 0;
    Engine.playing = false;
    Engine.paused = false;
    Engine.current = null;
    if (SUPPORTED) { try { window.speechSynthesis.cancel(); } catch (e) { /* ignore */ } }
  }

  function engineStart(queue, handlers, startIndex) {
    engineStop();
    Engine.queue = queue;
    Engine.index = Math.max(0, Math.min(startIndex || 0, queue.length - 1));
    Engine.playing = true;
    Engine.paused = false;
    Engine.onProgress = handlers.onProgress || null;
    Engine.onDone = handlers.onDone || null;
    Engine.onError = handlers.onError || null;
    if (queue.some(function (q) { return q.engine === 'azure'; })) azUnlock();
    // Chrome garde parfois une file fantôme après un cancel()
    setTimeout(speakCurrent, 60);
  }

  function advance() {
    clearTimers();
    Engine.index += 1;
    speakCurrent();
  }

  function speakCurrent() {
    if (!Engine.playing || Engine.paused) return;
    if (Engine.index >= Engine.queue.length) {
      var done = Engine.onDone;
      engineStop();
      if (done) done();
      return;
    }
    var item = Engine.queue[Engine.index];
    if (Engine.onProgress) Engine.onProgress(item.meta, Engine.index, Engine.queue.length);
    if (item.engine === 'azure') speakAzure(item);
    else speakWeb(item);
  }

  function speakAzure(item) {
    var gen = AZ.gen;
    var index = Engine.index;
    clipUrl(index).then(function (url) {
      if (gen !== AZ.gen || !Engine.playing || index !== Engine.index) return;
      var a = azAudio();
      var finished = false;
      a.onended = function () {
        if (finished || gen !== AZ.gen) return;
        finished = true;
        advance();
      };
      a.onerror = function () {
        if (gen !== AZ.gen) return;
        fail('Lecture de l\'extrait impossible.');
      };
      a.src = url;
      a.playbackRate = item.rate || 1;
      AZ.loaded = index;
      prefetch(index + 1);
      if (Engine.paused) return;
      var p = a.play();
      if (p && p.catch) {
        p.catch(function (err) {
          if (gen !== AZ.gen) return;
          if (err && err.name === 'AbortError') return;
          // Lecture bloquée par le navigateur : on attend un clic sur « Reprendre »
          Engine.paused = true;
          if (Engine.onError) Engine.onError('blocked', index);
        });
      }
    }, function (err) {
      if (gen !== AZ.gen) return;
      fail((err && err.message) || 'Azure indisponible');
    });
  }

  function speakWeb(item) {
    if (!SUPPORTED) { fail('Synthèse du navigateur indisponible'); return; }
    var u = new SpeechSynthesisUtterance(speakable(item.text));
    u.lang = (item.voice && item.voice.lang) || 'fr-FR';
    if (item.voice) u.voice = item.voice;
    u.rate = clamp((item.rate || 1) * (item.toneRate || 1), 0.5, 2);
    u.pitch = item.pitch || 1;
    u.volume = 1;

    var advanced = false;
    function next() {
      if (advanced) return;
      advanced = true;
      advance();
    }

    u.onend = next;
    u.onerror = function (e) {
      // « interrupted » et « canceled » viennent de nos propres arrêts : on ne relance pas
      if (e && (e.error === 'interrupted' || e.error === 'canceled')) { advanced = true; return; }
      next();
    };

    Engine.current = u;
    try { window.speechSynthesis.speak(u); } catch (e) { next(); return; }

    /* Filet de sécurité : si onend ne se déclenche jamais (bug connu de
       Chrome et de quelques WebView), on avance au bout d'une durée
       largement supérieure au temps de lecture attendu. */
    var expected = (item.text.length / 12) * 1000 / (u.rate || 1);
    clearTimers();
    Engine.watchdog = setTimeout(function () {
      if (!Engine.paused) next();
    }, Math.max(4000, expected * 2.4 + 2500));

    // Chrome suspend la synthèse au bout de ~15 s : ce ping la maintient éveillée
    Engine.keepAlive = setInterval(function () {
      if (Engine.paused || !Engine.playing) return;
      try {
        window.speechSynthesis.pause();
        window.speechSynthesis.resume();
      } catch (e) { /* ignore */ }
    }, 9000);
  }

  function currentEngine() {
    var item = Engine.queue[Engine.index];
    return item ? item.engine : null;
  }

  function enginePause() {
    if (!Engine.playing || Engine.paused) return;
    Engine.paused = true;
    clearTimers();
    if (currentEngine() === 'azure') {
      if (AZ.audio) AZ.audio.pause();
    } else {
      try { window.speechSynthesis.pause(); } catch (e) { /* ignore */ }
    }
  }

  function engineResume() {
    if (!Engine.playing || !Engine.paused) return;
    Engine.paused = false;
    if (currentEngine() === 'azure') {
      if (AZ.loaded === Engine.index && AZ.audio) {
        var p = AZ.audio.play();
        if (p && p.catch) p.catch(function () { /* ignore */ });
      } else {
        speakCurrent();
      }
      return;
    }
    try { window.speechSynthesis.resume(); } catch (e) { /* ignore */ }
    // Certaines plateformes perdent l'énonciation en pause : on la relance
    setTimeout(function () {
      if (Engine.playing && !Engine.paused && !window.speechSynthesis.speaking) speakCurrent();
    }, 320);
  }

  function engineJump(index) {
    if (!Engine.queue.length) return;
    Engine.index = Math.max(0, Math.min(index, Engine.queue.length - 1));
    Engine.paused = false;
    clearTimers();
    azReset(true);
    if (SUPPORTED) { try { window.speechSynthesis.cancel(); } catch (e) { /* ignore */ } }
    setTimeout(speakCurrent, 80);
  }

  /* Vitesse modifiée en cours d'écoute : immédiate avec Azure,
     reprise de la phrase en cours avec la voix du navigateur. */
  function engineSetRate(rate) {
    Engine.queue.forEach(function (q) { q.rate = rate; });
    if (!Engine.playing) return;
    if (currentEngine() === 'azure') {
      if (AZ.audio) AZ.audio.playbackRate = rate;
    } else if (!Engine.paused) {
      engineJump(Engine.index);
    }
  }

  // Un onglet qu'on quitte ne doit pas continuer à parler dans le vide
  window.addEventListener('pagehide', engineStop);
  window.addEventListener('beforeunload', engineStop);

  /* ============================================================
     3. Sélecteurs communs : voix, ton, vitesse
     ============================================================ */

  function fillVoiceSelect(select, selectedKey) {
    select.innerHTML = '';
    if (azureUsable()) {
      var g = document.createElement('optgroup');
      g.label = 'Azure — voix neuronales';
      Azure.voices.forEach(function (v) {
        var o = document.createElement('option');
        o.value = 'az:' + v.name;
        var extra = [];
        if (v.locale !== 'fr-FR' && /^fr-/i.test(v.locale)) extra.push(v.locale.slice(3));
        if (v.multilingual) extra.push('multilingue');
        if (v.hd) extra.push('HD');
        if (v.styles && v.styles.length) extra.push(v.styles.length + ' styles');
        o.textContent = v.label + (v.gender === 'Female' ? ' ♀' : v.gender === 'Male' ? ' ♂' : '') +
          (extra.length ? ' · ' + extra.join(', ') : '');
        g.appendChild(o);
      });
      select.appendChild(g);
    }
    if (webAvailable()) {
      var w = document.createElement('optgroup');
      w.label = 'Voix du navigateur' + (azureUsable() ? ' (hors ligne)' : '');
      frenchVoices().forEach(function (v) {
        var o = document.createElement('option');
        o.value = 'web:' + v.name;
        o.textContent = v.name.replace(/^Microsoft\s+/, '').replace(/\s*-\s*French.*$/i, '') +
          (v.localService ? '' : ' (en ligne)');
        w.appendChild(o);
      });
      select.appendChild(w);
    }
    if (!select.options.length) {
      var none = document.createElement('option');
      none.textContent = 'Aucune voix';
      select.appendChild(none);
      select.disabled = true;
      return;
    }
    select.disabled = false;
    if (selectedKey && validVoiceKey(selectedKey)) select.value = selectedKey;
  }

  function fillToneSelect(select, voiceKey, selectedTone) {
    select.innerHTML = '';
    var g = document.createElement('optgroup');
    g.label = 'Tons';
    TONE_PRESETS.forEach(function (t) {
      var o = document.createElement('option');
      o.value = 'p:' + t.id;
      o.textContent = t.label;
      g.appendChild(o);
    });
    select.appendChild(g);

    var v = isAzureKey(voiceKey) ? azureVoice(keyName(voiceKey)) : null;
    if (v && v.styles && v.styles.length) {
      var s = document.createElement('optgroup');
      s.label = 'Styles de ' + v.label;
      v.styles.forEach(function (st) {
        var o = document.createElement('option');
        o.value = 's:' + st;
        o.textContent = STYLE_LABELS[st] || st;
        s.appendChild(o);
      });
      select.appendChild(s);
    }
    select.value = selectedTone || 'p:neutre';
    if (select.value !== selectedTone) select.value = 'p:neutre';
  }

  function rateOptions() {
    return RATES.map(function (r) {
      return '<option value="' + r + '">' + rateLabel(r) + '</option>';
    }).join('');
  }

  /* ============================================================
     4. Extraction du texte lisible d'un module
     ============================================================ */

  var SKIP = 'script, style, .fold-next, .fold-toolbar, .quiz-section, .module-nav, .audio-bar, .podcast-box, .read-progress, .toast, .to-top';

  function readableNodes(root) {
    var nodes = [];
    var walker = root.querySelectorAll('p, li, dt, dd, h3, h4, h2, th, td, summary');
    Array.prototype.forEach.call(walker, function (el) {
      if (el.closest(SKIP)) return;
      if (el.closest('.solution-box') && el.tagName === 'SUMMARY') return;
      var text = (el.textContent || '').replace(/\s+/g, ' ').trim();
      if (text.length < 3) return;
      // On évite de lire deux fois un texte déjà couvert par un parent retenu
      if (nodes.length && nodes[nodes.length - 1].el.contains(el)) return;
      nodes.push({ el: el, text: text });
    });
    return nodes;
  }

  /* Construit la liste des pistes : une par volet du module. */
  function buildTracks(content) {
    content = content || document.querySelector('.module-content');
    if (!content) return [];

    var tracks = [];
    var intro = [];

    // Mise en situation et objectifs restent hors des volets
    ['.intro-box', '.objectives-box'].forEach(function (sel) {
      var box = content.querySelector(':scope > ' + sel);
      if (box) intro.push(box);
    });
    if (intro.length) {
      var introNodes = [];
      intro.forEach(function (box) { introNodes = introNodes.concat(readableNodes(box)); });
      if (introNodes.length) {
        tracks.push({ titre: 'Mise en situation et objectifs', fold: null, nodes: introNodes });
      }
    }

    var folds = content.querySelectorAll('details.section-fold');
    Array.prototype.forEach.call(folds, function (fold) {
      var titleEl = fold.querySelector(':scope > summary .fold-title');
      var body = fold.querySelector(':scope > .fold-body');
      if (!body) return;
      var nodes = readableNodes(body);
      if (!nodes.length) return;
      tracks.push({
        titre: titleEl ? titleEl.textContent.trim() : 'Section',
        fold: fold,
        nodes: nodes
      });
    });

    return tracks;
  }

  /* Azure : on regroupe les paragraphes courts d'une même section
     (≈ 700 caractères) pour limiter le nombre de requêtes — le palier
     gratuit est limité en requêtes par minute. */
  var AZ_GROUP = 700;
  var AZ_CHUNK = 1200;

  function trackQueue(tracks, voiceKey, toneKey, rate) {
    var queue = [];
    var azure = isAzureKey(voiceKey);

    tracks.forEach(function (track, ti) {
      queue.push(makeItem(speakable(track.titre) + '.', voiceKey, toneKey, rate,
        { track: ti, els: [], titre: track.titre, heading: true }));

      if (!azure) {
        track.nodes.forEach(function (node) {
          chunkText(node.text, 210).forEach(function (c) {
            queue.push(makeItem(c, voiceKey, toneKey, rate,
              { track: ti, els: [node.el], titre: track.titre, heading: false }));
          });
        });
        return;
      }

      var bufText = '';
      var bufEls = [];
      function flush() {
        if (!bufText) return;
        queue.push(makeItem(bufText, voiceKey, toneKey, rate,
          { track: ti, els: bufEls, titre: track.titre, heading: false }));
        bufText = '';
        bufEls = [];
      }
      track.nodes.forEach(function (node) {
        var t = speakable(node.text);
        if (!/[.!?…:;]$/.test(t)) t += '.';
        if (t.length > AZ_CHUNK) {
          flush();
          chunkText(t, AZ_CHUNK).forEach(function (c) {
            queue.push(makeItem(c, voiceKey, toneKey, rate,
              { track: ti, els: [node.el], titre: track.titre, heading: false }));
          });
          return;
        }
        if (bufText && (bufText.length + t.length + 1) > AZ_GROUP) flush();
        bufText = bufText ? bufText + ' ' + t : t;
        bufEls.push(node.el);
      });
      flush();
    });
    return queue;
  }

  /* ============================================================
     5. Le lecteur « Écouter le module »
     ============================================================ */

  function moduleId() {
    var btn = document.getElementById('btn-mark-complete');
    return (btn && btn.dataset.moduleId) || location.pathname;
  }

  /* Lien vers les réglages : voix, ton et vitesse ne se choisissent
     que sur la page Paramètres. */
  function settingsLink() {
    return '<a class="audio-settings-link" href="' + ROOT + 'parametres.html#audio-settings-panel" ' +
      'title="Voix, ton et vitesse se règlent dans Paramètres">⚙ Voix et vitesse</a>';
  }

  function buildControls(bar, opts) {
    bar.innerHTML =
      '<div class="audio-row">' +
      '  <button type="button" class="btn btn-primary btn-sm audio-play" aria-label="Lire ou mettre en pause">▶ ' + opts.label + '</button>' +
      '  <button type="button" class="btn btn-ghost btn-sm audio-prev" title="Section précédente" aria-label="Section précédente" hidden>⏮</button>' +
      '  <button type="button" class="btn btn-ghost btn-sm audio-next" title="Section suivante" aria-label="Section suivante" hidden>⏭</button>' +
      '  <button type="button" class="btn btn-ghost btn-sm audio-stop" title="Arrêter" aria-label="Arrêter la lecture" hidden>⏹</button>' +
      '  <span class="audio-status" role="status" aria-live="polite"></span>' +
      '  <span class="audio-engine" aria-hidden="true"></span>' +
      '  ' + settingsLink() +
      '</div>' +
      '<div class="audio-progress" aria-hidden="true"><span></span></div>';

    // Les réglages restent en mémoire (préférences de Paramètres),
    // sans être affichés sur la page du module.
    var hidden = document.createElement('div');
    hidden.innerHTML =
      '<div class="audio-row audio-settings">' +
      '  <label class="audio-field audio-voice-field"><span>Voix</span>' +
      '    <select class="audio-voice" aria-label="Voix de lecture"></select></label>' +
      '  <label class="audio-field"><span>Ton</span>' +
      '    <select class="audio-tone" aria-label="Ton de la voix"></select></label>' +
      '  <label class="audio-field"><span>Vitesse</span>' +
      '    <select class="audio-rate" aria-label="Vitesse de lecture">' + rateOptions() + '</select></label>' +
      '</div>';

    var ui = {
      play: bar.querySelector('.audio-play'),
      prev: bar.querySelector('.audio-prev'),
      next: bar.querySelector('.audio-next'),
      stop: bar.querySelector('.audio-stop'),
      status: bar.querySelector('.audio-status'),
      rate: hidden.querySelector('.audio-rate'),
      voice: hidden.querySelector('.audio-voice'),
      tone: hidden.querySelector('.audio-tone'),
      engine: bar.querySelector('.audio-engine'),
      progress: bar.querySelector('.audio-progress span')
    };

    // Ancienne préférence (V7) : nom de voix système sans préfixe
    if (!prefs.voiceKey && prefs.voice) prefs.voiceKey = 'web:' + prefs.voice;
    var key = validVoiceKey(prefs.voiceKey) ? prefs.voiceKey : defaultVoiceKey('Female');
    fillVoiceSelect(ui.voice, key);
    fillToneSelect(ui.tone, ui.voice.value, prefs.tone);
    ui.rate.value = String(nearestRate(prefs.rate || 1));
    return ui;
  }

  function paintEngineBadge(el, voiceKey) {
    if (!el) return;
    var az = isAzureKey(voiceKey);
    el.textContent = az ? 'Azure' : 'Navigateur';
    el.className = 'audio-engine ' + (az ? 'is-azure' : 'is-web');
    el.title = az ? 'Voix neuronale Microsoft Azure' : 'Voix du système, fonctionne hors ligne';
  }

  function initModulePlayer() {
    var header = document.querySelector('.module-header');
    var content = document.querySelector('.module-content');
    if (!header || !content) return null;

    var bar = document.createElement('section');
    bar.className = 'audio-bar';
    bar.setAttribute('aria-label', 'Écoute du module');
    header.parentNode.insertBefore(bar, header.nextSibling);

    if (!anyVoice()) {
      if (!SUPPORTED) {
        bar.innerHTML = '<p class="audio-unsupported">🔇 Aucune voix disponible : ce navigateur ne propose pas de ' +
          'synthèse vocale et les voix Azure ne répondent pas' + (Azure.error ? ' (' + Azure.error + ')' : '') + '.</p>';
        return null;
      }
      bar.innerHTML = '<p class="audio-unsupported">🔇 Aucune voix disponible. Les voix Azure ne répondent pas' +
        (Azure.error ? ' (' + Azure.error + ')' : ' (hors ligne ?)') + ', et aucune voix française n\'est installée ' +
        'sur cet appareil. Sous Windows, ajoutez-en une dans <em>Paramètres → Heure et langue → Voix</em>, ' +
        'puis rechargez la page.</p>';
      return null;
    }

    var ui = buildControls(bar, { label: 'Écouter le module' });
    var tracks = buildTracks();
    if (!tracks.length) { bar.remove(); return null; }
    paintEngineBadge(ui.engine, ui.voice.value);

    var state = { active: false, queue: [], track: -1, els: [] };
    var resumeStore = readStore(POS_KEY, {}) || {};
    // Position mémorisée par section (indépendante de la voix choisie)
    var saved = resumeStore[moduleId()];
    var savedTrack = (saved && typeof saved === 'object' && typeof saved.t === 'number') ? saved.t : null;

    function currentRate() { return parseFloat(ui.rate.value) || 1; }

    function clearHighlight() {
      state.els.forEach(function (el) { el.classList.remove('is-speaking'); });
      state.els = [];
    }

    function paint(meta, index, total) {
      if (typeof index === 'number' && total) {
        ui.progress.style.width = Math.round(((index + 1) / total) * 100) + '%';
      }
      if (!meta) return;

      clearHighlight();
      state.els = (meta.els || []).slice();
      state.els.forEach(function (el) { el.classList.add('is-speaking'); });
      var first = state.els[0];
      if (first) {
        var rect = first.getBoundingClientRect();
        if (rect.top < 90 || rect.bottom > window.innerHeight - 60) {
          first.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }

      if (meta.track !== state.track) {
        // Le volet qu'on quitte se referme : la page reste lisible pendant l'écoute
        var previous = tracks[state.track];
        if (previous && previous.fold && meta.track > state.track) previous.fold.open = false;
        state.track = meta.track;
        resumeStore[moduleId()] = { t: meta.track };
        writeStore(POS_KEY, resumeStore);
        var track = tracks[meta.track];
        if (track && track.fold) {
          track.fold.open = true;
          if (typeof window.markRead === 'function') window.markRead(track.fold);
        }
      }
      ui.status.textContent = 'Section ' + (meta.track + 1) + '/' + tracks.length + ' — ' + meta.titre;
    }

    function indexOfTrack(queue, t) {
      for (var i = 0; i < queue.length; i++) if (queue[i].meta.track === t) return i;
      return 0;
    }

    function indexOfEl(queue, el, fallbackTrack) {
      if (el) {
        for (var i = 0; i < queue.length; i++) {
          if ((queue[i].meta.els || []).indexOf(el) !== -1) return i;
        }
      }
      return indexOfTrack(queue, fallbackTrack || 0);
    }

    function onError(message, at) {
      if (message === 'blocked') {
        ui.play.textContent = '▶ Reprendre';
        bar.classList.remove('is-playing');
        ui.status.textContent = 'Le navigateur a bloqué la lecture — cliquez sur Reprendre.';
        return;
      }
      var meta = state.queue[at] && state.queue[at].meta;
      var fallback = isAzureKey(ui.voice.value) ? webFallbackKey() : null;
      stop();
      if (fallback) {
        // Azure indisponible (hors ligne, quota…) : la voix du navigateur prend le relais
        ui.voice.value = fallback;
        fillToneSelect(ui.tone, fallback, ui.tone.value);
        paintEngineBadge(ui.engine, fallback);
        var q = trackQueue(tracks, fallback, ui.tone.value, currentRate());
        start(indexOfEl(q, meta && meta.els && meta.els[0], meta && meta.track), q);
        ui.status.textContent = '⚠ Azure indisponible (' + message + ') — voix du navigateur.';
        return;
      }
      ui.status.textContent = '⚠ Lecture interrompue : ' + message;
    }

    function start(fromIndex, prebuilt) {
      state.queue = prebuilt || trackQueue(tracks, ui.voice.value, ui.tone.value, currentRate());
      state.startedAt = Date.now();
      state.active = true;
      state.track = -1;
      bar.classList.add('is-playing');
      ui.play.textContent = '⏸ Pause';
      [ui.prev, ui.next, ui.stop].forEach(function (b) { b.hidden = false; });
      engineStart(state.queue, {
        onProgress: paint,
        onError: onError,
        onDone: function () {
          var duree = Date.now() - state.startedAt;
          stop();
          if (duree < 2500 && state.queue.length > 8) {
            // La synthèse n'a rien prononcé : voix indisponible ou bloquée
            ui.status.textContent = '🔇 La voix n\'a pas démarré — vérifiez les voix du système.';
            return;
          }
          ui.status.textContent = '✓ Module lu en entier.';
          delete resumeStore[moduleId()];
          writeStore(POS_KEY, resumeStore);
        }
      }, fromIndex || 0);
    }

    function stop() {
      engineStop();
      state.active = false;
      state.track = -1;
      clearHighlight();
      bar.classList.remove('is-playing');
      ui.play.textContent = '▶ Écouter le module';
      [ui.prev, ui.next, ui.stop].forEach(function (b) { b.hidden = true; });
      ui.progress.style.width = '0%';
    }

    function trackStartIndex(delta) {
      var meta = Engine.queue[Engine.index] && Engine.queue[Engine.index].meta;
      if (!meta) return 0;
      var target = Math.max(0, Math.min(tracks.length - 1, meta.track + delta));
      return indexOfTrack(Engine.queue, target);
    }

    ui.play.addEventListener('click', function () {
      if (!state.active) {
        if (savedTrack) {
          var q = trackQueue(tracks, ui.voice.value, ui.tone.value, currentRate());
          start(indexOfTrack(q, savedTrack), q);
          savedTrack = null;
        } else {
          start(0);
        }
        return;
      }
      if (Engine.paused) {
        engineResume();
        ui.play.textContent = '⏸ Pause';
        bar.classList.add('is-playing');
      } else {
        enginePause();
        ui.play.textContent = '▶ Reprendre';
        bar.classList.remove('is-playing');
      }
    });

    ui.stop.addEventListener('click', stop);
    ui.prev.addEventListener('click', function () { if (state.active) engineJump(trackStartIndex(-1)); });
    ui.next.addEventListener('click', function () { if (state.active) engineJump(trackStartIndex(1)); });

    /* Changement de voix ou de ton : on reprend au passage en cours */
    function restartWhereWeAre() {
      if (!state.active) return;
      var cur = Engine.queue[Engine.index];
      var meta = cur && cur.meta;
      var q = trackQueue(tracks, ui.voice.value, ui.tone.value, currentRate());
      start(indexOfEl(q, meta && meta.els && meta.els[0], meta && meta.track), q);
    }

    ui.rate.addEventListener('change', function () {
      prefs.rate = currentRate();
      savePrefs();
      engineSetRate(currentRate());
    });

    ui.voice.addEventListener('change', function () {
      prefs.voiceKey = ui.voice.value;
      fillToneSelect(ui.tone, ui.voice.value, ui.tone.value);
      prefs.tone = ui.tone.value;
      paintEngineBadge(ui.engine, ui.voice.value);
      savePrefs();
      restartWhereWeAre();
    });

    ui.tone.addEventListener('change', function () {
      prefs.tone = ui.tone.value;
      savePrefs();
      restartWhereWeAre();
    });

    if (savedTrack) {
      ui.status.textContent = '⏱ Reprise possible à la section ' + (savedTrack + 1) + '.';
    } else {
      ui.status.textContent = tracks.length + ' sections à écouter.';
    }

    return { stop: stop, isActive: function () { return state.active; } };
  }

  /* ============================================================
     6. Le lecteur de podcast
     ============================================================ */

  function podcastVoiceKeys() {
    var a = validVoiceKey(prefs.podVoiceA) ? prefs.podVoiceA : null;
    var b = validVoiceKey(prefs.podVoiceB) ? prefs.podVoiceB : null;
    if (!a) a = defaultVoiceKey('Female');
    if (!b) {
      if (azureUsable()) b = defaultVoiceKey('Male');
      else {
        var fr = frenchVoices();
        var other = fr.filter(function (v) { return 'web:' + v.name !== a; })[0];
        b = other ? 'web:' + other.name : a;
      }
    }
    return { a: a, b: b };
  }

  /* File de lecture d'un podcast — partagée avec le téléchargement hors ligne,
     pour que les extraits téléchargés soient exactement ceux qu'on écoute. */
  function podcastQueue(lignes, ka, kb, toneKey, rate) {
    var same = ka === kb && !isAzureKey(ka);
    var q = [];
    lignes.forEach(function (l, i) {
      var isB = l.v === 'b';
      var key = isB ? kb : ka;
      // Une seule voix système pour deux personnes : on les distingue par la hauteur
      var pitch = same ? (isB ? 0.85 : 1.12) : 1;
      var limit = isAzureKey(key) ? AZ_CHUNK : 210;
      chunkText(isAzureKey(key) ? speakable(l.t) : l.t, limit).forEach(function (c) {
        q.push(makeItem(c, key, toneKey, rate, { line: i }, pitch));
      });
    });
    return q;
  }

  /* Le ton du podcast : celui de l'intervenant dont la voix sait le faire */
  function podcastTone(ka, kb, toneKey) {
    var va = isAzureKey(ka) ? azureVoice(keyName(ka)) : null;
    var vb = isAzureKey(kb) ? azureVoice(keyName(kb)) : null;
    var ref = (va && va.styles && va.styles.length) ? ka :
      (vb && vb.styles && vb.styles.length) ? kb : ka;
    // Même enchaînement que le lecteur : d'abord la voix A, puis la voix de référence
    var probe = document.createElement('select');
    fillToneSelect(probe, ka, toneKey);
    fillToneSelect(probe, ref, probe.value || toneKey);
    return probe.value;
  }

  function initPodcastPlayer(otherPlayer) {
    var header = document.querySelector('.module-header');
    if (!header) return;
    var anchor = document.querySelector('.audio-bar') || header;

    var box = document.createElement('details');
    box.className = 'podcast-box';
    box.innerHTML =
      '<summary><span class="podcast-mark" aria-hidden="true">🎧</span>' +
      '<span class="podcast-title">Podcast du module</span>' +
      '<span class="podcast-meta">chargement…</span></summary>' +
      '<div class="podcast-body"></div>';
    anchor.parentNode.insertBefore(box, anchor.nextSibling);

    var body = box.querySelector('.podcast-body');
    var meta = box.querySelector('.podcast-meta');

    fetch('podcast.json', { cache: 'no-cache' })
      .then(function (r) {
        if (!r.ok) throw new Error('absent');
        return r.json();
      })
      .then(function (data) { render(data); })
      .catch(function () {
        meta.textContent = 'à venir';
        box.classList.add('is-empty');
        body.innerHTML = '<p class="podcast-empty">Le podcast de ce module n\'est pas encore écrit. ' +
          'Le lecteur apparaîtra ici dès que <code>podcast.json</code> sera présent dans le dossier du module.</p>';
      });

    /* Script du podcast (texte des répliques), surligné pendant l'écoute. */
    function buildScript(data, nomA, nomB) {
      var lignes = (data && data.lignes) || [];
      var script = document.createElement('div');
      script.className = 'podcast-script';
      if (data.resume) {
        var intro = document.createElement('p');
        intro.className = 'podcast-resume';
        intro.textContent = data.resume;
        script.appendChild(intro);
      }
      lignes.forEach(function (l, i) {
        var line = document.createElement('p');
        line.className = 'podcast-line pod-' + (l.v === 'b' ? 'b' : 'a');
        line.dataset.line = String(i);
        var who = document.createElement('span');
        who.className = 'podcast-who';
        who.textContent = (l.v === 'b' ? nomB : nomA);
        var txt = document.createElement('span');
        txt.className = 'podcast-text';
        txt.textContent = l.t;
        line.appendChild(who);
        line.appendChild(txt);
        script.appendChild(line);
      });
      return script;
    }

    function render(data) {
      var lignes = (data && data.lignes) || [];
      if (!lignes.length) { meta.textContent = 'à venir'; return; }

      var hosts = (data && data.hosts) || {};
      var nomA = (hosts.a && hosts.a.nom) || 'Animatrice';
      var nomB = (hosts.b && hosts.b.nom) || 'Expert';
      meta.textContent = (data.duree_estimee || '') + (data.duree_estimee ? ' · ' : '') +
        nomA + ' & ' + nomB + (Azure.enabled ? ' · voix Azure' : '');

      var script = buildScript(data, nomA, nomB);

      if (!anyVoice()) {
        body.innerHTML = '<p class="podcast-empty">Aucune voix disponible sur cet appareil : ' +
          'le texte du podcast reste lisible ci-dessous.</p>';
        body.appendChild(script);
        return;
      }

      var wrap = document.createElement('div');
      wrap.className = 'podcast-player';
      wrap.innerHTML =
        '<div class="audio-row">' +
        '  <button type="button" class="btn btn-primary btn-sm pod-play">▶ Écouter le podcast</button>' +
        '  <button type="button" class="btn btn-ghost btn-sm pod-stop" hidden aria-label="Arrêter le podcast">⏹</button>' +
        '  <span class="audio-status pod-status" role="status" aria-live="polite"></span>' +
        '  ' + settingsLink() +
        '</div>' +
        '<div class="audio-progress" aria-hidden="true"><span></span></div>';

      // Réglages en mémoire seulement : ils se changent dans Paramètres
      var hidden = document.createElement('div');
      hidden.innerHTML =
        '<div class="audio-row audio-settings">' +
        '  <label class="audio-field audio-voice-field"><span></span><select class="pod-voice-a"></select></label>' +
        '  <label class="audio-field audio-voice-field"><span></span><select class="pod-voice-b"></select></label>' +
        '  <label class="audio-field"><span>Ton</span><select class="pod-tone" aria-label="Ton du podcast"></select></label>' +
        '  <label class="audio-field"><span>Vitesse</span>' +
        '    <select class="pod-rate" aria-label="Vitesse du podcast">' + rateOptions() + '</select></label>' +
        '</div>';

      body.innerHTML = '';
      body.appendChild(wrap);
      body.appendChild(script);

      var ui = {
        play: wrap.querySelector('.pod-play'),
        stop: wrap.querySelector('.pod-stop'),
        status: wrap.querySelector('.pod-status'),
        rate: hidden.querySelector('.pod-rate'),
        voiceA: hidden.querySelector('.pod-voice-a'),
        voiceB: hidden.querySelector('.pod-voice-b'),
        tone: hidden.querySelector('.pod-tone'),
        progress: wrap.querySelector('.audio-progress span')
      };
      var labels = hidden.querySelectorAll('.audio-voice-field > span');
      labels[0].textContent = nomA;
      labels[1].textContent = nomB;
      ui.voiceA.setAttribute('aria-label', 'Voix de ' + nomA);
      ui.voiceB.setAttribute('aria-label', 'Voix de ' + nomB);

      var keys = podcastVoiceKeys();
      fillVoiceSelect(ui.voiceA, keys.a);
      fillVoiceSelect(ui.voiceB, keys.b);
      fillToneSelect(ui.tone, ui.voiceA.value, prefs.podTone);
      ui.rate.value = String(nearestRate(prefs.podcastRate || 1));

      var active = false;
      var startedAt = 0;
      var currentLine = null;
      var queue = [];

      function highlight(index) {
        if (currentLine) currentLine.classList.remove('is-speaking');
        var el = script.querySelector('[data-line="' + index + '"]');
        currentLine = el;
        if (!el) return;
        el.classList.add('is-speaking');
        var rect = el.getBoundingClientRect();
        if (rect.top < 80 || rect.bottom > window.innerHeight - 40) {
          el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }

      /* Les styles Azure dépendent de la voix : le ton choisi est appliqué
         à chaque intervenant s'il le sait faire, sinon il reste neutre. */
      function refreshTones() {
        var union = ui.voiceA.value;
        var va = isAzureKey(ui.voiceA.value) ? azureVoice(keyName(ui.voiceA.value)) : null;
        var vb = isAzureKey(ui.voiceB.value) ? azureVoice(keyName(ui.voiceB.value)) : null;
        if (!(va && va.styles && va.styles.length) && vb && vb.styles && vb.styles.length) union = ui.voiceB.value;
        fillToneSelect(ui.tone, union, ui.tone.value || prefs.podTone);
      }
      refreshTones();

      function buildQueue() {
        return podcastQueue(lignes, ui.voiceA.value, ui.voiceB.value, ui.tone.value,
          parseFloat(ui.rate.value) || 1);
      }

      function indexOfLine(q, line) {
        for (var i = 0; i < q.length; i++) if (q[i].meta.line === line) return i;
        return 0;
      }

      function onError(message, at) {
        if (message === 'blocked') {
          ui.play.textContent = '▶ Reprendre';
          ui.status.textContent = 'Le navigateur a bloqué la lecture — cliquez sur Reprendre.';
          return;
        }
        var line = queue[at] && queue[at].meta.line;
        var fb = webFallbackKey();
        var usedAzure = isAzureKey(ui.voiceA.value) || isAzureKey(ui.voiceB.value);
        stop();
        if (usedAzure && fb) {
          if (isAzureKey(ui.voiceA.value)) ui.voiceA.value = fb;
          if (isAzureKey(ui.voiceB.value)) ui.voiceB.value = fb;
          refreshTones();
          start(line || 0);
          ui.status.textContent = '⚠ Azure indisponible (' + message + ') — voix du navigateur.';
          return;
        }
        ui.status.textContent = '⚠ Lecture interrompue : ' + message;
      }

      function start(fromLine) {
        if (otherPlayer && otherPlayer.isActive && otherPlayer.isActive()) otherPlayer.stop();
        queue = buildQueue();
        active = true;
        startedAt = Date.now();
        box.open = true;
        ui.play.textContent = '⏸ Pause';
        ui.stop.hidden = false;
        engineStart(queue, {
          onProgress: function (m, index, total) {
            ui.progress.style.width = Math.round(((index + 1) / total) * 100) + '%';
            if (m) {
              highlight(m.line);
              ui.status.textContent = 'Réplique ' + (m.line + 1) + '/' + lignes.length;
            }
          },
          onError: onError,
          onDone: function () {
            var duree = Date.now() - startedAt;
            stop();
            ui.status.textContent = (duree < 2500 && lignes.length > 8)
              ? '🔇 La voix n\'a pas démarré — vérifiez les voix du système.'
              : '✓ Podcast terminé.';
          }
        }, indexOfLine(queue, fromLine || 0));
      }

      function stop() {
        engineStop();
        active = false;
        if (currentLine) currentLine.classList.remove('is-speaking');
        currentLine = null;
        ui.play.textContent = '▶ Écouter le podcast';
        ui.stop.hidden = true;
        ui.progress.style.width = '0%';
      }

      function currentLineIndex() {
        var it = Engine.queue[Engine.index];
        return it ? it.meta.line : 0;
      }

      ui.play.addEventListener('click', function () {
        if (!active) { start(0); return; }
        if (Engine.paused) { engineResume(); ui.play.textContent = '⏸ Pause'; }
        else { enginePause(); ui.play.textContent = '▶ Reprendre'; }
      });
      ui.stop.addEventListener('click', stop);

      ui.rate.addEventListener('change', function () {
        prefs.podcastRate = parseFloat(ui.rate.value) || 1;
        savePrefs();
        engineSetRate(prefs.podcastRate);
      });

      function onVoiceOrTone() {
        prefs.podVoiceA = ui.voiceA.value;
        prefs.podVoiceB = ui.voiceB.value;
        prefs.podTone = ui.tone.value;
        savePrefs();
        if (active) start(currentLineIndex());
      }
      ui.voiceA.addEventListener('change', function () { refreshTones(); onVoiceOrTone(); });
      ui.voiceB.addEventListener('change', function () { refreshTones(); onVoiceOrTone(); });
      ui.tone.addEventListener('change', onVoiceOrTone);

      script.addEventListener('click', function (e) {
        var line = e.target.closest && e.target.closest('.podcast-line');
        if (!line) return;
        var target = parseInt(line.dataset.line, 10);
        if (isNaN(target)) return;
        if (!active) { start(target); return; }
        engineJump(indexOfLine(Engine.queue, target));
      });
    }
  }

  /* ============================================================
     7. Page Paramètres : voix par défaut, sans ouvrir un module
     ============================================================ */

  function initAudioSettingsPanel() {
    var panel = document.getElementById('audio-settings-panel');
    if (!panel) return;
    var body = panel.querySelector('.tool-body') || panel;

    if (!anyVoice()) {
      body.innerHTML = '<p class="tool-note">Aucune voix disponible pour l\'instant' +
        (Azure.error ? ' — Azure : ' + Azure.error : ' (hors ligne, ou aucune voix installée sur cet appareil)') +
        '.</p>';
      return;
    }

    body.innerHTML =
      '<p class="tool-note">Ces réglages s\'appliquent à tous les modules et à tous les podcasts. ' +
      'Les audios téléchargés pour le hors ligne sont enregistrés avec ces voix et ce ton ; la vitesse, elle, ' +
      'peut changer à tout moment sans rien retélécharger.</p>' +
      '<h3 class="settings-subtitle">Lecture d\'un module</h3>' +
      '<div class="audio-row audio-settings">' +
      '  <label class="audio-field audio-voice-field"><span>Voix</span>' +
      '    <select class="set-voice" aria-label="Voix par défaut des modules"></select></label>' +
      '  <label class="audio-field"><span>Ton</span>' +
      '    <select class="set-tone" aria-label="Ton par défaut"></select></label>' +
      '  <label class="audio-field"><span>Vitesse</span>' +
      '    <select class="set-rate" aria-label="Vitesse par défaut">' + rateOptions() + '</select></label>' +
      '</div>' +
      '<h3 class="settings-subtitle">Podcasts — deux intervenants</h3>' +
      '<div class="audio-row audio-settings">' +
      '  <label class="audio-field audio-voice-field"><span>Voix — animatrice</span>' +
      '    <select class="set-pod-a" aria-label="Voix par défaut de l\'animatrice"></select></label>' +
      '  <label class="audio-field audio-voice-field"><span>Voix — expert</span>' +
      '    <select class="set-pod-b" aria-label="Voix par défaut de l\'expert"></select></label>' +
      '</div>' +
      '<div class="audio-row audio-settings">' +
      '  <label class="audio-field"><span>Ton du podcast</span>' +
      '    <select class="set-pod-tone" aria-label="Ton par défaut du podcast"></select></label>' +
      '  <label class="audio-field"><span>Vitesse du podcast</span>' +
      '    <select class="set-pod-rate" aria-label="Vitesse par défaut du podcast">' + rateOptions() + '</select></label>' +
      '</div>';

    var ui = {
      voice: body.querySelector('.set-voice'),
      tone: body.querySelector('.set-tone'),
      rate: body.querySelector('.set-rate'),
      podA: body.querySelector('.set-pod-a'),
      podB: body.querySelector('.set-pod-b'),
      podTone: body.querySelector('.set-pod-tone'),
      podRate: body.querySelector('.set-pod-rate')
    };

    if (!prefs.voiceKey && prefs.voice) prefs.voiceKey = 'web:' + prefs.voice;
    var voiceKey = validVoiceKey(prefs.voiceKey) ? prefs.voiceKey : defaultVoiceKey('Female');
    fillVoiceSelect(ui.voice, voiceKey);
    fillToneSelect(ui.tone, ui.voice.value, prefs.tone);
    ui.rate.value = String(nearestRate(prefs.rate || 1));

    var podKeys = podcastVoiceKeys();
    fillVoiceSelect(ui.podA, podKeys.a);
    fillVoiceSelect(ui.podB, podKeys.b);
    fillToneSelect(ui.podTone, ui.podA.value, prefs.podTone);
    ui.podRate.value = String(nearestRate(prefs.podcastRate || 1));

    ui.voice.addEventListener('change', function () {
      prefs.voiceKey = ui.voice.value;
      fillToneSelect(ui.tone, ui.voice.value, ui.tone.value);
      prefs.tone = ui.tone.value;
      savePrefs();
    });
    ui.tone.addEventListener('change', function () { prefs.tone = ui.tone.value; savePrefs(); });
    ui.rate.addEventListener('change', function () { prefs.rate = parseFloat(ui.rate.value) || 1; savePrefs(); });

    function refreshPodTone() {
      var va = isAzureKey(ui.podA.value) ? azureVoice(keyName(ui.podA.value)) : null;
      var vb = isAzureKey(ui.podB.value) ? azureVoice(keyName(ui.podB.value)) : null;
      var union = (va && va.styles && va.styles.length) ? ui.podA.value :
        (vb && vb.styles && vb.styles.length) ? ui.podB.value : ui.podA.value;
      fillToneSelect(ui.podTone, union, ui.podTone.value || prefs.podTone);
    }
    ui.podA.addEventListener('change', function () {
      prefs.podVoiceA = ui.podA.value;
      refreshPodTone();
      prefs.podTone = ui.podTone.value;
      savePrefs();
    });
    ui.podB.addEventListener('change', function () {
      prefs.podVoiceB = ui.podB.value;
      refreshPodTone();
      prefs.podTone = ui.podTone.value;
      savePrefs();
    });
    ui.podTone.addEventListener('change', function () { prefs.podTone = ui.podTone.value; savePrefs(); });
    ui.podRate.addEventListener('change', function () { prefs.podcastRate = parseFloat(ui.podRate.value) || 1; savePrefs(); });
  }

  /* ============================================================
     7 bis. Page Paramètres : audios à emporter hors ligne
     Le texte est déjà hors ligne (offline.js). Ici, on télécharge les
     extraits Azure d'une formation — cours lus et/ou podcasts — avec
     exactement les voix réglées ci-dessus, pour qu'ils soient retrouvés
     à l'écoute. Tout se passe dans la page (pas dans le service worker) :
     c'est ce qui rend le téléchargement fiable sur mobile.
     ============================================================ */

  var BYTES_PER_CHAR = 430;      // MP3 48 kbit/s ≈ 6 Ko/s, ≈ 14 caractères lus par seconde
  var AZURE_FREE_CHARS = 500000; // palier gratuit Azure Speech (voix neuronales), par mois

  function humanMo(bytes) {
    var mo = bytes / (1024 * 1024);
    if (mo < 1) return '< 1 Mo';
    return (mo < 10 ? mo.toFixed(1).replace('.', ',') : Math.round(mo)) + ' Mo';
  }

  function humanChars(n) {
    if (n >= 1000000) return (n / 1000000).toFixed(1).replace('.', ',') + ' M';
    if (n >= 1000) return Math.round(n / 1000) + ' k';
    return String(n);
  }

  function resolvedVoice(key, gender) {
    var probe = document.createElement('select');
    fillVoiceSelect(probe, validVoiceKey(key) ? key : defaultVoiceKey(gender));
    return probe.value;
  }

  /* Voix réellement utilisées par les lecteurs, d'après les préférences */
  function currentVoices() {
    if (!prefs.voiceKey && prefs.voice) prefs.voiceKey = 'web:' + prefs.voice;
    var mv = resolvedVoice(prefs.voiceKey, 'Female');
    var mt = document.createElement('select');
    fillToneSelect(mt, mv, prefs.tone);
    var pk = podcastVoiceKeys();
    var pa = resolvedVoice(pk.a, 'Female');
    var pb = resolvedVoice(pk.b, 'Male');
    return {
      module: mv, moduleTone: mt.value,
      podA: pa, podB: pb, podTone: podcastTone(pa, pb, prefs.podTone)
    };
  }

  function voiceLabel(key) {
    if (isAzureKey(key)) {
      var v = azureVoice(keyName(key));
      return v ? v.label : keyName(key);
    }
    return keyName(key).replace(/^Microsoft\s+/, '').replace(/\s*-\s*French.*$/i, '') + ' (navigateur)';
  }

  function fetchText(url) {
    return fetch(url, { cache: 'no-cache' }).then(function (r) {
      if (!r.ok) throw new Error('absent');
      return r.text();
    });
  }

  /* Extraits Azure du cours d'un module, tels que le lecteur les demandera */
  function moduleItems(url, v) {
    return fetchText(url).then(function (html) {
      var doc = new DOMParser().parseFromString(html, 'text/html');
      var content = doc.querySelector('.module-content');
      if (!content) return [];
      // Même découpage en volets que progress.js sur la page du module
      if (content.querySelectorAll('h2').length >= 2 && typeof window.buildFolds === 'function') {
        window.buildFolds(content);
      }
      return trackQueue(buildTracks(content), v.module, v.moduleTone, 1)
        .filter(function (it) { return it.engine === 'azure'; });
    });
  }

  function podcastItems(url, v) {
    return fetch(url, { cache: 'no-cache' })
      .then(function (r) { if (!r.ok) throw new Error('absent'); return r.json(); })
      .then(function (data) {
        return podcastQueue((data && data.lignes) || [], v.podA, v.podB, v.podTone, 1)
          .filter(function (it) { return it.engine === 'azure'; });
      });
  }

  var offlinePanelWatch = false;

  function initAudioOfflinePanel() {
    var root = document.getElementById('audio-offline');
    if (!root) return;
    if (root.classList.contains('is-busy')) return;   // pas pendant un téléchargement

    // Voix ou ton changés plus haut : la liste est recalculée pour ces voix
    if (!offlinePanelWatch) {
      offlinePanelWatch = true;
      var timer = null;
      window.addEventListener('formahub-audio-prefs', function () {
        clearTimeout(timer);
        timer = setTimeout(initAudioOfflinePanel, 400);
      });
    }

    if (!('caches' in window) || !('DOMParser' in window)) {
      root.innerHTML = '<p class="tool-note">Ce navigateur ne permet pas d\'enregistrer les audios.</p>';
      return;
    }

    var formations = [];           // { slug, nom, modules: [url], podcasts: [url], plan: {course, pod} }
    var busy = false;
    var cancelled = false;
    var wakeLock = null;

    root.innerHTML =
      '<p class="tool-note dl-voices"></p>' +
      '<div class="tool-status dl-status" role="status" aria-live="polite"></div>' +
      '<div class="tool-progress dl-progress" hidden><span></span></div>' +
      '<div class="tool-actions">' +
      '  <button type="button" class="btn btn-primary btn-sm dl-all-pods" disabled>🎧 Tous les podcasts</button>' +
      '  <button type="button" class="btn btn-outline btn-sm dl-cancel" hidden>Arrêter</button>' +
      '  <button type="button" class="btn btn-ghost btn-sm dl-clear">Supprimer les audios</button>' +
      '</div>' +
      '<ul class="dl-list"></ul>' +
      '<p class="tool-note dl-help"></p>';

    var el = {
      voices: root.querySelector('.dl-voices'),
      status: root.querySelector('.dl-status'),
      progress: root.querySelector('.dl-progress'),
      fill: root.querySelector('.dl-progress > span'),
      allPods: root.querySelector('.dl-all-pods'),
      cancel: root.querySelector('.dl-cancel'),
      clear: root.querySelector('.dl-clear'),
      list: root.querySelector('.dl-list'),
      help: root.querySelector('.dl-help')
    };

    var v = currentVoices();
    var anyAzure = isAzureKey(v.module) || isAzureKey(v.podA) || isAzureKey(v.podB);

    el.voices.innerHTML = 'Voix enregistrées : cours — <strong>' + voiceLabel(v.module) + '</strong> · podcasts — <strong>' +
      voiceLabel(v.podA) + '</strong> &amp; <strong>' + voiceLabel(v.podB) + '</strong>. ' +
      'Changer de voix ou de ton plus haut demandera de retélécharger ; la vitesse, non.';

    el.help.innerHTML = 'Gardez cette page ouverte (écran allumé) pendant le téléchargement. Les voix du navigateur, elles, ' +
      'fonctionnent hors ligne sans rien télécharger. Palier gratuit Azure : ' + humanChars(AZURE_FREE_CHARS) +
      ' caractères par mois — la plateforme entière en compte bien plus, d\'où le choix formation par formation.';

    if (!Azure.enabled) {
      el.status.innerHTML = '<span class="dot dot-ko"></span> Les voix Azure ne répondent pas' +
        (Azure.error ? ' (' + Azure.error + ')' : ' (hors connexion ?)') +
        ' : téléchargement impossible pour l\'instant.' +
        (Azure.cachedOnly ? ' Les audios déjà téléchargés restent jouables.' : '');
      el.allPods.hidden = true;
    } else if (!anyAzure) {
      el.status.innerHTML = '<span class="dot dot-ok"></span> Vos voix sont des voix du navigateur : ' +
        'elles fonctionnent déjà hors ligne, rien à télécharger.';
      el.allPods.hidden = true;
    } else {
      el.status.innerHTML = '<span class="dot dot-run"></span> Calcul de la taille des audios…';
    }

    /* ---------- Liste des formations (depuis le catalogue de l'accueil) ---------- */

    Promise.all([
      fetchText(ROOT + 'index.html'),
      fetch(ROOT + 'offline-manifest.json', { cache: 'no-cache' }).then(function (r) { return r.json(); })
    ]).then(function (res) {
      var doc = new DOMParser().parseFromString(res[0], 'text/html');
      var urls = (res[1] && res[1].urls) || [];
      Array.prototype.forEach.call(doc.querySelectorAll('[data-formation-slug]'), function (card) {
        var slug = card.getAttribute('data-formation-slug');
        var h = card.querySelector('h2, h3');
        var prefix = 'formations/' + slug + '/';
        var mods = urls.filter(function (u) { return u.indexOf(prefix) === 0 && /\/module-\d+\/index\.html$/.test(u); });
        var pods = urls.filter(function (u) { return u.indexOf(prefix) === 0 && /\/podcast\.json$/.test(u); });
        var num = function (u) { return parseInt((u.match(/module-(\d+)/) || [0, 0])[1], 10); };
        mods.sort(function (a, b) { return num(a) - num(b); });
        pods.sort(function (a, b) { return num(a) - num(b); });
        formations.push({
          slug: slug,
          nom: h ? h.textContent.trim() : slug,
          modules: mods.map(function (u) { return ROOT + u; }),
          podcasts: pods.map(function (u) { return ROOT + u; }),
          plan: { course: null, pod: null }
        });
      });
      renderList();
      if (Azure.enabled && anyAzure) return planAll();
    }).catch(function () {
      el.status.innerHTML = '<span class="dot dot-ko"></span> Liste des formations indisponible (hors connexion ?).';
    });

    function renderList() {
      el.list.innerHTML = '';
      formations.forEach(function (f) {
        var li = document.createElement('li');
        li.className = 'dl-row';
        li.innerHTML =
          '<div class="dl-name"><strong></strong><span class="dl-sub"></span></div>' +
          '<div class="dl-btns">' +
          '  <button type="button" class="btn btn-outline btn-sm dl-course" disabled>🔊 Cours lus</button>' +
          '  <button type="button" class="btn btn-outline btn-sm dl-pod" disabled>🎧 Podcasts</button>' +
          '</div>';
        li.querySelector('strong').textContent = f.nom;
        li.querySelector('.dl-sub').textContent = f.modules.length + ' modules' +
          (f.podcasts.length ? ' · ' + f.podcasts.length + ' podcasts' : ' · pas de podcast');
        f.row = li;
        f.btnCourse = li.querySelector('.dl-course');
        f.btnPod = li.querySelector('.dl-pod');
        if (!f.podcasts.length) f.btnPod.hidden = true;
        f.btnCourse.addEventListener('click', function () { run([{ f: f, kind: 'course' }]); });
        f.btnPod.addEventListener('click', function () { run([{ f: f, kind: 'pod' }]); });
        el.list.appendChild(li);
      });
    }

    /* ---------- Taille et état de chaque lot ---------- */

    function planFor(f, kind) {
      if (f.plan[kind]) return Promise.resolve(f.plan[kind]);
      var urls = kind === 'course' ? f.modules : f.podcasts;
      var build = kind === 'course' ? moduleItems : podcastItems;
      var items = [];
      var chain = Promise.resolve();
      urls.forEach(function (u) {
        chain = chain.then(function () {
          return build(u, v).then(function (list) { items = items.concat(list); }).catch(function () { /* module illisible */ });
        });
      });
      return chain.then(function () {
        // Un même extrait (titre répété…) ne se télécharge qu'une fois
        var seen = {};
        var unique = [];
        items.forEach(function (it) {
          var k = clipKey(it);
          if (seen[k]) return;
          seen[k] = 1;
          it.key = k;
          unique.push(it);
        });
        var chars = unique.reduce(function (n, it) { return n + it.text.length; }, 0);
        return Promise.all(unique.map(function (it) { return dlHas(it.key); })).then(function (flags) {
          var have = flags.filter(Boolean).length;
          f.plan[kind] = { items: unique, chars: chars, have: have };
          return f.plan[kind];
        });
      });
    }

    function paintButton(f, kind) {
      var p = f.plan[kind];
      var btn = kind === 'course' ? f.btnCourse : f.btnPod;
      var label = kind === 'course' ? '🔊 Cours lus' : '🎧 Podcasts';
      if (!p) return;
      var voiceOk = kind === 'course' ? isAzureKey(v.module) : (isAzureKey(v.podA) || isAzureKey(v.podB));
      if (!voiceOk || !p.items.length) {
        btn.textContent = label + ' · voix du navigateur';
        btn.disabled = true;
        btn.title = 'Voix du navigateur : fonctionne hors ligne sans téléchargement';
        return;
      }
      var left = p.items.length - p.have;
      if (!left) {
        btn.textContent = label + ' ✓ hors ligne';
        btn.disabled = true;
        btn.classList.add('is-done');
        btn.title = humanMo(p.chars * BYTES_PER_CHAR) + ' enregistrés sur cet appareil';
        return;
      }
      var leftChars = p.chars * left / p.items.length;
      btn.classList.remove('is-done');
      btn.textContent = label + ' · ' + humanMo(leftChars * BYTES_PER_CHAR) + (p.have ? ' restants' : '');
      btn.title = '≈ ' + humanChars(Math.round(leftChars)) + ' caractères Azure — ' + p.have + '/' + p.items.length + ' extraits déjà enregistrés';
      btn.disabled = busy;
    }

    function planAll() {
      var chain = Promise.resolve();
      formations.forEach(function (f) {
        chain = chain.then(function () {
          return planFor(f, 'course').then(function () { paintButton(f, 'course'); })
            .then(function () { return f.podcasts.length ? planFor(f, 'pod') : null; })
            .then(function () { if (f.podcasts.length) paintButton(f, 'pod'); });
        });
      });
      return chain.then(function () { paintSummary(); });
    }

    function paintSummary() {
      if (busy) return;
      var podLeft = 0, podChars = 0, done = 0, total = 0;
      formations.forEach(function (f) {
        ['course', 'pod'].forEach(function (k) {
          var p = f.plan[k];
          if (!p || !p.items.length) return;
          total += p.items.length;
          done += p.have;
          if (k === 'pod') {
            podLeft += p.items.length - p.have;
            podChars += p.chars * (p.items.length - p.have) / p.items.length;
          }
        });
      });
      el.allPods.disabled = !podLeft;
      el.allPods.textContent = podLeft
        ? '🎧 Tous les podcasts · ' + humanMo(podChars * BYTES_PER_CHAR)
        : '🎧 Tous les podcasts ✓';
      el.status.innerHTML = done
        ? '<span class="dot dot-ok"></span> ' + done + ' extraits audio enregistrés sur cet appareil.'
        : '<span class="dot"></span> Aucun audio téléchargé pour l\'instant — choisissez une formation.';
    }

    el.allPods.addEventListener('click', function () {
      run(formations.filter(function (f) { return f.podcasts.length; })
        .map(function (f) { return { f: f, kind: 'pod' }; }));
    });

    /* ---------- Téléchargement ---------- */

    function lockScreen() {
      try {
        if (navigator.wakeLock && navigator.wakeLock.request) {
          navigator.wakeLock.request('screen').then(function (l) { wakeLock = l; }).catch(function () { /* ignore */ });
        }
      } catch (e) { /* ignore */ }
    }

    function unlockScreen() {
      try { if (wakeLock) wakeLock.release(); } catch (e) { /* ignore */ }
      wakeLock = null;
    }

    // L'écran s'est rallumé pendant un téléchargement : on reprend le verrou
    document.addEventListener('visibilitychange', function () {
      if (busy && document.visibilityState === 'visible') { wakeLock = null; lockScreen(); }
    });

    function setBusy(on) {
      busy = on;
      root.classList.toggle('is-busy', on);
      el.cancel.hidden = !on;
      el.clear.disabled = on;
      el.allPods.disabled = on;
      el.progress.hidden = !on;
      formations.forEach(function (f) {
        if (on) {
          f.btnCourse.disabled = true;
          f.btnPod.disabled = true;
        } else {
          paintButton(f, 'course');
          paintButton(f, 'pod');
        }
      });
    }

    function getOne(it, tries) {
      tries = tries || 0;
      return fetchClip(it, 0, true).catch(function (err) {
        var msg = (err && err.message) || '';
        if (cancelled) throw err;
        // Quota par minute : on patiente puis on reprend
        if (/quota|429|trop de requ/i.test(msg) && tries < 6) {
          el.status.innerHTML = '<span class="dot dot-run"></span> Azure demande une pause (quota par minute) — reprise dans 30 s…';
          return wait(30000).then(function () { return getOne(it, tries + 1); });
        }
        if (!navigator.onLine) throw new Error('connexion perdue');
        if (tries < 2) return wait(3000).then(function () { return getOne(it, tries + 1); });
        throw err;
      });
    }

    function run(jobs) {
      if (busy || !jobs.length) return;
      cancelled = false;
      setBusy(true);
      lockScreen();
      if (window.formahubOffline && window.formahubOffline.persist) window.formahubOffline.persist();
      el.fill.style.width = '2%';
      el.status.innerHTML = '<span class="dot dot-run"></span> Préparation…';

      var queue = [];
      var failed = 0;
      var lastError = '';

      var prep = Promise.resolve();
      jobs.forEach(function (j) {
        prep = prep.then(function () {
          return planFor(j.f, j.kind).then(function (p) {
            p.items.forEach(function (it) { queue.push({ it: it, job: j }); });
          });
        });
      });

      prep.then(function () {
        var total = queue.length;
        var done = 0;
        var i = 0;

        function paint() {
          el.fill.style.width = Math.max(2, Math.round(done / Math.max(1, total) * 100)) + '%';
          el.status.innerHTML = '<span class="dot dot-run"></span> ' + done + ' / ' + total + ' extraits' +
            (failed ? ' · ' + failed + ' en échec' : '') + ' — gardez la page ouverte';
        }
        paint();

        function worker() {
          if (cancelled || i >= queue.length) return Promise.resolve();
          var q = queue[i++];
          return dlHas(q.it.key).then(function (has) {
            if (has) return null;
            return getOne(q.it).then(function () { q.job.f.plan[q.job.kind].have += 1; });
          }).catch(function (err) {
            failed += 1;
            lastError = (err && err.message) || 'erreur';
            if (lastError === 'connexion perdue') cancelled = true;
          }).then(function () {
            done += 1;
            paint();
            if (done % 10 === 0) jobs.forEach(function (j) { paintButton(j.f, j.kind); });
            return worker();
          });
        }
        // Deux requêtes à la fois : le palier gratuit d'Azure limite le débit
        return Promise.all([worker(), worker()]).then(function () {
          return { total: total, done: done };
        });
      }).then(function (r) {
        unlockScreen();
        setBusy(false);
        // Recompte exact de ce qui est enregistré
        jobs.forEach(function (j) { j.f.plan[j.kind] = null; });
        var chain = Promise.resolve();
        jobs.forEach(function (j) {
          chain = chain.then(function () { return planFor(j.f, j.kind).then(function () { paintButton(j.f, j.kind); }); });
        });
        return chain.then(function () {
          paintSummary();
          var msg;
          if (cancelled && lastError === 'connexion perdue') msg = '⚠️ Connexion perdue — relancez pour reprendre là où ça s\'est arrêté.';
          else if (cancelled) msg = '⏸ Téléchargement arrêté — ce qui est déjà enregistré est conservé.';
          else if (failed) msg = '⚠️ ' + failed + ' extraits en échec (' + lastError + ') — relancez pour les compléter.';
          else msg = '📦 Audios enregistrés : écoute possible hors ligne.';
          if (cancelled || failed) el.status.innerHTML = '<span class="dot dot-ko"></span> ' + msg.replace(/^\S+\s/, '');
          if (typeof window.formahubToast === 'function') window.formahubToast(msg);
        });
      }).catch(function (err) {
        unlockScreen();
        setBusy(false);
        el.status.innerHTML = '<span class="dot dot-ko"></span> Téléchargement interrompu (' +
          ((err && err.message) || 'erreur') + ').';
      });
    }

    el.cancel.addEventListener('click', function () {
      cancelled = true;
      el.cancel.disabled = true;
      setTimeout(function () { el.cancel.disabled = false; }, 1500);
    });

    /* Suppression en deux temps (pas de boîte de dialogue du navigateur) */
    var clearArmed = null;
    el.clear.addEventListener('click', function () {
      if (!clearArmed) {
        el.clear.textContent = 'Confirmer la suppression';
        el.clear.classList.add('is-armed');
        clearArmed = setTimeout(function () {
          clearArmed = null;
          el.clear.textContent = 'Supprimer les audios';
          el.clear.classList.remove('is-armed');
        }, 4000);
        return;
      }
      clearTimeout(clearArmed);
      clearArmed = null;
      el.clear.textContent = 'Supprimer les audios';
      el.clear.classList.remove('is-armed');
      Promise.all([caches.delete(TTS_DL_CACHE), caches.delete(TTS_CACHE)]).then(function () {
        formations.forEach(function (f) {
          ['course', 'pod'].forEach(function (k) {
            if (f.plan[k]) f.plan[k].have = 0;
            var btn = k === 'course' ? f.btnCourse : f.btnPod;
            btn.classList.remove('is-done');
            paintButton(f, k);
          });
        });
        paintSummary();
        if (typeof window.formahubToast === 'function') window.formahubToast('🧹 Audios supprimés de cet appareil.');
      });
    });
  }

  /* ============================================================
     8. Amorçage
     ============================================================ */

  function boot() {
    var hasModule = !!document.querySelector('.module-content');
    var hasSettings = !!document.getElementById('audio-settings-panel');
    var hasOffline = !!document.getElementById('audio-offline');
    if (!hasModule && !hasSettings && !hasOffline) return;

    var pending = 2;
    function ready() {
      pending -= 1;
      if (pending) return;
      if (hasModule) {
        var player = initModulePlayer();
        initPodcastPlayer(player);
        // Le lecteur de module coupe le podcast, et inversement
        var bar = document.querySelector('.audio-bar .audio-play');
        if (bar) {
          bar.addEventListener('click', function () {
            var podStop = document.querySelector('.pod-stop');
            if (podStop && !podStop.hidden) podStop.click();
          }, true);
        }
      }
      if (hasSettings) initAudioSettingsPanel();
      if (hasOffline) initAudioOfflinePanel();
    }
    whenVoicesReady(ready);
    azureInit().then(ready);
  }

  /* progress.js restructure le module au DOMContentLoaded ; comme il est
     chargé avant nous, son écouteur passe en premier et les volets existent
     déjà quand celui-ci se déclenche. */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    setTimeout(boot, 0);
  }
})();
