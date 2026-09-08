/* ============================================================
   Formahub — sauvegarde automatique par code secret (V7)

   Un code choisi par l'utilisatrice remplace l'identifiant aléatoire
   d'origine. Il ne quitte jamais le navigateur : on en dérive
     • une adresse de stockage  = SHA-256("formahub-id:" + code) ;
     • une clé de chiffrement   = PBKDF2(code) → AES-GCM 256 bits.
   Le serveur (Cloudflare KV) ne reçoit donc qu'un bloc chiffré :
   sans le code, la progression est illisible, y compris pour lui.

   Sont sauvegardés : progression des modules, cases cochées,
   sections lues, inscriptions aux formations externes, dernier
   module consulté, préférences de lecture audio et thème.
   ============================================================ */

(function () {
  'use strict';

  var SELF = document.currentScript;
  var ROOT = (function () {
    if (SELF && SELF.src) return SELF.src.replace(/assets\/js\/sync\.js.*$/, '');
    return new URL('.', location.href).toString();
  })();

  var CONF_KEY = 'formahub-backup';
  var WATCHED = [
    'formahub-progress',
    'formahub-checklists',
    'formahub-sections',
    'formahub-inscriptions',
    'formahub-last-module',
    'formahub-audio-prefs',
    'theme-preference'
  ];

  var SUBTLE = (window.crypto && window.crypto.subtle) ? window.crypto.subtle : null;
  var enc = new TextEncoder();
  var dec = new TextDecoder();

  var conf = readConf();
  var key = null;            // CryptoKey dérivée du code, gardée en mémoire
  var pushTimer = null;
  var lastSignature = null;
  var busy = false;

  /* ---------- Stockage local ---------- */

  function readConf() {
    try {
      var raw = localStorage.getItem(CONF_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch (e) { return {}; }
  }

  function writeConf() {
    try { localStorage.setItem(CONF_KEY, JSON.stringify(conf)); } catch (e) { /* ignore */ }
  }

  function bundle() {
    var data = {};
    WATCHED.forEach(function (k) {
      try {
        var raw = localStorage.getItem(k);
        if (raw !== null) data[k] = raw;
      } catch (e) { /* ignore */ }
    });
    return data;
  }

  function applyBundle(data) {
    if (!data) return;
    WATCHED.forEach(function (k) {
      if (typeof data[k] !== 'string') return;
      try { localStorage.setItem(k, data[k]); } catch (e) { /* ignore */ }
    });
  }

  function signature() {
    var d = bundle();
    return WATCHED.map(function (k) { return (d[k] || '').length + ':' + (d[k] || '').slice(-24); }).join('|');
  }

  function countDone(data) {
    try {
      var p = JSON.parse((data && data['formahub-progress']) || '{}');
      return Object.keys(p).filter(function (k) { return p[k] && p[k].completed; }).length;
    } catch (e) { return 0; }
  }

  /* ---------- Dérivation du code ---------- */

  function toHex(buffer) {
    var bytes = new Uint8Array(buffer);
    var out = '';
    for (var i = 0; i < bytes.length; i++) out += ('0' + bytes[i].toString(16)).slice(-2);
    return out;
  }

  function b64(buffer) {
    var bytes = new Uint8Array(buffer);
    var s = '';
    for (var i = 0; i < bytes.length; i++) s += String.fromCharCode(bytes[i]);
    return btoa(s);
  }

  function unb64(str) {
    var s = atob(str);
    var bytes = new Uint8Array(s.length);
    for (var i = 0; i < s.length; i++) bytes[i] = s.charCodeAt(i);
    return bytes;
  }

  function normalizeCode(code) {
    return String(code || '').trim().toLowerCase().replace(/\s+/g, ' ');
  }

  function deriveId(code) {
    if (!SUBTLE) {
      // Repli sans WebCrypto : identifiant simple, sans chiffrement
      var h = 5381;
      var s = 'formahub-id:' + code;
      for (var i = 0; i < s.length; i++) h = ((h * 33) ^ s.charCodeAt(i)) >>> 0;
      return Promise.resolve(('00000000' + h.toString(16)).slice(-8).repeat(2));
    }
    return SUBTLE.digest('SHA-256', enc.encode('formahub-id:' + code))
      .then(function (buf) { return toHex(buf).slice(0, 32); });
  }

  function deriveKey(code, id) {
    if (!SUBTLE) return Promise.resolve(null);
    return SUBTLE.importKey('raw', enc.encode(code), { name: 'PBKDF2' }, false, ['deriveKey'])
      .then(function (material) {
        return SUBTLE.deriveKey(
          {
            name: 'PBKDF2',
            salt: enc.encode('formahub-v7-salt:' + id),
            iterations: 150000,
            hash: 'SHA-256'
          },
          material,
          { name: 'AES-GCM', length: 256 },
          false,
          ['encrypt', 'decrypt']
        );
      });
  }

  function encryptPayload(obj) {
    var json = JSON.stringify(obj);
    if (!key) return Promise.resolve(JSON.stringify({ v: 1, plain: json }));
    var iv = window.crypto.getRandomValues(new Uint8Array(12));
    return SUBTLE.encrypt({ name: 'AES-GCM', iv: iv }, key, enc.encode(json))
      .then(function (ct) {
        return JSON.stringify({ v: 1, iv: b64(iv), ct: b64(ct) });
      });
  }

  function decryptPayload(text) {
    var raw;
    try { raw = JSON.parse(text); } catch (e) { return Promise.resolve(null); }
    if (!raw || (!raw.ct && !raw.plain)) return Promise.resolve(null);
    if (raw.plain) {
      try { return Promise.resolve(JSON.parse(raw.plain)); } catch (e) { return Promise.resolve(null); }
    }
    if (!key) return Promise.reject(new Error('nokey'));
    return SUBTLE.decrypt({ name: 'AES-GCM', iv: unb64(raw.iv) }, key, unb64(raw.ct))
      .then(function (buf) { return JSON.parse(dec.decode(buf)); });
  }

  /* ---------- Échanges avec le Worker ---------- */

  function push() {
    if (!conf.id || !conf.active || busy) return Promise.resolve(false);
    if (!navigator.onLine) return Promise.resolve(false);
    busy = true;
    var payload = { v: 1, updatedAt: new Date().toISOString(), data: bundle() };
    return encryptPayload(payload)
      .then(function (body) {
        return fetch(ROOT + 'api/progress/' + conf.id, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: body
        });
      })
      .then(function (r) {
        if (!r.ok) throw new Error('http ' + r.status);
        conf.lastPush = payload.updatedAt;
        conf.localUpdatedAt = payload.updatedAt;
        writeConf();
        lastSignature = signature();
        paint();
        return true;
      })
      .catch(function () { return false; })
      .then(function (v) { busy = false; return v; });
  }

  function pull() {
    if (!conf.id) return Promise.resolve(null);
    return fetch(ROOT + 'api/progress/' + conf.id, { cache: 'no-store' })
      .then(function (r) { return r.ok ? r.text() : '{}'; })
      .then(function (text) {
        if (!text || text === '{}' || text === '') return null;
        return decryptPayload(text);
      });
  }

  /* ---------- Fusion ---------- */

  function mergeBundles(local, remote) {
    var out = {};
    WATCHED.forEach(function (k) {
      var a = local[k];
      var b = remote[k];
      if (!a) { if (b) out[k] = b; return; }
      if (!b) { out[k] = a; return; }
      if (k === 'formahub-progress' || k === 'formahub-checklists' ||
          k === 'formahub-sections' || k === 'formahub-inscriptions') {
        try {
          var A = JSON.parse(a) || {};
          var B = JSON.parse(b) || {};
          var merged = {};
          Object.keys(B).forEach(function (id) { merged[id] = B[id]; });
          Object.keys(A).forEach(function (id) {
            if (!merged[id]) { merged[id] = A[id]; return; }
            // Deux valeurs : on garde l'entrée la plus « avancée »
            if (typeof A[id] === 'object' && typeof merged[id] === 'object') {
              var da = A[id].date || '';
              var db = merged[id].date || '';
              merged[id] = (da && db) ? (da <= db ? A[id] : merged[id]) : (A[id] || merged[id]);
              if (k === 'formahub-checklists' || k === 'formahub-sections') {
                var u = {};
                Object.keys(merged[id]).forEach(function (x) { u[x] = merged[id][x]; });
                Object.keys(A[id]).forEach(function (x) { if (A[id][x]) u[x] = true; });
                merged[id] = u;
              }
            }
          });
          out[k] = JSON.stringify(merged);
        } catch (e) { out[k] = a; }
      } else {
        out[k] = a;   // préférences : l'appareil courant fait foi
      }
    });
    return out;
  }

  /* ---------- Boucle de sauvegarde ---------- */

  function queueBackup() {
    if (!conf.active) return;
    clearTimeout(pushTimer);
    pushTimer = setTimeout(function () { push(); }, 2500);
  }

  function watchChanges() {
    lastSignature = signature();
    setInterval(function () {
      if (!conf.active) return;
      var sig = signature();
      if (sig !== lastSignature) {
        lastSignature = sig;
        queueBackup();
      }
    }, 4000);

    document.addEventListener('visibilitychange', function () {
      if (document.visibilityState === 'hidden' && conf.active && signature() !== conf.pushedSignature) push();
    });
    window.addEventListener('online', function () { if (conf.active) push(); });
  }

  /* ---------- Activation d'un code ---------- */

  function activate(rawCode, strategy) {
    var code = normalizeCode(rawCode);
    if (code.length < 6) return Promise.reject(new Error('court'));

    return deriveId(code)
      .then(function (id) {
        conf.id = id;
        return deriveKey(code, id);
      })
      .then(function (k) {
        key = k;
        conf.code = code;             // gardé sur cet appareil pour la reprise automatique
        return pull();
      })
      .then(function (remote) {
        var local = bundle();
        var localCount = countDone(local);
        var remoteCount = remote ? countDone(remote.data) : 0;

        if (!remote) {
          conf.active = true;
          writeConf();
          return push().then(function () {
            // Aucune sauvegarde à ce code : soit c'est la première fois,
            // soit le code comporte une faute de frappe. On le dit.
            return { mode: localCount ? 'created' : 'created-vide', local: localCount, remote: 0 };
          });
        }

        if (strategy === 'remote' || (!strategy && localCount === 0)) {
          applyBundle(remote.data);
          conf.active = true;
          writeConf();
          return { mode: 'restored', local: localCount, remote: remoteCount, reload: true };
        }
        if (strategy === 'local') {
          conf.active = true;
          writeConf();
          return push().then(function () { return { mode: 'pushed', local: localCount, remote: remoteCount }; });
        }
        if (strategy === 'merge') {
          applyBundle(mergeBundles(local, remote.data));
          conf.active = true;
          writeConf();
          return push().then(function () { return { mode: 'merged', local: localCount, remote: remoteCount, reload: true }; });
        }
        // Deux jeux de données et aucune consigne : on demande
        return { mode: 'conflict', local: localCount, remote: remoteCount };
      });
  }

  function resume() {
    if (!conf.active || !conf.code) return Promise.resolve(false);
    return deriveKey(conf.code, conf.id)
      .then(function (k) {
        key = k;
        return pull();
      })
      .then(function (remote) {
        if (!remote) return false;
        var localAt = conf.localUpdatedAt || '';
        if (remote.updatedAt && remote.updatedAt > localAt) {
          var merged = mergeBundles(bundle(), remote.data);
          applyBundle(merged);
          conf.localUpdatedAt = remote.updatedAt;
          writeConf();
          return true;
        }
        return false;
      })
      .catch(function () { return false; });
  }

  function forget() {
    conf = {};
    key = null;
    writeConf();
    try { localStorage.removeItem(CONF_KEY); } catch (e) { /* ignore */ }
    paint();
  }

  /* ---------- Interface du panneau ---------- */

  var panelBody = null;

  function humanDate(iso) {
    if (!iso) return '';
    try {
      return new Date(iso).toLocaleString('fr-FR', {
        day: '2-digit', month: 'long', hour: '2-digit', minute: '2-digit'
      });
    } catch (e) { return iso; }
  }

  function paint() {
    if (!panelBody) return;

    if (!conf.active) {
      panelBody.innerHTML =
        '<div class="tool-status"><span class="dot"></span> Sauvegarde non activée</div>' +
        '<label class="backup-field" for="backup-code">Votre code secret</label>' +
        '<div class="backup-row">' +
        '  <input type="password" id="backup-code" class="backup-input" autocomplete="off" ' +
        '         placeholder="au moins 6 caractères" aria-describedby="backup-note">' +
        '  <button type="button" class="btn btn-ghost btn-sm" id="backup-show" aria-label="Afficher le code">👁</button>' +
        '  <button type="button" class="btn btn-primary btn-sm" id="backup-go">Activer</button>' +
        '</div>' +
        '<p class="tool-note" id="backup-note">Ce code identifie votre progression et sert de clé de ' +
        'chiffrement : saisissez le même sur un autre appareil pour y retrouver vos modules validés. ' +
        'Il n\'est jamais envoyé au serveur, et personne ne peut le réinitialiser — notez-le.</p>' +
        '<div class="backup-choice" id="backup-choice" hidden></div>';

      var input = panelBody.querySelector('#backup-code');
      var go = panelBody.querySelector('#backup-go');
      var show = panelBody.querySelector('#backup-show');
      var note = panelBody.querySelector('#backup-note');
      var choice = panelBody.querySelector('#backup-choice');

      show.addEventListener('click', function () {
        input.type = input.type === 'password' ? 'text' : 'password';
      });

      function attempt(strategy) {
        go.disabled = true;
        note.textContent = 'Vérification…';
        activate(input.value, strategy)
          .then(function (res) {
            if (res.mode === 'conflict') {
              note.textContent = 'Ce code contient déjà une sauvegarde (' + res.remote +
                ' module(s) validé(s)) et cet appareil en a ' + res.local + '. Que faire ?';
              choice.hidden = false;
              choice.innerHTML =
                '<button type="button" class="btn btn-primary btn-sm" data-strategy="merge">Fusionner les deux</button>' +
                '<button type="button" class="btn btn-outline btn-sm" data-strategy="remote">Prendre la sauvegarde</button>' +
                '<button type="button" class="btn btn-outline btn-sm" data-strategy="local">Garder cet appareil</button>';
              go.disabled = false;
              return;
            }
            toast(res.mode === 'restored' ? '☁️ Progression restaurée depuis votre code.' :
                  res.mode === 'merged' ? '🔗 Les deux progressions ont été fusionnées.' :
                  '🔒 Sauvegarde automatique activée.');
            paint();
            if (res.mode === 'created-vide') {
              var st = panelBody.querySelector('.tool-note');
              if (st) {
                st.textContent = 'Aucune sauvegarde n\'existait sous ce code : une nouvelle vient ' +
                  'd\'être créée, vide. Si vous pensiez retrouver une progression, le code comporte ' +
                  'sans doute une faute de frappe — cliquez sur « Oublier sur cet appareil » et ressaisissez-le.';
              }
            }
            if (res.reload) setTimeout(function () { location.reload(); }, 900);
          })
          .catch(function (e) {
            go.disabled = false;
            if (e && e.message === 'court') {
              note.textContent = 'Choisissez un code d\'au moins 6 caractères — une phrase courte fait ' +
                'un très bon code (« mes-formations-2026 »).';
            } else if (e && e.message === 'nokey') {
              note.textContent = 'Ce code ne permet pas de lire la sauvegarde existante : ' +
                'vérifiez l\'orthographe, majuscules comprises.';
            } else {
              note.textContent = 'La sauvegarde n\'a pas pu être jointe. Réessayez plus tard — ' +
                'la progression reste enregistrée dans ce navigateur.';
            }
          });
      }

      go.addEventListener('click', function () { attempt(null); });
      input.addEventListener('keydown', function (e) { if (e.key === 'Enter') attempt(null); });
      choice.addEventListener('click', function (e) {
        var s = e.target.dataset && e.target.dataset.strategy;
        if (s) { choice.hidden = true; attempt(s); }
      });
      return;
    }

    var done = countDone(bundle());
    panelBody.innerHTML =
      '<div class="tool-status"><span class="dot dot-ok"></span> Sauvegarde active · ' +
      done + ' module(s) validé(s)</div>' +
      '<p class="tool-note">' +
      (conf.lastPush ? 'Dernière sauvegarde le ' + humanDate(conf.lastPush) + '. ' : '') +
      'Tout changement part automatiquement dans les secondes qui suivent. ' +
      (SUBTLE ? 'Le contenu est chiffré avec votre code avant l\'envoi.' :
                'Ce navigateur ne propose pas de chiffrement : la sauvegarde part en clair.') +
      '</p>' +
      '<div class="tool-actions">' +
      '  <button type="button" class="btn btn-primary btn-sm" id="backup-now">Sauvegarder maintenant</button>' +
      '  <button type="button" class="btn btn-outline btn-sm" id="backup-restore">Restaurer</button>' +
      '  <button type="button" class="btn btn-ghost btn-sm" id="backup-forget">Oublier sur cet appareil</button>' +
      '</div>';

    panelBody.querySelector('#backup-now').addEventListener('click', function () {
      push().then(function (ok) {
        toast(ok ? '☁️ Progression sauvegardée.' : '⚠️ Sauvegarde impossible pour le moment.');
        paint();
      });
    });

    panelBody.querySelector('#backup-restore').addEventListener('click', function () {
      pull().then(function (remote) {
        if (!remote) { toast('Aucune sauvegarde trouvée pour ce code.'); return; }
        applyBundle(mergeBundles(bundle(), remote.data));
        conf.localUpdatedAt = remote.updatedAt;
        writeConf();
        toast('☁️ Progression restaurée.');
        setTimeout(function () { location.reload(); }, 700);
      }).catch(function () { toast('⚠️ Restauration impossible.'); });
    });

    panelBody.querySelector('#backup-forget').addEventListener('click', function () {
      forget();
      toast('Ce navigateur ne sauvegarde plus. La progression locale est intacte.');
    });
  }

  function toast(message) {
    if (typeof window.formahubToast === 'function') window.formahubToast(message);
  }

  /* ---------- Amorçage ---------- */

  function boot() {
    var panel = document.getElementById('backup-panel');
    if (panel) {
      panelBody = panel.querySelector('.tool-body') || panel;
      paint();
    }
    if (conf.active && conf.code) {
      resume().then(function (changed) {
        if (changed) {
          if (typeof window.updateUIProgress === 'function') window.updateUIProgress();
          paint();
          toast('☁️ Progression mise à jour depuis votre sauvegarde.');
        }
      });
    }
    watchChanges();
  }

  window.formahubQueueBackup = queueBackup;
  window.formahubBackupActive = function () { return !!conf.active; };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
