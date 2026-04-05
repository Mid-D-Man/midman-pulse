<script lang="ts">
  import ArticleFeed from '$lib/components/feed/ArticleFeed.svelte';
  import CategoryFilter from '$lib/components/feed/CategoryFilter.svelte';
  import AdSlot from '$lib/components/ads/AdSlot.svelte';
  import type { Category, PaginatedArticles } from '$lib/types';

  export let data: {
    articles: PaginatedArticles;
    category: Category;
    categories: Category[];
    currentPage: number;
  };
</script>

<svelte:head>
  <title>{data.category.label} — MidMan Pulse</title>
  <meta name="description" content={data.category.description ?? `Latest ${data.category.label} news and analysis.`} />
</svelte:head>

<div class="category-page">
  <div class="container">

    <header class="category-header">
      <div class="category-label-row">
        <span class="category-kicker">Category</span>
      </div>
      <h1 class="category-title">{data.category.label}</h1>
      {#if data.category.description}
        <p class="category-desc">{data.category.description}</p>
      {/if}
    </header>

    <AdSlot slot="banner" />

    <div class="category-body">
      <div class="feed-col">
        <CategoryFilter categories={data.categories} active={data.category.slug} />
        <ArticleFeed data={data.articles} currentPage={data.currentPage} />
      </div>
      <aside class="sidebar">
        <div class="sidebar-sticky">
          <AdSlot slot="sidebar" />
        </div>
      </aside>
    </div>

  </div>
</div>

<style>
  .category-page {
    padding: 2.5rem 0 4rem;
  }

  .category-header {
    margin-bottom: 2rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--border);
  }

  .category-label-row {
    margin-bottom: 0.5rem;
  }

  .category-kicker {
    font-size: 0.6875rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--accent);
    font-family: var(--font-mono);
  }

  .category-title {
    font-size: clamp(1.75rem, 4vw, 2.5rem);
    font-weight: 700;
    color: var(--text);
    line-height: 1.2;
    margin-bottom: 0.5rem;
  }

  .category-desc {
    font-size: 1rem;
    color: var(--text-muted);
    max-width: 600px;
    line-height: 1.7;
  }

  .category-body {
    display: grid;
    grid-template-columns: 1fr 300px;
    gap: 2rem;
    align-items: start;
    margin-top: 1.5rem;
  }

  .sidebar-sticky {
    position: sticky;
    top: 5rem;
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
  }

  @media (max-width: 1024px) {
    .category-body {
      grid-template-columns: 1fr;
    }

    .sidebar { display: none; }
  }
</style>
