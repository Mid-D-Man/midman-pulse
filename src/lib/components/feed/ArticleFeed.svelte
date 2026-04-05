<script lang="ts">
  import ArticleCard from './ArticleCard.svelte';
  import AdSlot from '$lib/components/ads/AdSlot.svelte';
  import type { PaginatedArticles } from '$lib/types';

  export let data: PaginatedArticles;
  export let currentPage: number = 1;
</script>

{#if data.articles.length === 0}
  <div class="empty">
    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
      <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m9.303 3.376c.866 1.5-.217 3.374-1.948 3.374H4.645c-1.73 0-2.813-1.874-1.948-3.374L10.051 3.378c.866-1.5 3.032-1.5 3.898 0l7.354 12.748zM12 15.75h.007v.008H12v-.008z"/>
    </svg>
    <p>No articles found. Check back soon.</p>
  </div>
{:else}
  <div class="feed-grid">
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
    <div class="pagination">
      {#if currentPage > 1}
        <a href="?page={currentPage - 1}" class="page-btn">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18"/>
          </svg>
          Previous
        </a>
      {/if}
      <span class="page-info">
        Page {currentPage} of {Math.ceil(data.total / data.per_page)}
      </span>
      {#if data.has_more}
        <a href="?page={currentPage + 1}" class="page-btn">
          Next
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/>
          </svg>
        </a>
      {/if}
    </div>
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

  .feed-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.25rem;
  }

  .feed-ad {
    grid-column: 1 / -1;
  }

  .pagination {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    padding-top: 2.5rem;
  }

  .page-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.375rem;
    padding: 0.5rem 1rem;
    font-size: 0.875rem;
    font-weight: 600;
    border: 1px solid var(--border);
    border-radius: var(--radius);
    background: var(--bg-surface);
    color: var(--text);
    text-decoration: none;
    transition: all 0.15s;
  }

  .page-btn:hover {
    border-color: var(--accent);
    color: var(--accent);
    background: var(--accent-dim);
  }

  .page-info {
    font-size: 0.8125rem;
    color: var(--text-muted);
    font-family: var(--font-mono);
  }

  @media (max-width: 1024px) {
    .feed-grid { grid-template-columns: repeat(2, 1fr); }
  }

  @media (max-width: 640px) {
    .feed-grid { grid-template-columns: 1fr; }
  }
</style>
