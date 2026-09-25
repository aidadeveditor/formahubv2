/* ============================================================
   Formahub — mode hors ligne (V10)

   • Enregistre le service worker et affiche le bandeau « hors ligne ».
   • Le TEXTE est hors ligne d'office : dès la première visite de
     n'importe quelle page, le script range dans le cache toutes les
     adresses de offline-manifest.json (40 modules, quiz, scripts de
     podcast, pages, styles). Aucun bouton : il complète ce qui manque
     à chaque visite, en silence.
   • Les AUDIOS se téléchargent à la demande depuis la page
     Paramètres (voir audio.js).

   V10 — pourquoi le téléchargement échouait sur mobile :
   il était confié au service worker par message. Sur iOS et Android,
   le navigateur suspend un service worker au bout de quelques dizaines
   de secondes, et la page attendait une réponse qui ne venait jamais.
   Le travail se fait maintenant dans la page elle-même (API Cache),
   qui reste active tant qu'elle est ouverte.
   ============================================================ */

(function () {
  'use strict';

  /* Le script peut être chargé depuis la racine ou depuis un module :
     on déduit la racine du site de sa propre adresse. */
  var SELF = document.currentScript;
  var ROOT = (function () {
    if (SELF && SELF.src) return SELF.src.replace(/assets\/js\/offline\.js.*$/, '');
    return new URL('.', location.href).toString();
  })();

  var CACHE = 'formahub-offline-v1';      // même nom que dans sw.js
  var MATCH = { ignoreSearch: true, ignoreVary: true };
  var SECURE = location.protocol === 'https:' ||
    location.hostname === 'localhost' || location.hostname === '127.0.0.1';
  var CAN_CACHE = SECURE && ('caches' in window);

  /* État partagé avec la page Paramètres */
  var Text = { total: 0, have: 0, running: false, done: false, error: null, listeners: [] };

  function emit() {
    Text.listeners.forEach(function (fn) { try { fn(Text); } catch (e) { /* ignore */ } });
  }

  /* ---------- Adresses équivalentes d'une même page (cf. sw.js) ---------- */

  function variants(url) {
    var u = new URL(url);
    u.search = '';
    u.hash = '';
    var out = [u.toString()];
    var p = u.pathname;
    function add(path) {
      var v = new URL(u.toString());
      v.pathname = path;
      if (out.indexOf(v.toString()) === -1) out.push(v.toString());
    }
    if (/\/index\.html$/.test(p)) {
      add(p.slice(0, -'index.html'.length));
      add(p.slice(0, -'/index.html'.length) || '/');
    } else if (/\/$/.test(p)) {
      add(p + 'index.html');
      if (p.length > 1) add(p.slice(0, -1));
    } else if (/\.html$/.test(p)) {
      add(p.slice(0, -'.html'.length));
    } else if (!/\.[a-z0-9]+$/i.test(p)) {
      add(p + '.html');
      add(p + '/');
      add(p + '/index.html');
    }
    return out;
  }

  function lookup(cache, url) {
    var list = variants(url);
    var i = 0;
    function next() {
      if (i >= list.length) return Promise.resolve(null);
      return cache.match(list[i++], MATCH).then(function (hit) { return hit || next(); });
    }
    return next();
  }

  /* Une réponse « redirigée » ne peut pas servir une navigation :
     on en range une copie propre, sous toutes ses adresses. */
  function store(cache, url, res) {
    var finalUrl = res.url;
    return res.blob().then(function (body) {
      var keys = variants(url);
      if (finalUrl) variants(finalUrl).forEach(function (k) { if (keys.indexOf(k) === -1) keys.push(k); });
      return Promise.all(keys.map(function (k) {
        return cache.put(k, new Response(body, { status: res.status, statusText: res.statusText, headers: res.headers }));
      }));
    });
  }

  function abs(path) { return new URL(path, ROOT).toString(); }

  /* ---------- Texte hors ligne automatique ---------- */

  function loadManifest() {
    return fetch(abs('offline-manifest.json'), { cache: 'no-cache' })
      .then(function (r) { if (!r.ok) throw new Error('manifeste ' + r.status); return r.json(); })
      .then(function (m) { return (m && m.urls) || []; });
  }

  function ensureText() {
    if (!CAN_CACHE || Text.running) return Promise.resolve(Text);
    Text.running = true;
    Text.error = null;
    emit();

    var cache;
    return Promise.all([caches.open(CACHE), loadManifest()])
      .then(function (r) {
        cache = r[0];
        var urls = r[1];
        Text.total = urls.length;
        // Ce qui manque encore sur cet appareil
        return Promise.all(urls.map(function (u) {
          return lookup(cache, abs(u)).then(function (hit) { return hit ? null : u; });
        })).then(function (missing) {
          missing = missing.filter(Boolean);
          Text.have = urls.length - missing.length;
          emit();
          return fill(cache, missing);
        });
      })
      .catch(function (e) { Text.error = (e && e.message) || 'hors connexion'; })
      .then(function () {
        Text.running = false;
        Text.done = !Text.error && Text.total > 0 && Text.have >= Text.total;
        emit();
        return Text;
      });
  }

  function fill(cache, missing) {
    if (!missing.length || !navigator.onLine) return Promise.resolve();
    var i = 0;
    var BATCH = 4;
    function worker() {
      if (i >= missing.length) return Promise.resolve();
      var u = missing[i++];
      return fetch(abs(u), { cache: 'reload' })
        .then(function (res) {
          if (res && res.ok) return store(cache, abs(u), res).then(function () { Text.have += 1; emit(); });
        })
        .catch(function () { /* réessayé à la prochaine visite */ })
        .then(worker);
    }
    var workers = [];
    for (var k = 0; k < BATCH; k++) workers.push(worker());
    return Promise.all(workers);
  }

  // Petites aides partagées avec audio.js
  window.formahubOffline = {
    text: Text,
    onChange: function (fn) { Text.listeners.push(fn); fn(Text); },
    ensureText: ensureText,
    persist: function () {
      try {
        if (navigator.storage && navigator.storage.persist) return navigator.storage.persist();
      } catch (e) { /* ignore */ }
      return Promise.resolve(false);
    }
  };

  /* ---------- Bandeau « hors ligne » sur toutes les pages ---------- */

  function initBanner() {
    var banner = document.createElement('div');
    banner.className = 'offline-banner';
    banner.setAttribute('role', 'status');
    banner.hidden = true;
    banner.innerHTML = '<span aria-hidden="true">📴</span> ' +
      '<span class="offline-banner-text">Hors connexion — vous consultez la version enregistrée.</span>';
    document.body.appendChild(banner);

    function paint() {
      banner.hidden = navigator.onLine;
      document.documentElement.classList.toggle('is-offline', !navigator.onLine);
    }
    window.addEventListener('online', function () { paint(); ensureText(); });
    window.addEventListener('offline', paint);
    paint();
  }

  /* ---------- État du texte sur la page Paramètres ---------- */

  function initTextStatus() {
    var el = document.getElementById('offline-text-status');
    if (!el) return;
    if (!('serviceWorker' in navigator) || !('caches' in window)) {
      el.innerHTML = '<span class="dot dot-ko"></span> Ce navigateur ne gère pas la consultation hors ligne.';
      return;
    }
    if (!SECURE) {
      el.innerHTML = '<span class="dot"></span> Actif uniquement sur le site en ligne (https://), pas sur un fichier ouvert depuis le disque.';
      return;
    }
    window.formahubOffline.onChange(function (t) {
      if (t.done) {
        el.innerHTML = '<span class="dot dot-ok"></span> Disponible hors ligne — les 40 modules, quiz et scripts de podcast (' +
          t.have + '/' + t.total + ' fichiers).';
      } else if (t.running) {
        el.innerHTML = '<span class="dot dot-run"></span> Enregistrement automatique… ' +
          (t.total ? t.have + '/' + t.total + ' fichiers' : '');
      } else if (t.total) {
        el.innerHTML = '<span class="dot dot-ko"></span> ' + t.have + '/' + t.total +
          ' fichiers enregistrés — le reste se complétera à la prochaine connexion.';
      } else if (t.error) {
        el.innerHTML = '<span class="dot dot-ko"></span> Vérification impossible (' + t.error + ').';
      }
    });
  }

  /* ---------- Amorçage ---------- */

  function boot() {
    initBanner();
    initTextStatus();
    // On laisse la page s'afficher avant de travailler en arrière-plan
    setTimeout(ensureText, document.getElementById('offline-text-status') ? 0 : 1500);
  }

  if ('serviceWorker' in navigator && SECURE) {
    navigator.serviceWorker.register(ROOT + 'sw.js', { scope: ROOT })
      .catch(function () { /* le site fonctionne sans */ });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
