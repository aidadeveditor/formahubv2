/* ============================================================
   Formahub — écoute audio des modules et podcasts (V7)
   Synthèse vocale du navigateur (Web Speech API), sans dépendance
   ni fichier son à héberger : tout fonctionne hors ligne dès que
   les voix françaises du système sont installées.

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

  /* ============================================================
     1. Le moteur de parole
     ============================================================ */

  var Engine = {
    voices: [],
    ready: false,
    queue: [],          // { text, voice, rate, pitch, meta }
    index: 0,
    playing: false,
    paused: false,
    current: null,
    onProgress: null,   // (meta, indexDansLaQueue) -> void
    onDone: null,
    watchdog: null,
    keepAlive: null
  };

  function loadVoices() {
    var list = [];
    try { list = window.speechSynthesis.getVoices() || []; } catch (e) { list = []; }
    Engine.voices = list;
    Engine.ready = list.length > 0;
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

  /* Découpe un texte en fragments courts.
     Chrome interrompt une énonciation qui dépasse ~15 secondes : on
     découpe donc aux frontières de phrases, sans dépasser ~210 caractères. */
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
      .replace(/ /g, ' ')
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

  function engineStop() {
    clearTimers();
    Engine.queue = [];
    Engine.index = 0;
    Engine.playing = false;
    Engine.paused = false;
    Engine.current = null;
    try { window.speechSynthesis.cancel(); } catch (e) { /* ignore */ }
  }

  function engineStart(queue, handlers, startIndex) {
    engineStop();
    Engine.queue = queue;
    Engine.index = Math.max(0, Math.min(startIndex || 0, queue.length - 1));
    Engine.playing = true;
    Engine.paused = false;
    Engine.onProgress = handlers.onProgress || null;
    Engine.onDone = handlers.onDone || null;
    // Chrome garde parfois une file fantôme après un cancel()
    setTimeout(speakCurrent, 60);
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

    var u = new SpeechSynthesisUtterance(item.text);
    u.lang = (item.voice && item.voice.lang) || 'fr-FR';
    if (item.voice) u.voice = item.voice;
    u.rate = item.rate || 1;
    u.pitch = item.pitch || 1;
    u.volume = 1;

    var advanced = false;
    function advance() {
      if (advanced) return;
      advanced = true;
      clearTimers();
      Engine.index += 1;
      speakCurrent();
    }

    u.onend = advance;
    u.onerror = function (e) {
      // « interrupted » et « canceled » viennent de nos propres arrêts : on ne relance pas
      if (e && (e.error === 'interrupted' || e.error === 'canceled')) { advanced = true; return; }
      advance();
    };

    Engine.current = u;
    try { window.speechSynthesis.speak(u); } catch (e) { advance(); return; }

    /* Filet de sécurité : si onend ne se déclenche jamais (bug connu de
       Chrome et de quelques WebView), on avance au bout d'une durée
       largement supérieure au temps de lecture attendu. */
    var expected = (item.text.length / 12) * 1000 / (u.rate || 1);
    clearTimers();
    Engine.watchdog = setTimeout(function () {
      if (!Engine.paused) advance();
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

  function enginePause() {
    if (!Engine.playing || Engine.paused) return;
    Engine.paused = true;
    clearTimers();
    try { window.speechSynthesis.pause(); } catch (e) { /* ignore */ }
  }

  function engineResume() {
    if (!Engine.playing || !Engine.paused) return;
    Engine.paused = false;
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
    try { window.speechSynthesis.cancel(); } catch (e) { /* ignore */ }
    setTimeout(speakCurrent, 80);
  }

  // Un onglet qu'on quitte ne doit pas continuer à parler dans le vide
  window.addEventListener('pagehide', engineStop);
  window.addEventListener('beforeunload', engineStop);

  /* ============================================================
     2. Extraction du texte lisible d'un module
     ============================================================ */

  var SKIP = 'script, style, .fold-next, .fold-toolbar, .quiz-section, .module-nav, .audio-bar, .podcast-box, .read-progress, .toast, .to-top';

  function readableNodes(root) {
    var nodes = [];
    var walker = root.querySelectorAll('p, li, dt, dd, h3, h4, h2, th, td, summary');
    Array.prototype.forEach.call(walker, function (el) {
      if (el.closest(SKIP)) return;
      if (el.closest('.solution-box') && el.tagName === 'SUMMARY') return;
      // Un <li> qui ne contient que d'autres blocs n'apporte rien
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

  function trackQueue(tracks, voice, rate) {
    var queue = [];
    tracks.forEach(function (track, ti) {
      chunkText(track.titre, 210).forEach(function (c) {
        queue.push({
          text: speakable(c), voice: voice, rate: rate, pitch: 1,
          meta: { track: ti, el: null, titre: track.titre, heading: true }
        });
      });
      track.nodes.forEach(function (node) {
        chunkText(node.text, 210).forEach(function (c) {
          queue.push({
            text: speakable(c), voice: voice, rate: rate, pitch: 1,
            meta: { track: ti, el: node.el, titre: track.titre, heading: false }
          });
        });
      });
    });
    return queue;
  }

  /* ============================================================
     3. Le lecteur « Écouter le module »
     ============================================================ */

  function moduleId() {
    var btn = document.getElementById('btn-mark-complete');
    return (btn && btn.dataset.moduleId) || location.pathname;
  }

  function buildControls(bar, opts) {
    var voices = frenchVoices();
    var html =
      '<div class="audio-row">' +
      '  <button type="button" class="btn btn-primary btn-sm audio-play" aria-label="Lire ou mettre en pause">▶ ' + opts.label + '</button>' +
      '  <button type="button" class="btn btn-ghost btn-sm audio-prev" title="Section précédente" aria-label="Section précédente" hidden>⏮</button>' +
      '  <button type="button" class="btn btn-ghost btn-sm audio-next" title="Section suivante" aria-label="Section suivante" hidden>⏭</button>' +
      '  <button type="button" class="btn btn-ghost btn-sm audio-stop" title="Arrêter" aria-label="Arrêter la lecture" hidden>⏹</button>' +
      '  <span class="audio-status" role="status" aria-live="polite"></span>' +
      '  <span class="audio-spacer"></span>' +
      '  <label class="audio-field"><span>Vitesse</span>' +
      '    <select class="audio-rate" aria-label="Vitesse de lecture">' +
      '      <option value="0.8">0,8×</option><option value="0.9">0,9×</option>' +
      '      <option value="1">1×</option><option value="1.1">1,1×</option>' +
      '      <option value="1.25">1,25×</option><option value="1.5">1,5×</option>' +
      '    </select></label>' +
      '  <label class="audio-field audio-voice-field"><span>Voix</span>' +
      '    <select class="audio-voice" aria-label="Voix de lecture"></select></label>' +
      '</div>' +
      '<div class="audio-progress" aria-hidden="true"><span></span></div>';
    bar.innerHTML = html;

    var select = bar.querySelector('.audio-voice');
    voices.forEach(function (v) {
      var o = document.createElement('option');
      o.value = v.name;
      o.textContent = v.name.replace(/^Microsoft\s+/, '').replace(/\s*-\s*French.*$/i, '') +
        (v.localService ? '' : ' (en ligne)');
      select.appendChild(o);
    });
    if (!voices.length) {
      var o = document.createElement('option');
      o.textContent = 'Voix par défaut';
      select.appendChild(o);
      select.disabled = true;
    }
    if (prefs.voice && voiceByName(prefs.voice)) select.value = prefs.voice;

    var rate = bar.querySelector('.audio-rate');
    rate.value = String(prefs.rate || 1);

    return {
      play: bar.querySelector('.audio-play'),
      prev: bar.querySelector('.audio-prev'),
      next: bar.querySelector('.audio-next'),
      stop: bar.querySelector('.audio-stop'),
      status: bar.querySelector('.audio-status'),
      rate: rate,
      voice: select,
      progress: bar.querySelector('.audio-progress span')
    };
  }

  function initModulePlayer() {
    var header = document.querySelector('.module-header');
    var content = document.querySelector('.module-content');
    if (!header || !content) return null;

    var bar = document.createElement('section');
    bar.className = 'audio-bar';
    bar.setAttribute('aria-label', 'Écoute du module');
    header.parentNode.insertBefore(bar, header.nextSibling);

    if (!SUPPORTED) {
      bar.innerHTML = '<p class="audio-unsupported">🔇 Ce navigateur ne propose pas de synthèse vocale — ' +
        'l\'écoute du module n\'est pas disponible ici. Elle fonctionne sur Chrome, Edge, Safari et Firefox à jour.</p>';
      return null;
    }

    var ui = buildControls(bar, { label: 'Écouter le module' });
    var tracks = buildTracks();
    if (!tracks.length) { bar.remove(); return null; }

    if (!Engine.voices.length) {
      ui.play.disabled = true;
      ui.status.textContent = 'Aucune voix installée sur cet appareil.';
      var aide = document.createElement('p');
      aide.className = 'audio-unsupported';
      aide.innerHTML = 'La lecture utilise les voix du système. Sous Windows, ajoutez une voix ' +
        'française dans <em>Paramètres → Heure et langue → Voix</em>, puis rechargez la page. ' +
        'Sur Android et iOS, elles sont installées d\'origine.';
      bar.appendChild(aide);
      return null;
    }

    var state = { active: false, queue: [], track: -1, el: null };
    var resumeStore = readStore(POS_KEY, {}) || {};
    var savedIndex = resumeStore[moduleId()];

    function currentVoice() { return voiceByName(ui.voice.value); }
    function currentRate() { return parseFloat(ui.rate.value) || 1; }

    function paint(meta, index, total) {
      if (typeof index === 'number' && total) {
        ui.progress.style.width = Math.round(((index + 1) / total) * 100) + '%';
        resumeStore[moduleId()] = index;
        writeStore(POS_KEY, resumeStore);
      }
      if (!meta) return;

      if (state.el && state.el !== meta.el) state.el.classList.remove('is-speaking');
      state.el = meta.el;
      if (meta.el) {
        meta.el.classList.add('is-speaking');
        var rect = meta.el.getBoundingClientRect();
        if (rect.top < 90 || rect.bottom > window.innerHeight - 60) {
          meta.el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }

      if (meta.track !== state.track) {
        // Le volet qu'on quitte se referme : la page reste lisible pendant l'écoute
        var previous = tracks[state.track];
        if (previous && previous.fold && meta.track > state.track) previous.fold.open = false;
        state.track = meta.track;
        var track = tracks[meta.track];
        if (track && track.fold) {
          track.fold.open = true;
          if (typeof window.markRead === 'function') window.markRead(track.fold);
        }
      }
      ui.status.textContent = 'Section ' + (meta.track + 1) + '/' + tracks.length + ' — ' + meta.titre;
    }

    function clearHighlight() {
      if (state.el) state.el.classList.remove('is-speaking');
      state.el = null;
    }

    function start(fromIndex) {
      state.queue = trackQueue(tracks, currentVoice(), currentRate());
      state.startedAt = Date.now();
      state.active = true;
      state.track = -1;
      bar.classList.add('is-playing');
      ui.play.textContent = '⏸ Pause';
      [ui.prev, ui.next, ui.stop].forEach(function (b) { b.hidden = false; });
      engineStart(state.queue, {
        onProgress: paint,
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
      for (var i = 0; i < Engine.queue.length; i++) {
        if (Engine.queue[i].meta.track === target) return i;
      }
      return 0;
    }

    ui.play.addEventListener('click', function () {
      if (!state.active) {
        if (savedIndex && savedIndex > 2) {
          start(savedIndex);
          savedIndex = null;
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

    function restartWhereWeAre() {
      if (!state.active) return;
      var at = Engine.index;
      start(at);
    }

    ui.rate.addEventListener('change', function () {
      prefs.rate = currentRate();
      savePrefs();
      restartWhereWeAre();
    });

    ui.voice.addEventListener('change', function () {
      prefs.voice = ui.voice.value;
      savePrefs();
      restartWhereWeAre();
    });

    if (savedIndex && savedIndex > 2) {
      ui.status.textContent = '⏱ Reprise possible où vous vous étiez arrêtée.';
    } else {
      ui.status.textContent = tracks.length + ' sections à écouter.';
    }

    return { stop: stop, isActive: function () { return state.active; } };
  }

  /* ============================================================
     4. Le lecteur de podcast
     ============================================================ */

  function pickTwoVoices() {
    var fr = frenchVoices();
    var a = voiceByName(prefs.podcastVoiceA) || fr[0] || null;
    var b = voiceByName(prefs.podcastVoiceB) ||
      (fr.filter(function (v) { return v !== a; })[0]) || a;
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
      .then(function (data) { render(data); })
      .catch(function () {
        meta.textContent = 'à venir';
        box.classList.add('is-empty');
        body.innerHTML = '<p class="podcast-empty">Le podcast de ce module n\'est pas encore écrit. ' +
          'Le lecteur apparaîtra ici dès que <code>podcast.json</code> sera présent dans le dossier du module.</p>';
      });

    function render(data) {
      var lignes = (data && data.lignes) || [];
      if (!lignes.length) { meta.textContent = 'à venir'; return; }

      var hosts = (data && data.hosts) || {};
      var nomA = (hosts.a && hosts.a.nom) || 'Animatrice';
      var nomB = (hosts.b && hosts.b.nom) || 'Expert';
      meta.textContent = (data.duree_estimee || '') + (data.duree_estimee ? ' · ' : '') +
        nomA + ' & ' + nomB;

      if (!SUPPORTED) {
        body.innerHTML = '<p class="podcast-empty">Ce navigateur ne propose pas de synthèse vocale : ' +
          'le texte du podcast reste lisible ci-dessous.</p>';
      }

      var wrap = document.createElement('div');
      wrap.className = 'podcast-player';
      wrap.innerHTML =
        '<div class="audio-row">' +
        '  <button type="button" class="btn btn-primary btn-sm pod-play">▶ Écouter le podcast</button>' +
        '  <button type="button" class="btn btn-ghost btn-sm pod-stop" hidden aria-label="Arrêter le podcast">⏹</button>' +
        '  <span class="audio-status pod-status" role="status" aria-live="polite"></span>' +
        '  <span class="audio-spacer"></span>' +
        '  <label class="audio-field"><span>Vitesse</span>' +
        '    <select class="pod-rate" aria-label="Vitesse du podcast">' +
        '      <option value="0.9">0,9×</option><option value="1">1×</option>' +
        '      <option value="1.1">1,1×</option><option value="1.25">1,25×</option>' +
        '    </select></label>' +
        '</div>' +
        '<div class="audio-progress" aria-hidden="true"><span></span></div>';

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

      body.innerHTML = '';
      body.appendChild(wrap);
      body.appendChild(script);

      if (!SUPPORTED) { wrap.remove(); return; }

      if (!Engine.voices.length) {
        wrap.querySelector('.pod-play').disabled = true;
        wrap.querySelector('.pod-status').textContent =
          'Aucune voix installée : le texte reste lisible ci-dessous.';
      }

      var ui = {
        play: wrap.querySelector('.pod-play'),
        stop: wrap.querySelector('.pod-stop'),
        status: wrap.querySelector('.pod-status'),
        rate: wrap.querySelector('.pod-rate'),
        progress: wrap.querySelector('.audio-progress span')
      };
      ui.rate.value = String(prefs.podcastRate || 1);

      var active = false;
      var startedAt = 0;
      var currentLine = null;

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

      function buildQueue() {
        var v = pickTwoVoices();
        var rate = parseFloat(ui.rate.value) || 1;
        var queue = [];
        lignes.forEach(function (l, i) {
          var isB = l.v === 'b';
          var voice = isB ? v.b : v.a;
          // Si une seule voix française est installée, on distingue par la hauteur
          var pitch = (v.a === v.b) ? (isB ? 0.85 : 1.12) : 1;
          chunkText(l.t, 210).forEach(function (c) {
            queue.push({
              text: speakable(c), voice: voice, rate: rate, pitch: pitch,
              meta: { line: i }
            });
          });
        });
        return queue;
      }

      function start(fromIndex) {
        if (otherPlayer && otherPlayer.isActive && otherPlayer.isActive()) otherPlayer.stop();
        active = true;
        startedAt = Date.now();
        box.open = true;
        ui.play.textContent = '⏸ Pause';
        ui.stop.hidden = false;
        engineStart(buildQueue(), {
          onProgress: function (m, index, total) {
            ui.progress.style.width = Math.round(((index + 1) / total) * 100) + '%';
            if (m) {
              highlight(m.line);
              ui.status.textContent = 'Réplique ' + (m.line + 1) + '/' + lignes.length;
            }
          },
          onDone: function () {
            var duree = Date.now() - startedAt;
            stop();
            ui.status.textContent = (duree < 2500 && lignes.length > 8)
              ? '🔇 La voix n\'a pas démarré — vérifiez les voix du système.'
              : '✓ Podcast terminé.';
          }
        }, fromIndex || 0);
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

      ui.play.addEventListener('click', function () {
        if (!active) { start(); return; }
        if (Engine.paused) { engineResume(); ui.play.textContent = '⏸ Pause'; }
        else { enginePause(); ui.play.textContent = '▶ Reprendre'; }
      });
      ui.stop.addEventListener('click', stop);
      ui.rate.addEventListener('change', function () {
        prefs.podcastRate = parseFloat(ui.rate.value) || 1;
        savePrefs();
        if (active) start(Engine.index);
      });

      script.addEventListener('click', function (e) {
        var line = e.target.closest && e.target.closest('.podcast-line');
        if (!line) return;
        var target = parseInt(line.dataset.line, 10);
        if (isNaN(target)) return;
        if (!active) start();
        setTimeout(function () {
          for (var i = 0; i < Engine.queue.length; i++) {
            if (Engine.queue[i].meta.line === target) { engineJump(i); return; }
          }
        }, active ? 0 : 180);
      });
    }
  }

  /* ============================================================
     5. Amorçage
     ============================================================ */

  function boot() {
    if (!document.querySelector('.module-content')) return;
    whenVoicesReady(function () {
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
    });
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
