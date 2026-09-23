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

  var Azure = { enabled: false, voices: [], error: null };

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
        return Azure;
      })
      .catch(function () { return Azure; })
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
    return caches.open(TTS_CACHE)
      .then(function (c) { return c.match(key); })
      .then(function (r) { return r ? r.blob() : null; })
      .catch(function () { return null; });
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

  function fetchClip(item, attempt) {
    attempt = attempt || 0;
    var body = azureBody(item);
    var payload = JSON.stringify(body);
    var key = ROOT + '__tts-cache/' + hashString(payload);
    return cacheGet(key).then(function (blob) {
      if (blob) return blob;
      return fetch(TTS_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: payload
      }).then(function (r) {
        if (r.status === 429 && attempt < 4) {
          var after = parseInt(r.headers.get('Retry-After'), 10);
          return wait((after > 0 ? after : 2 * (attempt + 1)) * 1000)
            .then(function () { return fetchClip(item, attempt + 1); });
        }
        if (!r.ok) {
          return r.json().catch(function () { return {}; }).then(function (d) {
            throw new Error(d.error || ('erreur ' + r.status));
          });
        }
        return r.blob().then(function (b) {
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
  function anyVoice() { return Azure.enabled || webAvailable(); }

  /* Clés de voix : « az:<ShortName> » ou « web:<nom système> » */
  function isAzureKey(k) { return typeof k === 'string' && k.indexOf('az:') === 0; }
  function keyName(k) { return String(k || '').replace(/^(az|web):/, ''); }

  function validVoiceKey(k) {
    if (!k) return false;
    if (isAzureKey(k)) return Azure.enabled && !!azureVoice(keyName(k));
    return webAvailable() && !!voiceByName(keyName(k));
  }

  function defaultVoiceKey(gender) {
    if (Azure.enabled) {
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
    if (Azure.enabled) {
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
      w.label = 'Voix du navigateur' + (Azure.enabled ? ' (hors ligne)' : '');
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
  function buildTracks() {
    var content = document.querySelector('.module-content');
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

  function buildControls(bar, opts) {
    bar.innerHTML =
      '<div class="audio-row">' +
      '  <button type="button" class="btn btn-primary btn-sm audio-play" aria-label="Lire ou mettre en pause">▶ ' + opts.label + '</button>' +
      '  <button type="button" class="btn btn-ghost btn-sm audio-prev" title="Section précédente" aria-label="Section précédente" hidden>⏮</button>' +
      '  <button type="button" class="btn btn-ghost btn-sm audio-next" title="Section suivante" aria-label="Section suivante" hidden>⏭</button>' +
      '  <button type="button" class="btn btn-ghost btn-sm audio-stop" title="Arrêter" aria-label="Arrêter la lecture" hidden>⏹</button>' +
      '  <span class="audio-status" role="status" aria-live="polite"></span>' +
      '</div>' +
      '<div class="audio-row audio-settings">' +
      '  <label class="audio-field audio-voice-field"><span>Voix</span>' +
      '    <select class="audio-voice" aria-label="Voix de lecture"></select></label>' +
      '  <label class="audio-field"><span>Ton</span>' +
      '    <select class="audio-tone" aria-label="Ton de la voix"></select></label>' +
      '  <label class="audio-field"><span>Vitesse</span>' +
      '    <select class="audio-rate" aria-label="Vitesse de lecture">' + rateOptions() + '</select></label>' +
      '  <span class="audio-engine" aria-hidden="true"></span>' +
      '</div>' +
      '<div class="audio-progress" aria-hidden="true"><span></span></div>';

    var ui = {
      play: bar.querySelector('.audio-play'),
      prev: bar.querySelector('.audio-prev'),
      next: bar.querySelector('.audio-next'),
      stop: bar.querySelector('.audio-stop'),
      status: bar.querySelector('.audio-status'),
      rate: bar.querySelector('.audio-rate'),
      voice: bar.querySelector('.audio-voice'),
      tone: bar.querySelector('.audio-tone'),
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

  /* Un vrai fichier audio (export NotebookLM, ou tout autre enregistrement)
     posé à côté de podcast.json prend le pas sur la voix de synthèse.
     On essaie ces noms dans l'ordre ; le premier qui existe est utilisé. */
  var PODCAST_AUDIO_CANDIDATES = ['podcast-audio.mp3', 'podcast-audio.m4a', 'podcast-audio.wav'];

  function probeAudioFile(list, i) {
    i = i || 0;
    if (i >= list.length) return Promise.resolve(null);
    return fetch(list[i], { method: 'HEAD', cache: 'no-cache' })
      .then(function (r) { return (r && r.ok) ? list[i] : probeAudioFile(list, i + 1); })
      .catch(function () { return probeAudioFile(list, i + 1); });
  }

  function podcastVoiceKeys() {
    var a = validVoiceKey(prefs.podVoiceA) ? prefs.podVoiceA : null;
    var b = validVoiceKey(prefs.podVoiceB) ? prefs.podVoiceB : null;
    if (!a) a = defaultVoiceKey('Female');
    if (!b) {
      if (Azure.enabled) b = defaultVoiceKey('Male');
      else {
        var fr = frenchVoices();
        var other = fr.filter(function (v) { return 'web:' + v.name !== a; })[0];
        b = other ? 'web:' + other.name : a;
      }
    }
    return { a: a, b: b };
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
      .then(function (data) {
        probeAudioFile(PODCAST_AUDIO_CANDIDATES).then(function (audioUrl) {
          render(data, audioUrl);
        });
      })
      .catch(function () {
        meta.textContent = 'à venir';
        box.classList.add('is-empty');
        body.innerHTML = '<p class="podcast-empty">Le podcast de ce module n\'est pas encore écrit. ' +
          'Le lecteur apparaîtra ici dès que <code>podcast.json</code> sera présent dans le dossier du module.</p>';
      });

    /* Construit systématiquement le script (texte des répliques) : il sert
       de transcription dans les deux cas, fichier audio réel ou synthèse. */
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

    /* Fichier audio réel (ex. export NotebookLM) : lecteur natif du
       navigateur + vitesse jusqu'à 2× + transcription en dessous. */
    function renderRealAudio(data, audioUrl, nomA, nomB) {
      var wrap = document.createElement('div');
      wrap.className = 'podcast-player podcast-player-real';
      var audioEl = document.createElement('audio');
      audioEl.className = 'pod-audio';
      audioEl.controls = true;
      audioEl.preload = 'none';
      audioEl.src = audioUrl;
      audioEl.preservesPitch = true;
      wrap.appendChild(audioEl);

      var row = document.createElement('div');
      row.className = 'audio-row';
      row.innerHTML = '<span class="audio-spacer"></span><label class="audio-field"><span>Vitesse</span>' +
        '<select class="pod-rate" aria-label="Vitesse du podcast">' + rateOptions() + '</select></label>';
      wrap.appendChild(row);
      var rate = row.querySelector('.pod-rate');
      rate.value = String(nearestRate(prefs.podcastRate || 1));
      function applyRate() { audioEl.playbackRate = parseFloat(rate.value) || 1; }
      applyRate();
      audioEl.addEventListener('loadedmetadata', applyRate);
      rate.addEventListener('change', function () {
        prefs.podcastRate = parseFloat(rate.value) || 1;
        savePrefs();
        applyRate();
      });

      audioEl.addEventListener('play', function () {
        if (otherPlayer && otherPlayer.isActive && otherPlayer.isActive()) otherPlayer.stop();
        engineStop();
      });

      body.innerHTML = '';
      body.appendChild(wrap);
      body.appendChild(buildScript(data, nomA, nomB));
    }

    function render(data, audioUrl) {
      var lignes = (data && data.lignes) || [];
      if (!lignes.length) { meta.textContent = 'à venir'; return; }

      var hosts = (data && data.hosts) || {};
      var nomA = (hosts.a && hosts.a.nom) || 'Animatrice';
      var nomB = (hosts.b && hosts.b.nom) || 'Expert';
      meta.textContent = (data.duree_estimee || '') + (data.duree_estimee ? ' · ' : '') +
        nomA + ' & ' + nomB + (audioUrl ? ' · 🎙️ audio réel' : (Azure.enabled ? ' · voix Azure' : ''));

      if (audioUrl) {
        renderRealAudio(data, audioUrl, nomA, nomB);
        return;
      }

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
        '</div>' +
        '<div class="audio-row audio-settings">' +
        '  <label class="audio-field audio-voice-field"><span></span><select class="pod-voice-a"></select></label>' +
        '  <label class="audio-field audio-voice-field"><span></span><select class="pod-voice-b"></select></label>' +
        '  <label class="audio-field"><span>Ton</span><select class="pod-tone" aria-label="Ton du podcast"></select></label>' +
        '  <label class="audio-field"><span>Vitesse</span>' +
        '    <select class="pod-rate" aria-label="Vitesse du podcast">' + rateOptions() + '</select></label>' +
        '</div>' +
        '<div class="audio-progress" aria-hidden="true"><span></span></div>';

      body.innerHTML = '';
      body.appendChild(wrap);
      body.appendChild(script);

      var ui = {
        play: wrap.querySelector('.pod-play'),
        stop: wrap.querySelector('.pod-stop'),
        status: wrap.querySelector('.pod-status'),
        rate: wrap.querySelector('.pod-rate'),
        voiceA: wrap.querySelector('.pod-voice-a'),
        voiceB: wrap.querySelector('.pod-voice-b'),
        tone: wrap.querySelector('.pod-tone'),
        progress: wrap.querySelector('.audio-progress span')
      };
      var labels = wrap.querySelectorAll('.audio-voice-field > span');
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
        var rate = parseFloat(ui.rate.value) || 1;
        var ka = ui.voiceA.value, kb = ui.voiceB.value;
        var same = ka === kb && !isAzureKey(ka);
        var q = [];
        lignes.forEach(function (l, i) {
          var isB = l.v === 'b';
          var key = isB ? kb : ka;
          // Une seule voix système pour deux personnes : on les distingue par la hauteur
          var pitch = same ? (isB ? 0.85 : 1.12) : 1;
          var limit = isAzureKey(key) ? AZ_CHUNK : 210;
          chunkText(isAzureKey(key) ? speakable(l.t) : l.t, limit).forEach(function (c) {
            q.push(makeItem(c, key, ui.tone.value, rate, { line: i }, pitch));
          });
        });
        return q;
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
     7. Amorçage
     ============================================================ */

  function boot() {
    if (!document.querySelector('.module-content')) return;
    var pending = 2;
    function ready() {
      pending -= 1;
      if (pending) return;
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
