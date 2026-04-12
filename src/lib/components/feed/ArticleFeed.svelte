<script lang="ts">
  import { goto } from '$app/navigation';
  import { page } from '$app/stores';
  import ArticleCard from './ArticleCard.svelte';
  import AdSlot from '$lib/components/ads/AdSlot.svelte';
  import type { PaginatedArticles } from '$lib/types';

  export let data: PaginatedArticles;

  // Derive currentPage from data itself — no more prop mismatch
  $: currentPage = data.page ?? 1;
  $: totalPages  = Math.ceil(data.total / data.per_page);

  let navigating = false;

  async function goTo(p: number) {
    if (p < 1 || p > totalPages || navigating) return;
    navigating = true;
    const params = new URLSearchParams($page.url.searchParams);
    params.set('page', String(p));
    await goto(`?${params.toString()}`, { keepFocus: true, noScroll: false });
    navigating = false;
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
</script>

{#if data.articles.length === 0}
  <div class="empty">
    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
      <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m9.303 3.376c.866 1.5-.217 3.374-1.948 3.374H4.645c-1.73 0-2.813-1.874-1.948-3.374L10.051 3.378c.866-1.5 3.032-1.5 3.898 0l7.354 12.748zM12 15.75h.007v.008H12v-.008z"/>
    </svg>
    <p>No articles found. Check back soon.</p>
  </div>
{:else}
  <div class="feed-grid" class:feed-grid--loading={navigating}>
    {#each data.articles as article, i (article.id)}
      <ArticleCard {article} />
      {#if (i + 1) % 6 === 0}
        <div class="feed-ad">
          <AdSlot slot="inline" />
        </div>
      {/if}
    {/each}
  </div>

  {#if data.total > data.per_page}
    <nav class="pagination" aria-label="Article pagination">

      <!-- Previous -->
      <button
        class="page-btn"
        class:page-btn--disabled={currentPage <= 1}
        disabled={currentPage <= 1 || navigating}
        on:click={() => goTo(currentPage - 1)}
        aria-label="Previous page"
      >
        {#if navigating && currentPage > 1}
          <span class="spinner" aria-hidden="true"></span>
        {:else}
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18"/>
          </svg>
        {/if}
        <span>Previous</span>
      </button>

      <!-- Page numbers -->
      <div class="page-numbers">
        {#each Array.from({ length: totalPages }, (_, i) => i + 1) as p}
          {#if totalPages <= 7 || p === 1 || p === totalPages || (p >= currentPage - 1 && p <= currentPage + 1)}
            <button
              class="page-num"
              class:page-num--active={p === currentPage}
              disabled={navigating}
              on:click={() => goTo(p)}
              aria-label="Page {p}"
              aria-current={p === currentPage ? 'page' : undefined}
            >
              {p}
            </button>
          {:else if p === currentPage - 2 || p === currentPage + 2}
            <span class="page-ellipsis">…</span>
          {/if}
        {/each}
      </div>

      <!-- Next -->
      <button
        class="page-btn"
        class:page-btn--disabled={!data.has_more}
        disabled={!data.has_more || navigating}
        on:click={() => goTo(currentPage + 1)}
        aria-label="Next page"
      >
        <span>Next</span>
        {#if navigating && data.has_more}
          <span class="spinner" aria-hidden="true"></span>
        {:else}
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/>
          </svg>
        {/if}
      </button>

    </nav>

    <p class="page-info" aria-live="polite">
      Page {currentPage} of {totalPages} — {data.total} articles
    </p>
  {/if}
{/if}

<style>
  .empty {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    padding: 4rem 2rem;
    color: var(--text-muted);
    text-align: center;
  }

  /* ── Grid ── */
  .feed-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.25rem;
    transition: opacity 0.2s ease;
  }

  .feed-grid--loading { opacity: 0.55; pointer-events: none; }

  .feed-ad { grid-column: 1 / -1; }

  /* ── Pagination ── */
  .pagination {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.625rem;
    padding-top: 2.5rem;
    flex-wrap: wrap;
  }

  .page-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.5rem 1.1rem;
    font-size: 0.875rem;
    font-weight: 600;
    border: 1px solid var(--border);
    border-radius: var(--radius);
    background: var(--bg-surface);
    color: var(--text);
    cursor: pointer;
    transition: all 0.15s;
    user-select: none;
  }

  .page-btn:hover:not(:disabled):not(.page-btn--disabled) {
    border-color: var(--accent);
    color: var(--accent);
    background: var(--accent-dim);
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(2,132,199,0.15);
  }

  .page-btn:active:not(:disabled) { transform: translateY(0); }

  .page-btn--disabled,
  .page-btn:disabled {
    opacity: 0.4;
    cursor: not-allowed;
    pointer-events: none;
  }

  /* ── Page numbers ── */
  .page-numbers {
    display: flex;
    align-items: center;
    gap: 0.3rem;
  }

  .page-num {
    width: 2.25rem;
    height: 2.25rem;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.875rem;
    font-weight: 500;
    border: 1px solid transparent;
    border-radius: var(--radius);
    background: none;
    color: var(--text-muted);
    cursor: pointer;
    transition: all 0.15s;
  }

  .page-num:hover:not(:disabled) {
    background: var(--bg-muted);
    color: var(--text);
    border-color: var(--border);
  }

  .page-num--active {
    background: var(--accent) !important;
    color: #fff !important;
    border-color: var(--accent) !important;
    font-weight: 700;
    cursor: default;
  }

  .page-num:disabled { opacity: 0.5; cursor: not-allowed; }

  .page-ellipsis {
    color: var(--text-muted);
    font-size: 0.875rem;
    padding: 0 0.1rem;
    user-select: none;
  }

  /* ── Info text ── */
  .page-info {
    text-align: center;
    font-size: 0.75rem;
    color: var(--text-muted);
    font-family: var(--font-mono);
    margin-top: 0.75rem;
  }

  /* ── Spinner ── */
  .spinner {
    display: inline-block;
    width: 14px;
    height: 14px;
    border: 2px solid var(--border);
    border-top-color: var(--accent);
    border-radius: 50%;
    animation: spin 0.65s linear infinite;
    flex-shrink: 0;
  }

  @keyframes spin { to { transform: rotate(360deg); } }

  /* ── Responsive ── */
  @media (max-width: 1024px) {
    .feed-grid { grid-template-columns: repeat(2, 1fr); }
  }

  @media (max-width: 640px) {
    .feed-grid { grid-template-columns: 1fr; }

    .page-btn { padding: 0.45rem 0.8rem; font-size: 0.8rem; }
    .page-num  { width: 2rem; height: 2rem; font-size: 0.8rem; }
  }

  @media (max-width: 380px) {
    .page-numbers { gap: 0.2rem; }
    .page-num { width: 1.75rem; height: 1.75rem; font-size: 0.75rem; }
  }
</style>
