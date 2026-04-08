<script lang="ts">
  import type { Category } from '$lib/types';

  export let categories: Category[] = [];
  export let active: string = 'all';
</script>

<div class="filter-bar">
  <a
    href="/"
    class="filter-chip"
    class:filter-chip--active={active === 'all'}
  >
    All
  </a>
  {#each categories as cat}
    
      href="/{cat.slug}"
      class="filter-chip"
      class:filter-chip--active={active === cat.slug}
    >
      {cat.label}
    </a>
  {/each}
</div>

<style>
  .filter-bar {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    padding-bottom: 1.5rem;
  }

  .filter-chip {
    display: inline-flex;
    align-items: center;
    padding: 0.375rem 0.875rem;
    font-size: 0.8125rem;
    font-weight: 500;
    border-radius: 9999px;
    border: 1px solid var(--border);
    background: var(--bg-surface);
    color: var(--text-muted);
    text-decoration: none;
    transition: all 0.15s;
  }

  .filter-chip:hover {
    border-color: var(--accent);
    color: var(--accent);
    background: var(--accent-dim);
  }

  .filter-chip--active {
    background: var(--accent);
    border-color: var(--accent);
    color: #fff;
  }

  .filter-chip--active:hover {
    color: #fff;
    background: var(--accent-hover);
  }
</style>
