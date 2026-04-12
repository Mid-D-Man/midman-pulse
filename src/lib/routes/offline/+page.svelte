<svelte:head>
  <title>You're offline — MidMan Pulse</title>
</svelte:head>

<div class="offline-page container">
  <div class="offline-inner">

    <div class="offline-icon" aria-hidden="true">
      <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path stroke-linecap="round" stroke-linejoin="round" d="M3 3l18 18M8.111 8.111A5.97 5.97 0 006 12a6 6 0 006 6 5.97 5.97 0 003.889-1.389M10.59 5.17A6 6 0 0118 12a5.97 5.97 0 01-.54 2.48M21 12a9 9 0 00-9-9 8.966 8.966 0 00-4.949 1.465M3 12a9 9 0 009 9c.956 0 1.878-.149 2.742-.424"/>
      </svg>
    </div>

    <h1 class="offline-title">You're offline</h1>
    <p class="offline-sub">
      No internet connection right now. Previously visited pages are available below.
      New articles will load once you're back online.
    </p>

    <button class="offline-retry" on:click={() => window.location.reload()}>
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <path stroke-linecap="round" stroke-linejoin="round" d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99"/>
      </svg>
      Try again
    </button>

    <a href="/" class="offline-home">Go to home</a>

  </div>
</div>

<style>
  .offline-page {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: calc(100vh - 7rem);
    padding-top: 2rem;
    padding-bottom: 2rem;
  }

  .offline-inner {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.25rem;
    text-align: center;
    max-width: 420px;
  }

  .offline-icon {
    width: 80px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--bg-muted);
    border: 1px solid var(--border);
    border-radius: 50%;
    color: var(--text-muted);
  }

  .offline-title {
    font-size: 1.75rem;
    color: var(--text);
  }

  .offline-sub {
    font-size: 0.9375rem;
    color: var(--text-muted);
    line-height: 1.75;
  }

  .offline-retry {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.65rem 1.5rem;
    background: var(--accent);
    color: #fff;
    border: none;
    border-radius: var(--radius);
    font-size: 0.9375rem;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.15s, transform 0.15s;
    margin-top: 0.5rem;
  }

  .offline-retry:hover {
    background: var(--accent-hover);
    transform: translateY(-1px);
  }

  .offline-home {
    font-size: 0.875rem;
    color: var(--text-muted);
    text-decoration: underline;
    text-underline-offset: 2px;
    transition: color 0.15s;
  }

  .offline-home:hover { color: var(--accent); }
</style>
