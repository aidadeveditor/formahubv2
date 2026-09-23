/* ============================================================
   Formahub — service worker (V9)
   Rend la plateforme consultable sans connexion.

   Stratégies :
     • pages HTML          → réseau d'abord, cache en secours ;
     • CSS / JS / JSON     → cache d'abord, rafraîchi en arrière-plan ;
     • /api/               → réseau uniquement, jamais mis en cache.

   V9 — pourquoi les modules n'étaient pas disponibles hors ligne :
   Cloudflare (Pages comme Workers) redirige « …/module-1/index.html »
   vers « …/module-1/ » et « page.html » vers « page ». Le cache
   contenait donc des réponses « redirigées », que le navigateur refuse
   de servir pour une navigation, et rangées sous une adresse qui
   n'était pas celle que la page demande ensuite. Désormais chaque
   réponse est nettoyée avant d'être rangée, enregistrée sous toutes
   ses adresses équivalentes, et la recherche essaie ces variantes.
   ============================================================ */

// Changer VERSION à chaque mise en ligne. Si la copie hors ligne avait
// été téléchargée, elle est remise à jour toute seule à l'activation.
const VERSION = '2026-09-23-hors-ligne-v9';
const CACHE = 'formahub-offline-v1';
const CORE = [
  './',
  'index.html',
  'ressources-externes.html',
  'formations-espagne.html',
  'parametres.html',
  'assets/css/style.css',
  'assets/js/progress.js',
  'assets/js/quiz-engine.js',
  'assets/js/audio.js',
  'assets/js/offline.js',
  'assets/js/sync.js',
  'favicon.svg',
  'favicon.png',
  'apple-touch-icon.png',
  'offline-manifest.json'
];
// Marqueur posé quand la copie complète a été demandée sur cet appareil
const FULL_MARK = '__formahub-copie-complete';
// Versions ≤ V8 (sans marqueur) : une copie complète comptait plus de 100 entrées
const LEGACY_FULL_MIN = 100;
const MATCH = { ignoreSearch: true, ignoreVary: true };

const scopeUrl = () => new URL(self.registration.scope);

function abs(path) {
  return new URL(path, scopeUrl()).toString();
}

/* ---------- Adresses équivalentes d'une même page ---------- */

function variants(url) {
  const u = new URL(url);
  u.search = '';
  u.hash = '';
  const out = new Set([u.toString()]);
  const p = u.pathname;
  const add = path => { const v = new URL(u); v.pathname = path; out.add(v.toString()); };

  if (p.endsWith('/index.html')) {
    add(p.slice(0, -'index.html'.length));            // …/module-1/
    add(p.slice(0, -'/index.html'.length) || '/');    // …/module-1
  } else if (p.endsWith('/')) {
    add(p + 'index.html');
    if (p.length > 1) add(p.slice(0, -1));
  } else if (p.endsWith('.html')) {
    add(p.slice(0, -'.html'.length));                 // page
  } else if (!/\.[a-z0-9]+$/i.test(p)) {
    add(p + '.html');                                 // page → page.html
    add(p + '/');
    add(p + '/index.html');
  }
  return [...out];
}

/* Une réponse « redirigée » ne peut pas servir une navigation :
   on en fait une copie propre avant de la ranger. */
async function clean(res) {
  if (!res || !res.redirected) return res;
  const body = await res.blob();
  return new Response(body, { status: res.status, statusText: res.statusText, headers: res.headers });
}

async function store(cache, requestUrl, res) {
  const finalUrl = res.url;
  const copy = await clean(res);
  const keys = new Set(variants(requestUrl));
  if (finalUrl) variants(finalUrl).forEach(k => keys.add(k));
  await Promise.all([...keys].map(k => cache.put(k, copy.clone())));
}

async function lookup(cache, url) {
  for (const v of variants(url)) {
    const hit = await cache.match(v, MATCH);
    if (hit) return hit.redirected ? clean(hit) : hit;
  }
  return null;
}

/* ---------- Installation : la coquille ---------- */

self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE);
    await Promise.all(CORE.map(async path => {
      try {
        const res = await fetch(abs(path), { cache: 'reload' });
        if (res.ok) await store(cache, abs(path), res);
      } catch (e) { /* une ressource absente ne doit pas faire échouer l'installation */ }
    }));
    await self.skipWaiting();
  })());
});

/* ---------- Activation : ménage, réparation, mise à jour ---------- */

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const names = await caches.keys();
    await Promise.all(names.map(n => (n.startsWith('formahub-') && n !== CACHE) ? caches.delete(n) : null));
    await self.clients.claim();

    // Une copie complète existait (versions précédentes, avec des réponses
    // redirigées inutilisables) : on la refait avec la version courante.
    const cache = await caches.open(CACHE);
    const keys = await cache.keys();
    const wanted = (await cache.match(abs(FULL_MARK))) || keys.length >= LEGACY_FULL_MIN;
    if (wanted) {
      try {
        const res = await fetch(abs('offline-manifest.json'), { cache: 'reload' });
        const manifest = await res.json();
        await precache((manifest && manifest.urls) || [], () => {});
      } catch (e) { /* hors ligne à l'activation : la copie existante reste */ }
    }
  })());
});

