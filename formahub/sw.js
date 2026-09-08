/* ============================================================
   Formahub — service worker (V7)
   Rend la plateforme consultable sans connexion.

   Stratégies :
     • pages HTML          → réseau d'abord, cache en secours ;
     • CSS / JS / JSON     → cache d'abord, rafraîchi en arrière-plan ;
     • /api/               → réseau uniquement, jamais mis en cache.

   Le téléchargement complet est déclenché par la page (bouton
   « Rendre disponible hors ligne »), pas à l'installation : on ne
   consomme le forfait de personne sans son accord.
   ============================================================ */

const CACHE = 'formahub-offline-v1';
const CORE = [
  './',
  'index.html',
  'ressources-externes.html',
  'formations-espagne.html',
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

const scopeUrl = () => new URL(self.registration.scope);

function abs(path) {
  return new URL(path, scopeUrl()).toString();
}

/* ---------- Installation : uniquement la coquille ---------- */

self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE);
    await Promise.all(CORE.map(async path => {
      try {
        const res = await fetch(abs(path), { cache: 'reload' });
        if (res.ok) await cache.put(abs(path), res.clone());
      } catch (e) { /* une ressource absente ne doit pas faire échouer l'installation */ }
    }));
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const names = await caches.keys();
    await Promise.all(names.map(n => (n.startsWith('formahub-') && n !== CACHE) ? caches.delete(n) : null));
    await self.clients.claim();
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

  if (isDocument) {
    event.respondWith(networkFirst(request));
  } else {
    event.respondWith(cacheFirst(request));
  }
});

async function networkFirst(request) {
  const cache = await caches.open(CACHE);
  try {
    const res = await fetch(request);
    if (res && res.ok) cache.put(request, res.clone());
    return res;
  } catch (e) {
    const cached = await cache.match(request, { ignoreSearch: true });
    if (cached) return cached;
    const home = await cache.match(abs('index.html'));
    if (home) return home;
    return new Response(
      '<!DOCTYPE html><html lang="fr"><meta charset="utf-8">' +
      '<title>Formahub — hors ligne</title>' +
      '<body style="font-family:system-ui;max-width:38rem;margin:15vh auto;padding:0 1.5rem;line-height:1.6">' +
      '<h1>Page non disponible hors ligne</h1>' +
      '<p>Cette page n\'a pas encore été téléchargée. Reconnectez-vous, ' +
      'puis lancez « Rendre disponible hors ligne » depuis l\'accueil pour ' +
      'enregistrer l\'ensemble des modules.</p></body></html>',
      { status: 503, headers: { 'Content-Type': 'text/html; charset=utf-8' } }
    );
  }
}

async function cacheFirst(request) {
  const cache = await caches.open(CACHE);
  const cached = await cache.match(request, { ignoreSearch: true });
  if (cached) {
    // Rafraîchissement silencieux pour la prochaine visite
    fetch(request).then(res => {
      if (res && res.ok) cache.put(request, res.clone());
    }).catch(() => { /* hors ligne : le cache suffit */ });
    return cached;
  }
  try {
    const res = await fetch(request);
    if (res && res.ok) cache.put(request, res.clone());
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
    event.waitUntil((async () => {
      const cache = await caches.open(CACHE);
      const keys = await cache.keys();
      let bytes = null;
      try {
        const est = await navigator.storage.estimate();
        bytes = est && est.usage ? est.usage : null;
      } catch (e) { /* estimation indisponible */ }
      reply({ type: 'STATUS', count: keys.length, bytes: bytes });
    })());
  }
});

async function precache(urls, reply) {
  const cache = await caches.open(CACHE);
  const list = urls.map(u => abs(u));
  let done = 0;
  let failed = 0;
  const BATCH = 6;

  for (let i = 0; i < list.length; i += BATCH) {
    const slice = list.slice(i, i + BATCH);
    await Promise.all(slice.map(async u => {
      try {
        const res = await fetch(u, { cache: 'reload' });
        if (res && res.ok) await cache.put(u, res.clone());
        else failed += 1;
      } catch (e) {
        failed += 1;
      } finally {
        done += 1;
      }
    }));
    reply({ type: 'PRECACHE_PROGRESS', done: done, total: list.length, failed: failed });
  }

  let bytes = null;
  try {
    const est = await navigator.storage.estimate();
    bytes = est && est.usage ? est.usage : null;
  } catch (e) { /* ignore */ }
  reply({ type: 'PRECACHE_DONE', done: done, total: list.length, failed: failed, bytes: bytes });
}
