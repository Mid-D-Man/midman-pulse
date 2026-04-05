<script lang="ts">
  export let slot: 'banner' | 'sidebar' | 'inline' = 'inline';
  export let label: string = 'Advertisement';
</script>

<div class="ad-slot ad-slot--{slot}" aria-label={label}>
  <span class="ad-label">{label}</span>
  <div class="ad-placeholder">
    <!-- ad network script goes here once approved -->
  </div>
</div>

<style>
  .ad-slot {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.375rem;
    border: 1px dashed var(--border);
    border-radius: var(--radius);
    background: var(--bg-muted);
    overflow: hidden;
  }

  .ad-label {
    font-size: 0.625rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--text-muted);
    font-family: var(--font-mono);
    padding-top: 0.375rem;
  }

  .ad-slot--banner {
    width: 100%;
    min-height: 90px;
  }

  .ad-slot--sidebar {
    width: 100%;
    min-height: 250px;
  }

  .ad-slot--inline {
    width: 100%;
    min-height: 100px;
  }

  .ad-placeholder {
    width: 100%;
    flex: 1;
  }
</style>
