<script lang="ts">
  export let variant: 'default' | 'accent' | 'muted' = 'default';
  export let label: string;
</script>

<span class="badge badge--{variant}">{label}</span>

<style>
  .badge {
    display: inline-flex;
    align-items: center;
    font-size: 0.625rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    padding: 0.2rem 0.5rem;
    border-radius: 9999px;
    font-family: var(--font-mono);
    white-space: nowrap;
  }

  .badge--default {
    background: var(--bg-muted);
    color: var(--text-muted);
    border: 1px solid var(--border);
  }

  .badge--accent {
    background: var(--accent-dim);
    color: var(--accent);
    border: 1px solid var(--accent);
  }

  .badge--muted {
    background: transparent;
    color: var(--text-muted);
    border: 1px solid var(--border);
  }
</style>
