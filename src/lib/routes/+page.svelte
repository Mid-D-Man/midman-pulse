<script lang="ts">
  import EditorialSection from '$lib/components/feed/EditorialSection.svelte';
  import ArticleFeed from '$lib/components/feed/ArticleFeed.svelte';
  import ArticleCard from '$lib/components/feed/ArticleCard.svelte';
  import Newsletter from '$lib/components/layout/Newsletter.svelte';
  import type { Article, PaginatedArticles } from '$lib/types';

  export let data: {
    featured: Article[];
    recent: PaginatedArticles;
  };
</script>

<svelte:head>
  <title>MidMan Pulse — AI, Cybersecurity &amp; Business Intelligence</title>
  <meta name="description" content="Curated intelligence on agentic AI, cybersecurity threats, and profit-driven business tools. Updated every few hours." />
</svelte:head>

<div class="home">

  <!-- Your own articles — always pinned at the very top -->
  <div class="container">
    <EditorialSection />
  </div>

  <!-- Scraped featured articles -->
  {#if data.featured.length > 0}
    <section class="featured-section">
      <div class="container">
        <div class="section-header">
          <span class="section-label">Featured</span>
        </div>
        <div class="featured-grid">
          {#each data.featured as article (article.id)}
            <ArticleCard {article} featured />
          {/each}
        </div>
      </div>
    </section>
  {/if}

  <!-- Main feed -->
  <section class="feed-section">
    <div class="container">
      <div class="section-header">
        <span class="section-label">Latest</span>
      </div>
      <ArticleFeed data={data.recent} />
    </div>
  </section>

  <!-- Newsletter -->
  <section class="newsletter-section">
    <div class="container">
      <Newsletter />
    </div>
  </section>

</div>

<style>
  .home { padding-bottom: 4rem; }

  .featured-section {
    padding: 2.5rem 0 2rem;
    border-bottom: 1px solid var(--border);
    background: var(--bg-surface);
  }

  .feed-section     { padding: 2.5rem 0; }
  .newsletter-section { padding: 0 0 2rem; }

  .section-header { margin-bottom: 1.25rem; }

  .section-label {
    font-size: 0.6875rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--accent);
    font-family: var(--font-mono);
  }

  .featured-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.25rem;
  }

  @media (max-width: 1024px) {
    .featured-grid { grid-template-columns: repeat(2, 1fr); }
  }

  @media (max-width: 640px) {
    .featured-grid { grid-template-columns: 1fr; }
  }
</style>