/* ---------- Interception des requêtes ---------- */

self.addEventListener('fetch', event => {
  const request = event.request;
  if (request.method !== 'GET') return;

  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;
  if (url.pathname.includes('/api/')) return;   // progression : toujours le réseau

  const isDocument = request.mode === 'navigate' ||
    (request.headers.get('accept') || '').includes('text/html');

  event.respondWith(isDocument ? networkFirst(request) : cacheFirst(request));
});

async function networkFirst(request) {
  const cache = await caches.open(CACHE);
  try {
    const res = await fetch(request);
    if (res && res.ok) {
      store(cache, request.url, res.clone()).catch(() => {});
      return res;
    }
    const cached = await lookup(cache, request.url);
    return cached || res;
  } catch (e) {
    const cached = await lookup(cache, request.url);
    if (cached) return cached;
    return new Response(
      '<!DOCTYPE html><html lang="fr"><meta charset="utf-8">' +
      '<meta name="viewport" content="width=device-width, initial-scale=1">' +
      '<title>Formahub — hors ligne</title>' +
      '<body style="font-family:system-ui;max-width:38rem;margin:15vh auto;padding:0 1.5rem;line-height:1.6">' +
      '<h1>Page non disponible hors ligne</h1>' +
      '<p>Cette page n\'a pas encore été enregistrée sur cet appareil. Reconnectez-vous, ' +
      'puis lancez « Rendre disponible hors ligne » dans l\'onglet Paramètres.</p>' +
      '<p><a href="' + abs('index.html') + '">Retour à l\'accueil</a></p></body></html>',
      { status: 503, headers: { 'Content-Type': 'text/html; charset=utf-8' } }
    );
  }
}

async function cacheFirst(request) {
  const cache = await caches.open(CACHE);
  const cached = await lookup(cache, request.url);
  if (cached) {
    // Rafraîchissement silencieux pour la prochaine visite
    fetch(request).then(res => {
      if (res && res.ok) return store(cache, request.url, res);
    }).catch(() => { /* hors ligne : le cache suffit */ });
    return cached;
  }
  try {
    const res = await fetch(request);
    if (res && res.ok) store(cache, request.url, res.clone()).catch(() => {});
    return res;
  } catch (e) {
    return new Response('', { status: 504, statusText: 'Hors ligne' });
  }
}

/* ---------- Dialogue avec la page ---------- */

self.addEventListener('message', event => {
  const data = event.data || {};
  const reply = msg => {
    if (event.ports && event.ports[0]) event.ports[0].postMessage(msg);
  };

  if (data.type === 'PRECACHE') {
    event.waitUntil(precache(data.urls || [], reply));
  } else if (data.type === 'CLEAR') {
    event.waitUntil((async () => {
      await caches.delete(CACHE);
      reply({ type: 'CLEARED' });
    })());
  } else if (data.type === 'STATUS') {
    // Couverture réelle : combien des adresses du manifeste sont en cache
    event.waitUntil((async () => {
      const cache = await caches.open(CACHE);
      const urls = data.urls || [];
      let have = 0;
      const missing = [];
      for (const u of urls) {
        if (await lookup(cache, abs(u))) have += 1;
        else if (missing.length < 20) missing.push(u);
      }
      let bytes = null;
      try {
        const est = await navigator.storage.estimate();
        bytes = est && est.usage ? est.usage : null;
      } catch (e) { /* estimation indisponible */ }
      reply({ type: 'STATUS', have: have, total: urls.length, missing: missing, bytes: bytes });
    })());
  }
});

async function precache(urls, reply) {
  const cache = await caches.open(CACHE);
  const list = urls.map(u => abs(u));
  let done = 0;
  let failed = 0;
  const failures = [];
  const BATCH = 6;

  for (let i = 0; i < list.length; i += BATCH) {
    const slice = list.slice(i, i + BATCH);
    await Promise.all(slice.map(async u => {
      try {
        const res = await fetch(u, { cache: 'reload' });
        if (res && res.ok) await store(cache, u, res);
        else { failed += 1; failures.push(u); }
      } catch (e) {
        failed += 1;
        failures.push(u);
      } finally {
        done += 1;
      }
    }));
    reply({ type: 'PRECACHE_PROGRESS', done: done, total: list.length, failed: failed });
  }

  await cache.put(abs(FULL_MARK), new Response(new Date().toISOString()));

  let bytes = null;
  try {
    const est = await navigator.storage.estimate();
    bytes = est && est.usage ? est.usage : null;
  } catch (e) { /* ignore */ }
  reply({ type: 'PRECACHE_DONE', done: done, total: list.length, failed: failed, failures: failures.slice(0, 20), bytes: bytes });
}
