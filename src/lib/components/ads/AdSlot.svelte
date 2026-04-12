<script lang="ts">
  import { onMount } from 'svelte';
  import { ADS_ENABLED } from '$lib/config';

  export let slot: 'banner' | 'sidebar' | 'inline' = 'inline';

  /**
   * Adsterra Ad Units
   * ─────────────────────────────────────────────────────────────
   * WHICH TO USE WHERE:
   *
   * 'banner'  → top of category pages — use Native Banner
   * 'sidebar' → right column desktop  — use Native Banner
   * 'inline'  → between article cards — use Native Banner
   *
   * SKIP the Social Bar unit entirely on this site —
   * it floats over content and hurts UX for a news reader.
   * Keep it turned off unless you specifically want it.
   *
   * Your Native Banner unit ID: 18cf884c9084c53cdeb4e10b9fc28536
   * ─────────────────────────────────────────────────────────────
   */

  const NATIVE_BANNER_ID = '18cf884c9084c53cdeb4e10b9fc28536';
  const NATIVE_SCRIPT_SRC = 'https://pl29132590.profitablecpmratenetwork.com/18cf884c9084c53cdeb4e10b9fc28536/invoke.js';

  // Social Bar — disabled. Uncomment only if you specifically want it.
  // const SOCIAL_BAR_SRC = 'https://pl29132588.profitablecpmratenetwork.com/3c/33/04/3c33046a4c1ed7043b3c716ce5d67e2b.js';
  // const SOCIAL_BAR_POPUNDER = 'https://www.profitablecpmratenetwork.com/fn67x1re?key=ee7aec7cf1378be9724aa84032faa397';

  let mounted = false;
  onMount(() => { mounted = true; });
</script>

{#if ADS_ENABLED && mounted}
  <div class="ad-slot ad-slot--{slot}" aria-label="Advertisement">
    <span class="ad-label">Advertisement</span>
    <!-- Native Banner — works for all three slot positions -->
    <div id="container-{NATIVE_BANNER_ID}" class="ad-container">
      <script
        async
        data-cfasync="false"
        src={NATIVE_SCRIPT_SRC}
      ></script>
    </div>
  </div>
{/if}

<style>
  .ad-slot {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.375rem;
    overflow: hidden;
    width: 100%;
  }

  .ad-label {
    font-size: 0.6rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--text-muted);
    font-family: var(--font-mono);
    align-self: flex-start;
    padding: 0.2rem 0;
  }

  .ad-container { width: 100%; }

  .ad-slot--banner  { min-height: 90px; }
  .ad-slot--sidebar { min-height: 250px; }
  .ad-slot--inline  { min-height: 100px; }
</style>
