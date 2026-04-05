<script lang="ts">
  export let width: string = '100%';
  export let height: string = '1rem';
  export let rounded: boolean = false;
</script>

<div
  class="skeleton"
  class:skeleton--rounded={rounded}
  style="width:{width};height:{height}"
></div>

<style>
  .skeleton {
    background: linear-gradient(
      90deg,
      var(--bg-muted) 25%,
      var(--border) 50%,
      var(--bg-muted) 75%
    );
    background-size: 200% 100%;
    animation: shimmer 1.5s infinite;
    border-radius: var(--radius);
  }

  .skeleton--rounded { border-radius: 9999px; }

  @keyframes shimmer {
    0%   { background-position: 200% 0; }
    100% { background-position: -200% 0; }
  }
</style>
