<script lang="ts">
  let email   = '';
  let state: 'idle' | 'loading' | 'success' | 'error' = 'idle';
  let message = '';

  // Replace with your Brevo form action URL:
  // Brevo → Contacts → Forms → your form → Embed → action="..."
  const FORM_ACTION = 'https://app.brevo.com/newsletter/form/YOUR_FORM_ID';

  async function submit() {
    if (!email || !email.includes('@')) {
      message = 'Please enter a valid email address.';
      state   = 'error';
      return;
    }
    state   = 'loading';
    message = '';
    try {
      const body = new FormData();
      body.append('EMAIL', email);
      await fetch(FORM_ACTION, { method: 'POST', body, mode: 'no-cors' });
      state   = 'success';
      message = "You're in! Check your inbox to confirm.";
      email   = '';
    } catch {
      state   = 'error';
      message = 'Something went wrong. Please try again.';
    }
  }
</script>

<div class="newsletter">
  <div class="newsletter-inner">
    <div class="newsletter-text">
      <h3 class="newsletter-title">Stay in the loop</h3>
      <p class="newsletter-sub">AI, cybersecurity and business intel — straight to your inbox.</p>
    </div>

    {#if state === 'success'}
      <div class="newsletter-success">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
        </svg>
        <span>{message}</span>
      </div>
    {:else}
      <div class="newsletter-form">
        <input
          type="email"
          bind:value={email}
          placeholder="you@example.com"
          class="newsletter-input"
          class:error={state === 'error'}
          on:keydown={(e) => e.key === 'Enter' && submit()}
          disabled={state === 'loading'}
        />
        <button class="newsletter-btn" on:click={submit} disabled={state === 'loading'}>
          {state === 'loading' ? 'Subscribing…' : 'Subscribe'}
        </button>
      </div>
      {#if state === 'error'}
        <p class="newsletter-error">{message}</p>
      {/if}
      <p class="newsletter-note">Free. No spam. Unsubscribe any time.</p>
    {/if}
  </div>
</div>

<style>
  .newsletter {
    background: var(--bg-surface);
    border: 1px solid var(--border);
    border-radius: calc(var(--radius) * 2);
    padding: 2rem 1.5rem;
    margin: 2rem 0;
  }

  .newsletter-inner {
    max-width: 480px;
    margin: 0 auto;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }

  .newsletter-title {
    font-size: 1.125rem;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 0.25rem;
  }

  .newsletter-sub {
    font-size: 0.875rem;
    color: var(--text-muted);
    line-height: 1.6;
  }

  .newsletter-form {
    display: flex;
    gap: 0.5rem;
    width: 100%;
  }

  .newsletter-input {
    flex: 1;
    min-width: 0;
    padding: 0.625rem 1rem;
    font-size: 0.875rem;
    background: var(--bg-muted);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    color: var(--text);
    outline: none;
    transition: border-color 0.15s;
  }

  .newsletter-input:focus        { border-color: var(--accent); }
  .newsletter-input.error        { border-color: var(--danger); }
  .newsletter-input::placeholder { color: var(--text-muted); }

  .newsletter-btn {
    padding: 0.625rem 1.25rem;
    background: var(--accent);
    color: #fff;
    border: none;
    border-radius: var(--radius);
    font-size: 0.875rem;
    font-weight: 600;
    cursor: pointer;
    white-space: nowrap;
    flex-shrink: 0;
    transition: background 0.15s;
  }

  .newsletter-btn:hover:not(:disabled) { background: var(--accent-hover); }
  .newsletter-btn:disabled { opacity: 0.6; cursor: not-allowed; }

  .newsletter-error {
    font-size: 0.8125rem;
    color: var(--danger);
  }

  .newsletter-note {
    font-size: 0.75rem;
    color: var(--text-muted);
  }

  .newsletter-success {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: #22c55e;
    font-size: 0.9375rem;
    font-weight: 500;
  }

  @media (max-width: 480px) {
    .newsletter-form      { flex-direction: column; }
    .newsletter-btn       { justify-content: center; width: 100%; }
  }
</style>
