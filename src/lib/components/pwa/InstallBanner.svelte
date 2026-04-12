<script lang="ts">
  import { installable, updateReady, promptInstall, applyUpdate } from '$lib/pwa';

  let dismissed = false;

  function dismiss() { dismissed = true; }
</script>

<!-- Update banner — shown when a new version is available -->
{#if $updateReady}
  <div class="pwa-banner pwa-banner--update" role="alert">
    <div class="pwa-banner-text">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true">
        <path stroke-linecap="round" stroke-linejoin="round" d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99"/>
      </svg>
      <span>A new version of MidMan Pulse is ready.</span>
    </div>
    <button class="pwa-banner-btn pwa-banner-btn--primary" on:click={applyUpdate}>
      Update now
    </button>
  </div>
{/if}

<!-- Install banner — shown when PWA can be installed -->
{#if $installable && !dismissed}
  <div class="pwa-banner pwa-banner--install" role="complementary">
    <div class="pwa-banner-text">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true">
        <path stroke-linecap="round" stroke-linejoin="round" d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5M16.5 12L12 16.5m0 0L7.5 12m4.5 4.5V3"/>
      </svg>
      <span>Install MidMan Pulse for offline reading.</span>
    </div>
    <div class="pwa-banner-actions">
      <button class="pwa-banner-btn pwa-banner-btn--ghost" on:click={dismiss}>
        Not now
      </button>
      <button class="pwa-banner-btn pwa-banner-btn--primary" on:click={promptInstall}>
        Install
      </button>
    </div>
  </div>
{/if}

<style>
  .pwa-banner {
    position: fixed;
    bottom: 1rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 200;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    padding: 0.75rem 1rem;
    border-radius: calc(var(--radius) * 2);
    box-shadow: 0 4px 24px rgba(0,0,0,0.25);
    width: min(480px, calc(100vw - 2rem));
    animation: slide-up 0.3s ease both;
    flex-wrap: wrap;
  }

  @keyframes slide-up {
    from { opacity: 0; transform: translateX(-50%) translateY(1rem); }
    to   { opacity: 1; transform: translateX(-50%) translateY(0); }
  }

  .pwa-banner--update {
    background: var(--accent);
    border: 1px solid var(--accent-hover);
    color: #fff;
  }

  .pwa-banner--install {
    background: var(--bg-surface);
    border: 1px solid var(--border);
    color: var(--text);
  }

  .pwa-banner-text {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.875rem;
    font-weight: 500;
    flex: 1;
    min-width: 0;
  }

  .pwa-banner--install .pwa-banner-text { color: var(--text); }
  .pwa-banner--update  .pwa-banner-text { color: #fff; }

  .pwa-banner-actions {
    display: flex;
    gap: 0.5rem;
    align-items: center;
    flex-shrink: 0;
  }

  .pwa-banner-btn {
    padding: 0.4rem 0.875rem;
    border-radius: var(--radius);
    font-size: 0.8125rem;
    font-weight: 600;
    cursor: pointer;
    border: none;
    transition: all 0.15s;
    white-space: nowrap;
  }

  .pwa-banner-btn--primary {
    background: #fff;
    color: var(--accent);
  }

  .pwa-banner--update .pwa-banner-btn--primary:hover {
    background: #e0f2fe;
  }

  .pwa-banner-btn--ghost {
    background: transparent;
    color: var(--text-muted);
    border: 1px solid var(--border);
  }

  .pwa-banner-btn--ghost:hover {
    background: var(--bg-muted);
    color: var(--text);
  }

  @media (max-width: 480px) {
    .pwa-banner { bottom: 0; border-radius: calc(var(--radius) * 2) calc(var(--radius) * 2) 0 0; width: 100%; }
  }
</style>
