/* ============================================================
   Formahub — mode hors ligne (V7)
   Enregistre le service worker, propose le téléchargement complet
   de la plateforme en un clic, et signale la perte de connexion.
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

  var STATE_KEY = 'formahub-offline-state';
  var registration = null;

  function readState() {
    try {
      var raw = localStorage.getItem(STATE_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch (e) { return {}; }
  }

  function writeState(s) {
    try { localStorage.setItem(STATE_KEY, JSON.stringify(s)); } catch (e) { /* ignore */ }
  }

  function humanBytes(n) {
    if (!n && n !== 0) return '';
    if (n < 1024) return n + ' o';
    if (n < 1024 * 1024) return Math.round(n / 1024) + ' Ko';
    return (n / (1024 * 1024)).toFixed(1).replace('.', ',') + ' Mo';
  }

  function humanDate(iso) {
    if (!iso) return '';
    try {
      return new Date(iso).toLocaleDateString('fr-FR', {
        day: '2-digit', month: 'long', year: 'numeric', hour: '2-digit', minute: '2-digit'
      });
    } catch (e) { return iso.slice(0, 10); }
  }

  /* ---------- Échange avec le service worker ---------- */

  function ask(message, onMessage) {
    return new Promise(function (resolve, reject) {
      var target = (registration && (registration.active || registration.waiting)) ||
        navigator.serviceWorker.controller;
      if (!target) { reject(new Error('service worker inactif')); return; }
      var channel = new MessageChannel();
      channel.port1.onmessage = function (e) {
        var data = e.data || {};
        if (onMessage) onMessage(data);
        if (data.type === 'PRECACHE_DONE' || data.type === 'STATUS' || data.type === 'CLEARED') {
          resolve(data);
        }
      };
      target.postMessage(message, [channel.port2]);
      setTimeout(function () { reject(new Error('délai dépassé')); }, 15 * 60 * 1000);
    });
  }

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
    window.addEventListener('online', paint);
    window.addEventListener('offline', paint);
    paint();
  }

  /* ---------- Panneau de l'accueil ---------- */

  function initPanel() {
    var panel = document.getElementById('offline-panel');
    if (!panel) return;
    var body = panel.querySelector('.tool-body') || panel;

    if (!('serviceWorker' in navigator)) {
      body.innerHTML = '<p class="tool-note">Ce navigateur ne gère pas le mode hors ligne. ' +
        'La plateforme reste consultable normalement en ligne.</p>';
      return;
    }
    if (location.protocol !== 'https:' && location.hostname !== 'localhost' && location.hostname !== '127.0.0.1') {
      body.innerHTML = '<p class="tool-note">Le mode hors ligne demande une adresse sécurisée. ' +
        'Il s\'activera automatiquement sur le site déployé (<code>https://</code>) ; ' +
        'il ne fonctionne pas sur un fichier ouvert directement depuis le disque.</p>';
      return;
    }

    body.innerHTML =
      '<div class="tool-status" id="offline-status">Vérification…</div>' +
      '<div class="tool-progress" id="offline-progress" hidden><span></span></div>' +
      '<div class="tool-actions">' +
      '  <button type="button" class="btn btn-primary btn-sm" id="offline-download">⬇ Rendre disponible hors ligne</button>' +
      '  <button type="button" class="btn btn-ghost btn-sm" id="offline-clear">Vider le cache</button>' +
      '</div>' +
      '<p class="tool-note" id="offline-note"></p>';

    var status = body.querySelector('#offline-status');
    var progress = body.querySelector('#offline-progress');
    var fill = progress.firstElementChild;
    var btn = body.querySelector('#offline-download');
    var clear = body.querySelector('#offline-clear');
    var note = body.querySelector('#offline-note');
    var catalogue = { count: 0, bytes: 0 };

    // Volume réel annoncé avant le téléchargement, lu dans le manifeste
    fetch(ROOT + 'offline-manifest.json', { cache: 'no-cache' })
      .then(function (r) { return r.json(); })
      .then(function (m) {
        catalogue.count = (m && m.count) || 0;
        catalogue.bytes = (m && m.approx_bytes) || 0;
        refresh();
      })
      .catch(function () { /* le bouton reste utilisable */ });

    function refresh() {
      var s = readState();
      if (s.done) {
        status.innerHTML = '<span class="dot dot-ok"></span> Disponible hors ligne — ' +
          s.done + ' fichiers' + (s.bytes ? ' · ' + humanBytes(s.bytes) : '');
        note.textContent = 'Dernier téléchargement le ' + humanDate(s.date) +
          '. Relancez-le après chaque mise en ligne pour récupérer les nouveautés.';
        btn.textContent = '↻ Mettre à jour la copie hors ligne';
        clear.hidden = false;
      } else {
        status.innerHTML = '<span class="dot"></span> Pas encore téléchargé';
        note.textContent = catalogue.count
          ? 'Un seul clic enregistre les ' + catalogue.count + ' fichiers de la plateforme — ' +
            'modules, quiz et podcasts — dans ce navigateur. Comptez quelques secondes et ' +
            humanBytes(catalogue.bytes) + '.'
          : 'Un seul clic enregistre toute la plateforme dans ce navigateur : ' +
            'modules, quiz et podcasts.';
        btn.textContent = '⬇ Rendre disponible hors ligne';
        clear.hidden = true;
      }
    }

    refresh();

    btn.addEventListener('click', function () {
      btn.disabled = true;
      clear.disabled = true;
      progress.hidden = false;
      fill.style.width = '2%';
      status.innerHTML = '<span class="dot dot-run"></span> Téléchargement en cours…';

      fetch(ROOT + 'offline-manifest.json', { cache: 'no-cache' })
        .then(function (r) { return r.json(); })
        .then(function (manifest) {
          var urls = (manifest && manifest.urls) || [];
          return ask({ type: 'PRECACHE', urls: urls }, function (msg) {
            if (msg.type === 'PRECACHE_PROGRESS') {
              var pct = Math.round((msg.done / msg.total) * 100);
              fill.style.width = Math.max(2, pct) + '%';
              status.innerHTML = '<span class="dot dot-run"></span> ' +
                msg.done + ' / ' + msg.total + ' fichiers enregistrés';
            }
          });
        })
        .then(function (msg) {
          writeState({
            done: msg.done - (msg.failed || 0),
            total: msg.total,
            failed: msg.failed || 0,
            bytes: msg.bytes || null,
            date: new Date().toISOString()
          });
          fill.style.width = '100%';
          setTimeout(function () { progress.hidden = true; fill.style.width = '0%'; }, 900);
          refresh();
          if (msg.failed) {
            note.textContent += ' ' + msg.failed + ' fichier(s) n\'ont pas pu être enregistrés — ' +
              'relancez le téléchargement pour compléter.';
          }
          if (typeof window.formahubToast === 'function') {
            window.formahubToast('📦 Formahub est disponible hors ligne.');
          }
        })
        .catch(function () {
          progress.hidden = true;
          status.innerHTML = '<span class="dot dot-ko"></span> Téléchargement interrompu';
          note.textContent = 'Vérifiez la connexion et réessayez. Rien n\'a été perdu.';
        })
        .then(function () { btn.disabled = false; clear.disabled = false; });
    });

    clear.addEventListener('click', function () {
      clear.disabled = true;
      ask({ type: 'CLEAR' })
        .then(function () {
          writeState({});
          refresh();
          if (typeof window.formahubToast === 'function') {
            window.formahubToast('🧹 Copie hors ligne supprimée.');
          }
        })
        .catch(function () { /* rien à supprimer */ })
        .then(function () { clear.disabled = false; });
    });

    // Statut réel du cache, si le service worker répond
    navigator.serviceWorker.ready.then(function () {
      return ask({ type: 'STATUS' });
    }).then(function (msg) {
      var s = readState();
      if (msg && msg.count > 12 && !s.done) {
        writeState({ done: msg.count, total: msg.count, bytes: msg.bytes, date: s.date || new Date().toISOString() });
        refresh();
      }
    }).catch(function () { /* ignore */ });
  }

  /* ---------- Amorçage ---------- */

  function boot() {
    initBanner();
    initPanel();
  }

  if ('serviceWorker' in navigator &&
      (location.protocol === 'https:' || location.hostname === 'localhost' || location.hostname === '127.0.0.1')) {
    navigator.serviceWorker.register(ROOT + 'sw.js', { scope: ROOT })
      .then(function (reg) { registration = reg; })
      .catch(function () { /* le site fonctionne sans */ });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
