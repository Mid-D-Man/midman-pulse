<script lang="ts">
  import { onMount } from 'svelte';
  import '../../app.css';
  import { theme } from '$lib/stores/theme';
  import { registerSW } from '$lib/pwa';
  import Nav from '$lib/components/layout/Nav.svelte';
  import Footer from '$lib/components/layout/Footer.svelte';
  import InstallBanner from '$lib/components/pwa/InstallBanner.svelte';
  import CookieBanner from '$lib/components/ui/CookieBanner.svelte';

  export let data: { categories: any[] };

  onMount(() => {
    theme.init();
    registerSW();
  });
</script>

<div class="layout">
  <Nav categories={data.categories} />
  <main class="main">
    <slot />
  </main>
  <Footer />
  <InstallBanner />
  <CookieBanner />
</div>

<style>
  .layout {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }

  .main {
    flex: 1;
    display: flex;
    flex-direction: column;
  }
</style>
