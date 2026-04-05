<script lang="ts">
  import Badge from '$lib/components/ui/Badge.svelte';
  import type { Article } from '$lib/types';

  export let article: Article;
  export let featured: boolean = false;

  function formatDate(iso: string) {
    return new Date(iso).toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
    });
  }

  const categoryLabels: Record<string, string> = {
    ai: 'Agentic AI',
    cybersecurity: 'Cybersecurity',
    business: 'Business',
  };
</script>

<article class="card" class:card--featured={featured}>
  {#if article.image_url}
    <a href="/article/{article.slug}" class="card-image-wrap" tabindex="-1" aria-hidden="true">
      <img
        src={article.image_url}
        alt={article.title}
        class="card-image"
        loading="lazy"
      />
    </a>
  {/if}

  <div class="card-body">
    <div class="card-meta-row">
      <Badge
        label={categoryLabels[article.category] ?? article.category}
        variant="accent"
      />
      <span class="card-date">{formatDate(article.published_at)}</span>
    </div>

    <a href="/article/{article.slug}" class="card-title-link">
      <h2 class="card-title">{article.title}</h2>
    </a>

    <p class="card-summary">{article.summary}</p>

    <div class="card-footer">
      <span class="card-source">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M13.19 8.688a4.5 4.5 0 011.242 7.244l-4.5 4.5a4.5 4.5 0 01-6.364-6.364l1.757-1.757m13.35-.622l1.757-1.757a4.5 4.5 0 00-6.364-6.364l-4.5 4.5a4.5 4.5 0 001.242 7.244"/>
        </svg>
        {article.source_name}
      </span>
      <a href="/article/{article.slug}" class="card-read-link">
        Read
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/>
        </svg>
      </a>
    </div>
  </div>
</article>

<style>
  .card {
    display: flex;
    flex-direction: column;
    background: var(--bg-surface);
    border: 1px solid var(--border);
    border-radius: calc(var(--radius) * 2);
    overflow: hidden;
    transition: border-color 0.2s, box-shadow 0.2s;
  }

  .card:hover {
    border-color: var(--accent);
    box-shadow: 0 4px 24px rgba(0,0,0,0.12);
  }

  .card--featured .card-title {
    font-size: 1.125rem;
  }

  .card-image-wrap {
    display: block;
    aspect-ratio: 16/9;
    overflow: hidden;
    background: var(--bg-muted);
  }

  .card-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
  }

  .card:hover .card-image {
    transform: scale(1.03);
  }

  .card-body {
    display: flex;
    flex-direction: column;
    gap: 0.625rem;
    padding: 1.125rem;
    flex: 1;
  }

  .card-meta-row {
    display: flex;
    align-items: center;
    gap: 0.625rem;
    flex-wrap: wrap;
  }

  .card-date {
    font-size: 0.75rem;
    color: var(--text-muted);
    font-family: var(--font-mono);
  }

  .card-title-link {
    text-decoration: none;
  }

  .card-title {
    font-size: 1rem;
    font-weight: 600;
    color: var(--text);
    line-height: 1.4;
    transition: color 0.15s;
  }

  .card-title-link:hover .card-title {
    color: var(--accent);
  }

  .card-summary {
    font-size: 0.875rem;
    color: var(--text-muted);
    line-height: 1.7;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    flex: 1;
  }

  .card-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.5rem;
    padding-top: 0.625rem;
    border-top: 1px solid var(--border);
    margin-top: auto;
  }

  .card-source {
    display: flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.75rem;
    color: var(--text-muted);
    font-family: var(--font-mono);
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .card-read-link {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.8125rem;
    font-weight: 600;
    color: var(--accent);
    text-decoration: none;
    white-space: nowrap;
    transition: gap 0.15s;
  }

  .card-read-link:hover { gap: 0.5rem; }
</style>
