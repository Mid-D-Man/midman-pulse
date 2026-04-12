<script lang="ts">
  import type { EditorialArticle } from '$lib/editorial';

  export let article: EditorialArticle;

  const CATEGORY_META: Record<string, { label: string; colour: string }> = {
    announcement: { label: 'Announcement', colour: 'var(--accent)' },
    tool:         { label: 'Tool',         colour: '#8b5cf6' },
    game:         { label: 'Game',         colour: '#f59e0b' },
    guide:        { label: 'Guide',        colour: '#10b981' },
    update:       { label: 'Update',       colour: '#6366f1' },
    project:      { label: 'Project',      colour: '#ec4899' },
  };

  $: meta      = CATEGORY_META[article.category] ?? { label: article.category, colour: 'var(--accent)' };
  $: source    = article.source ?? 'MidManStudio';
  $: cta       = article.cta    ?? 'Read more';
  $: tag       = article.external ? { target: '_blank', rel: 'noopener noreferrer' } : {};

  function formatDate(iso?: string) {
    if (!iso) return '';
    return new Date(iso).toLocaleDateString('en-US', {
      month: 'short', day: 'numeric', year: 'numeric',
    });
  }
</script>

<article class="editorial-card">

  <!-- Left: image (optional) -->
  {#if article.image_url}
    
      href={article.link}
      class="editorial-image-wrap"
      {...tag}
      tabindex="-1"
      aria-hidden="true"
    >
      <img
        src={article.image_url}
        alt={article.title}
        class="editorial-image"
        loading="lazy"
      />
    </a>
  {/if}

  <!-- Right: content -->
  <div class="editorial-body" class:editorial-body--no-image={!article.image_url}>

    <!-- Top row: studio badge + category chip + date -->
    <div class="editorial-meta">
      <span class="editorial-studio-badge">
        <svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor">
          <path d="M13 10V3L4 14h7v7l9-11h-7z"/>
        </svg>
        MidManStudio
      </span>
      <span
        class="editorial-category"
        style="background: {meta.colour}22; color: {meta.colour}; border-color: {meta.colour}55;"
      >
        {meta.label}
      </span>
      {#if article.date}
        <span class="editorial-date">{formatDate(article.date)}</span>
      {/if}
    </div>

    <!-- Title -->
    <a href={article.link} class="editorial-title-link" {...tag}>
      <h2 class="editorial-title">{article.title}</h2>
    </a>

    <!-- Summary -->
    <p class="editorial-summary">{article.summary}</p>

    <!-- Footer: source + CTA -->
    <div class="editorial-footer">
      <span class="editorial-source">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10"/>
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3"/>
        </svg>
        {source}
      </span>
      <a href={article.link} class="editorial-cta" {...tag}>
        {cta}
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/>
        </svg>
      </a>
    </div>

  </div>

</article>

<style>
  .editorial-card {
    display: flex;
    gap: 1.5rem;
    background: var(--bg-surface);
    border: 1px solid var(--accent);
    border-left: 3px solid var(--accent);
    border-radius: calc(var(--radius) * 2);
    overflow: hidden;
    transition: box-shadow 0.2s, transform 0.2s;
    position: relative;
  }

  /* Subtle glow on hover to make them feel premium */
  .editorial-card:hover {
    box-shadow: 0 4px 32px rgba(2, 132, 199, 0.18);
    transform: translateY(-2px);
  }

  /* ── Image ── */
  .editorial-image-wrap {
    flex-shrink: 0;
    width: 220px;
    min-height: 140px;
    overflow: hidden;
    background: var(--bg-muted);
    display: block;
  }

  .editorial-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
  }

  .editorial-card:hover .editorial-image { transform: scale(1.04); }

  /* ── Body ── */
  .editorial-body {
    display: flex;
    flex-direction: column;
    gap: 0.625rem;
    padding: 1.25rem 1.25rem 1.25rem 0;
    flex: 1;
    min-width: 0;
  }

  .editorial-body--no-image { padding-left: 1.25rem; }

  /* ── Meta row ── */
  .editorial-meta {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex-wrap: wrap;
  }

  .editorial-studio-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.6rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-family: var(--font-mono);
    color: var(--accent);
    background: var(--accent-dim);
    border: 1px solid var(--accent);
    border-radius: 9999px;
    padding: 0.2rem 0.55rem;
  }

  .editorial-category {
    display: inline-flex;
    align-items: center;
    font-size: 0.6rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-family: var(--font-mono);
    border: 1px solid;
    border-radius: 9999px;
    padding: 0.2rem 0.55rem;
  }

  .editorial-date {
    font-size: 0.75rem;
    color: var(--text-muted);
    font-family: var(--font-mono);
    margin-left: auto;
  }

  /* ── Title ── */
  .editorial-title-link { text-decoration: none; }

  .editorial-title {
    font-size: 1.0625rem;
    font-weight: 700;
    color: var(--text);
    line-height: 1.4;
    transition: color 0.15s;
  }

  .editorial-title-link:hover .editorial-title { color: var(--accent); }

  /* ── Summary ── */
  .editorial-summary {
    font-size: 0.875rem;
    color: var(--text-muted);
    line-height: 1.7;
    flex: 1;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  /* ── Footer ── */
  .editorial-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.75rem;
    padding-top: 0.625rem;
    border-top: 1px solid var(--border);
    margin-top: auto;
  }

  .editorial-source {
    display: flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.75rem;
    color: var(--text-muted);
    font-family: var(--font-mono);
  }

  .editorial-cta {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    font-size: 0.8125rem;
    font-weight: 700;
    color: var(--accent);
    text-decoration: none;
    white-space: nowrap;
    transition: gap 0.15s;
  }

  .editorial-cta:hover { gap: 0.55rem; }

  /* ── Responsive ── */
  @media (max-width: 640px) {
    .editorial-card { flex-direction: column; }

    .editorial-image-wrap {
      width: 100%;
      min-height: 180px;
      aspect-ratio: 16/9;
    }

    .editorial-body,
    .editorial-body--no-image {
      padding: 1rem;
    }

    .editorial-date { margin-left: 0; }
  }
</style>
