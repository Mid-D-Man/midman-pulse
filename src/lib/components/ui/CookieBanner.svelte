<script lang="ts">
  import { browser } from '$app/environment';
  import { onMount } from 'svelte';

  let visible = false;
  const STORAGE_KEY = 'mmp-cookies-accepted';

  onMount(() => {
    if (!localStorage.getItem(STORAGE_KEY)) {
      // Small delay so it doesn't flash immediately on load
      setTimeout(() => { visible = true; }, 800);
    }
  });

  function accept() {
    localStorage.setItem(STORAGE_KEY, '1');
    visible = false;
  }

  function decline() {
    // We don't set any non-essential cookies so declining is fine —
    // the theme pref just won't persist across sessions
    localStorage.setItem(STORAGE_KEY, '0');
    visible = false;
  }
</script>

{#if visible}
  <div class="cookie-banner" role="dialog" aria-label="Cookie notice" aria-live="polite">
    <div class="cookie-inner">
      <div class="cookie-text">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" class="cookie-icon">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m9.303 3.376c.866 1.5-.217 3.374-1.948 3.374H4.645c-1.73 0-2.813-1.874-1.948-3.374L10.051 3.378c.866-1.5 3.032-1.5 3.898 0l7.354 12.748zM12 15.75h.007v.008H12v-.008z"/>
        </svg>
        <p>
          We use minimal browser storage — just to remember your light/dark preference. No tracking, no ads cookies.
          <a href="/cookies">Learn more</a>
        </p>
      </div>
      <div class="cookie-actions">
        <button class="cookie-btn cookie-btn--ghost" on:click={decline}>
          Decline
        </button>
        <button class="cookie-btn cookie-btn--primary" on:click={accept}>
          Got it
        </button>
      </div>
    </div>
  </div>
{/if}

<style>
  .cookie-banner {
    position: fixed;
    bottom: 1.25rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 300;
    width: min(560px, calc(100vw - 2rem));
    background: var(--bg-surface);
    border: 1px solid var(--border);
    border-radius: calc(var(--radius) * 2);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    animation: slide-up 0.35s cubic-bezier(0.16, 1, 0.3, 1) both;
  }

  @keyframes slide-up {
    from { opacity: 0; transform: translateX(-50%) translateY(1.5rem); }
    to   { opacity: 1; transform: translateX(-50%) translateY(0); }
  }

  .cookie-inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    padding: 1rem 1.25rem;
    flex-wrap: wrap;
  }

  .cookie-text {
    display: flex;
    align-items: flex-start;
    gap: 0.625rem;
    flex: 1;
    min-width: 0;
  }

  .cookie-icon {
    color: var(--accent);
    flex-shrink: 0;
    margin-top: 0.1rem;
  }

  .cookie-text p {
    font-size: 0.8125rem;
    color: var(--text-muted);
    line-height: 1.6;
    margin: 0;
  }

  .cookie-text a {
    color: var(--accent);
    text-decoration: underline;
    text-underline-offset: 2px;
    transition: color 0.15s;
  }

  .cookie-text a:hover { color: var(--accent-hover); }

  .cookie-actions {
    display: flex;
    gap: 0.5rem;
    flex-shrink: 0;
    align-items: center;
  }

  .cookie-btn {
    padding: 0.45rem 1rem;
    border-radius: var(--radius);
    font-size: 0.8125rem;
    font-weight: 600;
    cursor: pointer;
    border: none;
    transition: all 0.15s;
    white-space: nowrap;
  }

  .cookie-btn--primary {
    background: var(--accent);
    color: #fff;
  }

  .cookie-btn--primary:hover {
    background: var(--accent-hover);
    transform: translateY(-1px);
  }

  .cookie-btn--ghost {
    background: transparent;
    color: var(--text-muted);
    border: 1px solid var(--border);
  }

  .cookie-btn--ghost:hover {
    background: var(--bg-muted);
    color: var(--text);
  }

  @media (max-width: 480px) {
    .cookie-banner {
      bottom: 0;
      border-radius: calc(var(--radius) * 2) calc(var(--radius) * 2) 0 0;
      width: 100%;
    }
    .cookie-inner  { flex-direction: column; align-items: stretch; }
    .cookie-actions { justify-content: flex-end; }
  }
</style>
