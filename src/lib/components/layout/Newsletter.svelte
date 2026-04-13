<script lang="ts">
  /**
   * Newsletter signup widget.
   * Set FORM_ACTION to your email provider's form endpoint.
   * Works with Brevo, Mailchimp, ConvertKit, etc.
   */

  const FORM_ACTION = 'https://app.brevo.com/newsletter/form/YOUR_FORM_ID';
  const IS_CONFIGURED = !FORM_ACTION.includes('YOUR_FORM_ID');

  let email   = '';
  let state: 'idle' | 'loading' | 'success' | 'error' = 'idle';
  let message = '';

  async function submit() {
    if (!IS_CONFIGURED) {
      message = 'Newsletter signup is coming soon — check back shortly.';
      state   = 'error';
      return;
    }
    if (!email || !email.includes('@') || !email.includes('.')) {
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
      message = "You're in! Check your inbox to confirm your subscription.";
      email   = '';
    } catch {
      state   = 'error';
      message = 'Something went wrong. Please try again in a moment.';
    }
  }
</script>

<div class="newsletter">
  <div class="newsletter-inner">

    <div class="newsletter-text">
      <div class="newsletter-eyebrow">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75"/>
        </svg>
        <span>Free Newsletter</span>
      </div>
      <h3 class="newsletter-title">Stay in the loop</h3>
      <p class="newsletter-sub">
        AI, cybersecurity, and business intel — hand-curated and delivered to your inbox.
        No spam. Unsubscribe any time.
      </p>
    </div>

    {#if state === 'success'}
      <div class="newsletter-success">
        <div class="newsletter-success-icon" aria-hidden="true">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
        </div>
        <div>
          <p class="newsletter-success-title">You're subscribed!</p>
          <p class="newsletter-success-sub">{message}</p>
        </div>
      </div>

    {:else}
      <div class="newsletter-form-wrap">
        <div class="newsletter-form">
          <input
            type="email"
            bind:value={email}
            placeholder="your@email.com"
            class="newsletter-input"
            class:newsletter-input--error={state === 'error'}
            on:keydown={(e) => e.key === 'Enter' && submit()}
            disabled={state === 'loading'}
            aria-label="Email address"
          />
          <button
            class="newsletter-btn"
            on:click={submit}
            disabled={state === 'loading'}
            aria-label="Subscribe to newsletter"
          >
            {#if state === 'loading'}
              <span class="newsletter-spinner" aria-hidden="true"></span>
              Subscribing…
            {:else}
              Subscribe
            {/if}
          </button>
        </div>

        {#if state === 'error'}
          <p class="newsletter-error" role="alert">{message}</p>
        {/if}

        <p class="newsletter-note">
          Free newsletter. No spam. See our <a href="/privacy">Privacy Policy</a>.
        </p>
      </div>
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
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    align-items: center;
    max-width: 860px;
    margin: 0 auto;
  }

  .newsletter-eyebrow {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    font-size: 0.6875rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--accent);
    font-family: var(--font-mono);
    margin-bottom: 0.625rem;
  }

  .newsletter-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 0.5rem;
  }

  .newsletter-sub {
    font-size: 0.875rem;
    color: var(--text-muted);
    line-height: 1.7;
  }

  .newsletter-form-wrap {
    display: flex;
    flex-direction: column;
    gap: 0.625rem;
  }

  .newsletter-form {
    display: flex;
    gap: 0.5rem;
  }

  .newsletter-input {
    flex: 1;
    min-width: 0;
    padding: 0.65rem 1rem;
    font-size: 0.9rem;
    background: var(--bg-muted);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    color: var(--text);
    outline: none;
    transition: border-color 0.15s, box-shadow 0.15s;
  }

  .newsletter-input:focus {
    border-color: var(--accent);
    box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.12);
  }

  .newsletter-input--error { border-color: var(--danger); }
  .newsletter-input::placeholder { color: var(--text-muted); }

  .newsletter-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.375rem;
    padding: 0.65rem 1.25rem;
    background: var(--accent);
    color: #fff;
    border: none;
    border-radius: var(--radius);
    font-size: 0.875rem;
    font-weight: 600;
    cursor: pointer;
    white-space: nowrap;
    flex-shrink: 0;
    transition: background 0.15s, transform 0.15s;
  }

  .newsletter-btn:hover:not(:disabled) {
    background: var(--accent-hover);
    transform: translateY(-1px);
  }

  .newsletter-btn:disabled { opacity: 0.65; cursor: not-allowed; }

  .newsletter-spinner {
    display: inline-block;
    width: 13px;
    height: 13px;
    border: 2px solid rgba(255,255,255,0.4);
    border-top-color: #fff;
    border-radius: 50%;
    animation: spin 0.65s linear infinite;
    flex-shrink: 0;
  }

  @keyframes spin { to { transform: rotate(360deg); } }

  .newsletter-error {
    font-size: 0.8125rem;
    color: var(--danger);
  }

  .newsletter-note {
    font-size: 0.75rem;
    color: var(--text-muted);
    line-height: 1.6;
  }

  .newsletter-note a {
    color: var(--text-muted);
    text-decoration: underline;
    text-underline-offset: 2px;
    transition: color 0.15s;
  }

  .newsletter-note a:hover { color: var(--accent); }

  .newsletter-success {
    display: flex;
    align-items: flex-start;
    gap: 0.875rem;
    background: var(--accent-dim);
    border: 1px solid var(--accent);
    border-radius: var(--radius);
    padding: 1rem 1.25rem;
  }

  .newsletter-success-icon {
    color: var(--accent);
    flex-shrink: 0;
    margin-top: 0.1rem;
  }

  .newsletter-success-title {
    font-size: 0.9375rem;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 0.25rem;
  }

  .newsletter-success-sub {
    font-size: 0.8125rem;
    color: var(--text-muted);
    line-height: 1.6;
  }

  @media (max-width: 768px) {
    .newsletter-inner { grid-template-columns: 1fr; gap: 1.25rem; }
  }

  @media (max-width: 480px) {
    .newsletter-form     { flex-direction: column; }
    .newsletter-btn      { justify-content: center; }
    .newsletter { padding: 1.5rem 1rem; }
  }
</style>
