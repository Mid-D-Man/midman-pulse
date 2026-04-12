import { browser } from '$app/environment';
import { writable } from 'svelte/store';

/** True when the browser fires beforeinstallprompt */
export const installable  = writable(false);
/** True when a new SW version is waiting */
export const updateReady  = writable(false);

let deferredPrompt: any = null;
let waitingWorker: ServiceWorker | null = null;

export function registerSW() {
  if (!browser || !('serviceWorker' in navigator)) return;

  // ── Register ──────────────────────────────────────────────
  navigator.serviceWorker.register('/sw.js', { scope: '/' }).then((reg) => {

    // Check for waiting worker on load
    if (reg.waiting) {
      waitingWorker = reg.waiting;
      updateReady.set(true);
    }

    // New SW installed and waiting
    reg.addEventListener('updatefound', () => {
      const newWorker = reg.installing;
      if (!newWorker) return;
      newWorker.addEventListener('statechange', () => {
        if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
          waitingWorker = newWorker;
          updateReady.set(true);
        }
      });
    });

  }).catch((err) => {
    console.warn('SW registration failed:', err);
  });

  // ── Install prompt ─────────────────────────────────────────
  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    installable.set(true);
  });

  window.addEventListener('appinstalled', () => {
    installable.set(false);
    deferredPrompt = null;
  });
}

/** Call this when user clicks your install button */
export async function promptInstall() {
  if (!deferredPrompt) return;
  deferredPrompt.prompt();
  const { outcome } = await deferredPrompt.userChoice;
  if (outcome === 'accepted') installable.set(false);
  deferredPrompt = null;
}

/** Call this when user clicks your update button */
export function applyUpdate() {
  if (!waitingWorker) return;
  waitingWorker.postMessage({ type: 'SKIP_WAITING' });
  waitingWorker = null;
  updateReady.set(false);
  window.location.reload();
  }
