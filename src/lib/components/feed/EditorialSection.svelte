<script lang="ts">
  import { SHOW_EDITORIAL, EDITORIAL_ARTICLES } from '$lib/editorial';
  import EditorialCard from './EditorialCard.svelte';

  // Filter to only active articles
  $: visible = EDITORIAL_ARTICLES.filter(a => a.active !== false);
  $: show    = SHOW_EDITORIAL && visible.length > 0;
</script>

{#if show}
  <section class="editorial-section">
    <div class="editorial-header">
      <div class="editorial-header-left">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" class="editorial-icon">
          <path d="M13 10V3L4 14h7v7l9-11h-7z"/>
        </svg>
        <span class="editorial-label">From MidManStudio</span>
      </div>
      <span class="editorial-sub">Hand-picked by the studio</span>
    </div>

    <div class="editorial-list">
      {#each visible as article (article.title)}
        <EditorialCard {article} />
      {/each}
    </div>
  </section>
{/if}

<style>
  .editorial-section {
    padding: 2rem 0 1.5rem;
    border-bottom: 1px solid var(--border);
  }

  .editorial-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1.25rem;
    flex-wrap: wrap;
  }

  .editorial-header-left {
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }

  .editorial-icon {
    color: var(--accent);
    flex-shrink: 0;
  }

  .editorial-label {
    font-size: 0.6875rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--accent);
    font-family: var(--font-mono);
  }

  .editorial-sub {
    font-size: 0.75rem;
    color: var(--text-muted);
    font-family: var(--font-mono);
  }

  .editorial-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
</style>
