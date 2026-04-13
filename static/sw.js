/**
 * MidMan Pulse — Service Worker
 * Strategy:
 *   - App shell (HTML, CSS, JS, fonts) → Cache First
 *   - API / article pages              → Network First with cache fallback
 *   - Images                           → Cache First with network fallback
 */

const VERSION      = 'v1';
const SHELL_CACHE  = `mmp-shell-${VERSION}`;
const PAGES_CACHE  = `mmp-pages-${VERSION}`;
const IMAGES_CACHE = `mmp-images-${VERSION}`;

const SHELL_ASSETS = [
  '/',
  '/offline',
  '/manifest.json',
];

// ── Install: cache shell assets ───────────────────────────────
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(SHELL_CACHE).then((cache) =>
      cache.addAll(SHELL_ASSETS)
    ).then(() => self.skipWaiting())
  );
});

// ── Activate: purge old caches ────────────────────────────────
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys
          .filter((k) => ![SHELL_CACHE, PAGES_CACHE, IMAGES_CACHE].includes(k))
          .map((k) => caches.delete(k))
      )
    ).then(() => self.clients.claim())
  );
});

// ── Message: skip waiting (triggered by applyUpdate()) ────────
self.addEventListener('message', (event) => {
  if (event.data?.type === 'SKIP_WAITING') self.skipWaiting();
});

// ── Fetch ─────────────────────────────────────────────────────
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);

  if (request.method !== 'GET') return;
  if (url.origin !== self.location.origin) return;

  // Images → cache first
  if (request.destination === 'image') {
    event.respondWith(cacheFirst(request, IMAGES_CACHE));
    return;
  }

  // Static assets (JS, CSS, fonts, icons) → cache first
  if (
    url.pathname.startsWith('/_app/') ||
    url.pathname.startsWith('/icons/') ||
    url.pathname.endsWith('.js') ||
    url.pathname.endsWith('.css') ||
    url.pathname.endsWith('.woff2')
  ) {
    event.respondWith(cacheFirst(request, SHELL_CACHE));
    return;
  }

  // HTML pages → network first with offline fallback
  if (request.headers.get('accept')?.includes('text/html')) {
    event.respondWith(networkFirst(request, PAGES_CACHE));
    return;
  }
});

// ── Strategies ────────────────────────────────────────────────

async function cacheFirst(request, cacheName) {
  const cache  = await caches.open(cacheName);
  const cached = await cache.match(request);
  if (cached) return cached;

  try {
    const response = await fetch(request);
    if (response.ok) cache.put(request, response.clone());
    return response;
  } catch {
    return new Response('Offline', { status: 503 });
  }
}

async function networkFirst(request, cacheName) {
  const cache = await caches.open(cacheName);
  try {
    const response = await fetch(request);
    if (response.ok) cache.put(request, response.clone());
    return response;
  } catch {
    const cached = await cache.match(request);
    if (cached) return cached;
    const offline = await caches.match('/offline');
    return offline ?? new Response('You are offline', { status: 503 });
  }
}
