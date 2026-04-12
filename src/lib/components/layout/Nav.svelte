<script lang="ts">
  import { page } from '$app/stores';
  import { theme } from '$lib/stores/theme';
  import type { Category } from '$lib/types';

  export let categories: Category[] = [];

  let menuOpen = false;

  function isActive(href: string) {
    if (href === '/') return $page.url.pathname === '/';
    return $page.url.pathname.startsWith(href);
  }

  function closeMenu() { menuOpen = false; }
</script>

<nav class="nav">
  <div class="nav-inner container">

    <!-- FAR LEFT: logo -->
    <a href="/" class="brand" on:click={closeMenu}>
      <div class="brand-icon" aria-hidden="true">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z"/>
        </svg>
      </div>
      <span class="brand-name">MidMan<span class="brand-accent">Pulse</span></span>
    </a>

    <!-- MIDDLE: nav links (desktop) -->
    <div class="nav-links">
      <a href="/" class="nav-link" class:active={isActive('/')}>Home</a>
      {#each categories as cat}
        <a
          href="/{cat.slug}"
          class="nav-link"
          class:active={isActive(`/${cat.slug}`)}
        >
          {cat.label}
        </a>
      {/each}
    </div>

    <!-- FAR RIGHT: MMS CTA + theme + hamburger -->
    <div class="nav-actions">

      <!-- MMS Accounts CTA — always visible on desktop -->
      <a
        href="https://mms-accounts.pages.dev"
        class="nav-mms-btn"
        target="_blank"
        rel="noopener noreferrer"
        title="MidManStudio Accounts — your free studio identity"
      >
        <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M13 10V3L4 14h7v7l9-11h-7z"/>
        </svg>
        <span class="nav-mms-text">Get your MmS ID</span>
      </a>

      <button class="theme-btn" on:click={theme.toggle} aria-label="Toggle theme">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.718 9.718 0 0118 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 003 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 009.002-5.998z"/>
        </svg>
      </button>

      <button
        class="hamburger"
        on:click={() => (menuOpen = !menuOpen)}
        aria-label={menuOpen ? 'Close menu' : 'Open menu'}
        aria-expanded={menuOpen}
      >
        {#if menuOpen}
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        {:else}
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"/>
          </svg>
        {/if}
      </button>
    </div>

  </div>

  <!-- Mobile dropdown -->
  {#if menuOpen}
    <div class="mobile-menu">
      <a href="/" class="mobile-link" class:active={isActive('/')} on:click={closeMenu}>Home</a>
      {#each categories as cat}
        <a
          href="/{cat.slug}"
          class="mobile-link"
          class:active={isActive(`/${cat.slug}`)}
          on:click={closeMenu}
        >
          {cat.label}
        </a>
      {/each}

      <!-- MMS CTA in mobile menu too -->
      <div class="mobile-divider" aria-hidden="true"></div>
      <a
        href="https://mms-accounts.pages.dev"
        class="mobile-mms-btn"
        target="_blank"
        rel="noopener noreferrer"
        on:click={closeMenu}
      >
        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M13 10V3L4 14h7v7l9-11h-7z"/>
        </svg>
        Get your free MmS ID
      </a>
    </div>
  {/if}
</nav>

<style>
  .nav {
    position: sticky;
    top: 0;
    z-index: 100;
    background: var(--bg-surface);
    border-bottom: 1px solid var(--border);
    backdrop-filter: blur(8px);
  }

  .nav-inner {
    display: flex;
    align-items: center;
    height: 3.5rem;
    gap: 0.75rem;
  }

  /* ── Brand ── */
  .brand {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex-shrink: 0;
    text-decoration: none;
    margin-right: auto;
  }

  .brand-icon {
    width: 2rem;
    height: 2rem;
    background: var(--accent);
    color: #fff;
    border-radius: var(--radius);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  .brand-name {
    font-size: 1rem;
    font-weight: 700;
    color: var(--text);
    letter-spacing: -0.01em;
    white-space: nowrap;
  }

  .brand-accent { color: var(--accent); }

  /* ── Desktop nav links ── */
  .nav-links {
    display: flex;
    align-items: center;
    gap: 0.125rem;
  }

  .nav-link {
    padding: 0.375rem 0.7rem;
    font-size: 0.875rem;
    font-weight: 500;
    color: var(--text-muted);
    border-radius: var(--radius);
    transition: color 0.15s, background 0.15s;
    text-decoration: none;
    white-space: nowrap;
  }

  .nav-link:hover  { color: var(--text); background: var(--bg-muted); }
  .nav-link.active { color: var(--accent); background: var(--accent-dim); }

  /* ── Actions row ── */
  .nav-actions {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex-shrink: 0;
  }

  /* ── MMS CTA button ── */
  .nav-mms-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.375rem;
    padding: 0.4rem 0.875rem;
    background: var(--accent);
    color: #fff;
    border-radius: var(--radius);
    font-size: 0.8125rem;
    font-weight: 600;
    text-decoration: none;
    white-space: nowrap;
    transition: background 0.15s, transform 0.15s, box-shadow 0.15s;
    letter-spacing: -0.01em;
  }

  .nav-mms-btn:hover {
    background: var(--accent-hover);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3);
  }

  .nav-mms-btn:active { transform: translateY(0); }

  /* ── Theme button ── */
  .theme-btn {
    width: 2rem;
    height: 2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--bg-muted);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    color: var(--text-muted);
    cursor: pointer;
    transition: color 0.15s, background 0.15s;
    flex-shrink: 0;
  }

  .theme-btn:hover { color: var(--text); background: var(--border); }

  /* ── Hamburger ── */
  .hamburger {
    display: none;
    width: 2rem;
    height: 2rem;
    align-items: center;
    justify-content: center;
    background: var(--bg-muted);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    color: var(--text-muted);
    cursor: pointer;
    transition: color 0.15s;
    flex-shrink: 0;
  }

  .hamburger:hover { color: var(--text); }

  /* ── Mobile dropdown ── */
  .mobile-menu {
    display: flex;
    flex-direction: column;
    background: var(--bg-surface);
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    padding: 0.5rem 1rem 1rem;
    gap: 0.25rem;
    box-shadow: 0 4px 16px rgba(0,0,0,0.15);
  }

  .mobile-link {
    padding: 0.625rem 0.75rem;
    font-size: 0.9375rem;
    font-weight: 500;
    color: var(--text-muted);
    border-radius: var(--radius);
    text-decoration: none;
    transition: color 0.15s, background 0.15s;
  }

  .mobile-link:hover  { color: var(--text); background: var(--bg-muted); }
  .mobile-link.active { color: var(--accent); background: var(--accent-dim); }

  .mobile-divider {
    height: 1px;
    background: var(--border);
    margin: 0.5rem 0;
  }

  .mobile-mms-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1rem;
    background: var(--accent);
    color: #fff;
    border-radius: var(--radius);
    font-size: 0.9375rem;
    font-weight: 600;
    text-decoration: none;
    transition: background 0.15s;
    justify-content: center;
    margin-top: 0.25rem;
  }

  .mobile-mms-btn:hover { background: var(--accent-hover); }

  /* ── Breakpoints ── */
  @media (max-width: 900px) {
    /* Hide text label on smaller screens, keep icon + compact button */
    .nav-mms-text { display: none; }
    .nav-mms-btn  { padding: 0.4rem 0.6rem; }
  }

  @media (max-width: 768px) {
    .hamburger { display: flex; }
    .nav-links  { display: none; }
    /* Show full text in mobile menu — hide desktop button text is already gone */
  }

  @media (max-width: 380px) {
    .brand-name { font-size: 0.875rem; }
    .brand-icon { width: 1.75rem; height: 1.75rem; }
  }
</style>
