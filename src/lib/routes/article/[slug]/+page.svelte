<script lang="ts">
  import Badge from '$lib/components/ui/Badge.svelte';
  import ArticleCard from '$lib/components/feed/ArticleCard.svelte';
  import AdSlot from '$lib/components/ads/AdSlot.svelte';
  import type { Article } from '$lib/types';

  export let data: {
    article: Article;
    tags: string[];
    related: Article[];
  };

  const { article, tags, related } = data;

  function formatDate(iso: string) {
    return new Date(iso).toLocaleDateString('en-US', {
      weekday: 'long', month: 'long', day: 'numeric', year: 'numeric',
    });
  }

  const categoryLabels: Record<string, string> = {
    ai:            'Agentic AI',
    cybersecurity: 'Cybersecurity',
    business:      'Business',
    gamedev:       'Game Dev',
  };
</script>

<svelte:head>
  <title>{article.title} — MidMan Pulse</title>
  <meta name="description" content={article.summary} />
  {#if article.image_url}
    <meta property="og:image" content={article.image_url} />
  {/if}
</svelte:head>

<div class="article-page">
  <div class="container">
    <div class="article-layout">

      <article class="article-main">
        <header class="article-header">
          <div class="article-meta-row">
            <Badge label={categoryLabels[article.category] ?? article.category} variant="accent" />
            <span class="article-date">{formatDate(article.published_at)}</span>
          </div>
          <h1 class="article-title">{article.title}</h1>
          <p class="article-summary">{article.summary}</p>
          <div class="article-source-row">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M13.19 8.688a4.5 4.5 0 011.242 7.244l-4.5 4.5a4.5 4.5 0 01-6.364-6.364l1.757-1.757m13.35-.622l1.757-1.757a4.5 4.5 0 00-6.364-6.364l-4.5 4.5a4.5 4.5 0 001.242 7.244"/>
            </svg>
            <span>Source:</span>
            <a href={article.source_url} target="_blank" rel="noopener noreferrer" class="article-source-link">
              {article.source_name}
            </a>
          </div>
        </header>

        {#if article.image_url}
          <div class="article-image-wrap">
            <img src={article.image_url} alt={article.title} class="article-image" />
          </div>
        {/if}

        <AdSlot slot="inline" />

        {#if article.content}
          <div class="article-content prose">{@html article.content}</div>
        {:else}
          <div class="article-no-content">
            <p>Read the full article at the source.</p>
            <a href={article.source_url} target="_blank" rel="noopener noreferrer" class="source-btn">
              Read on {article.source_name}
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 6H5.25A2.25 2.25 0 003 8.25v10.5A2.25 2.25 0 005.25 21h10.5A2.25 2.25 0 0018 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25"/>
              </svg>
            </a>
          </div>
        {/if}

        {#if tags.length > 0}
          <div class="article-tags">
            {#each tags as tag}
              <span class="tag">{tag}</span>
            {/each}
          </div>
        {/if}
      </article>

      <aside class="article-sidebar">
        <div class="sidebar-sticky">
          <AdSlot slot="sidebar" />
        </div>
      </aside>
    </div>

    {#if related.length > 0}
      <section class="related-section">
        <h2 class="related-title">Related Articles</h2>
        <div class="related-grid">
          {#each related as rel (rel.id)}
            <ArticleCard article={rel} />
          {/each}
        </div>
      </section>
    {/if}
  </div>
</div>

<style>
  .article-page { padding: 2.5rem 0 4rem; }

  .article-layout {
    display: grid;
    grid-template-columns: 1fr 300px;
    gap: 2rem;
    align-items: start;
  }

  .article-header {
    margin-bottom: 1.75rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    gap: 0.875rem;
  }

  .article-meta-row {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    flex-wrap: wrap;
  }

  .article-date { font-size: 0.8125rem; color: var(--text-muted); font-family: var(--font-mono); }

  .article-title {
    font-size: clamp(1.5rem, 4vw, 2.25rem);
    font-weight: 700;
    color: var(--text);
    line-height: 1.25;
  }

  .article-summary { font-size: 1.0625rem; color: var(--text-muted); line-height: 1.75; }

  .article-source-row {
    display: flex;
    align-items: center;
    gap: 0.375rem;
    font-size: 0.875rem;
    color: var(--text-muted);
  }

  .article-source-link { color: var(--accent); text-decoration: underline; text-underline-offset: 2px; }

  .article-image-wrap {
    margin-bottom: 1.5rem;
    border-radius: calc(var(--radius) * 2);
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .article-image { width: 100%; display: block; aspect-ratio: 16/9; object-fit: cover; }

  .article-content { margin-top: 1.5rem; font-size: 0.9375rem; line-height: 1.8; color: var(--text); }

  .article-no-content {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
    padding: 2rem;
    background: var(--bg-muted);
    border: 1px solid var(--border);
    border-radius: calc(var(--radius) * 2);
    margin-top: 1.5rem;
  }

  .article-no-content p { font-size: 0.9375rem; color: var(--text-muted); }

  .source-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.375rem;
    padding: 0.625rem 1.25rem;
    background: var(--accent);
    color: #fff;
    border-radius: var(--radius);
    font-size: 0.875rem;
    font-weight: 600;
    text-decoration: none;
    transition: background 0.15s;
  }

  .source-btn:hover { background: var(--accent-hover); }

  .article-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 2rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--border);
  }

  .tag {
    display: inline-flex;
    align-items: center;
    padding: 0.25rem 0.75rem;
    font-size: 0.75rem;
    font-family: var(--font-mono);
    background: var(--bg-muted);
    border: 1px solid var(--border);
    border-radius: 9999px;
    color: var(--text-muted);
  }

  .article-sidebar .sidebar-sticky { position: sticky; top: 5rem; }

  .related-section { margin-top: 3rem; padding-top: 2rem; border-top: 1px solid var(--border); }
  .related-title { font-size: 1.125rem; font-weight: 700; color: var(--text); margin-bottom: 1.25rem; }

  .related-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.25rem;
  }

  /* Tablet */
  @media (max-width: 1024px) {
    .article-layout { grid-template-columns: 1fr; }
    .article-sidebar { display: none; }
    .related-grid { grid-template-columns: repeat(2, 1fr); }
  }

  /* Mobile */
  @media (max-width: 640px) {
    .article-page { padding: 1.5rem 0 3rem; }
    .related-grid { grid-template-columns: 1fr; }
  }
</style>
