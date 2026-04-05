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

    <a href="/" class="brand" on:click={closeMenu}>
      <div class="brand-icon">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z"/>
        </svg>
      </div>
      <span class="brand-name">MidMan<span class="brand-accent">Pulse</span></span>
    </a>

    <div class="nav-links" class:open={menuOpen}>
      <a href="/" class="nav-link" class:active={isActive('/')} on:click={closeMenu}>Home</a>
      {#each categories as cat}
        
          href="/{cat.slug}"
          class="nav-link"
          class:active={isActive(`/${cat.slug}`)}
          on:click={closeMenu}
        >
          {cat.label}
        </a>
      {/each}
    </div>

    <div class="nav-actions">
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
    gap: 1rem;
    height: 3.5rem;
  }

  .brand {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex-shrink: 0;
    text-decoration: none;
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
  }

  .brand-accent {
    color: var(--accent);
  }

  .nav-links {
    display: flex;
    align-items: center;
    gap: 0.25rem;
    margin-left: auto;
  }

  .nav-link {
    padding: 0.375rem 0.75rem;
    font-size: 0.875rem;
    font-weight: 500;
    color: var(--text-muted);
    border-radius: var(--radius);
    transition: color 0.15s, background 0.15s;
    text-decoration: none;
  }

  .nav-link:hover { color: var(--text); background: var(--bg-muted); }
  .nav-link.active { color: var(--accent); background: var(--accent-dim); }

  .nav-actions {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-left: 0.5rem;
    flex-shrink: 0;
  }

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
  }

  .theme-btn:hover { color: var(--text); background: var(--border); }

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
  }

  .hamburger:hover { color: var(--text); }

  @media (max-width: 768px) {
    .hamburger { display: flex; }

    .nav-links {
      display: none;
      position: absolute;
      top: 3.5rem;
      left: 0;
      right: 0;
      flex-direction: column;
      align-items: stretch;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border);
      padding: 0.5rem 1rem 0.75rem;
      gap: 0.25rem;
      margin-left: 0;
      box-shadow: 0 4px 16px rgba(0,0,0,0.15);
    }

    .nav-links.open { display: flex; }
    .nav-link { padding: 0.625rem 0.75rem; }
  }
</style>
