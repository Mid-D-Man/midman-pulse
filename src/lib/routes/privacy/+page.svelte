<svelte:head>
  <title>Privacy Policy — MidMan Pulse</title>
</svelte:head>

<div class="legal-page container">
  <h1>Privacy Policy</h1>
  <p class="updated">Last updated: April 2026</p>

  <section>
    <h2>1. What we collect</h2>
    <p>MidMan Pulse does not require registration. We collect only what is necessary to operate the site:</p>
    <ul>
      <li><strong>Newsletter email address</strong> — only if you voluntarily subscribe via our Brevo-powered form.</li>
      <li><strong>Usage analytics</strong> — anonymised page-view data via Cloudflare's built-in analytics (no cookies, no cross-site tracking).</li>
      <li><strong>Server logs</strong> — standard Cloudflare edge logs (IP address, user-agent, request path) retained for up to 24 hours for abuse prevention.</li>
    </ul>
  </section>

  <section>
    <h2>2. How we use it</h2>
    <ul>
      <li>Newsletter emails are used solely to send the MidMan Pulse digest. We do not sell, rent, or share your email with third parties.</li>
      <li>Analytics data is used only to understand aggregate traffic patterns and improve the site.</li>
    </ul>
  </section>

  <section>
    <h2>3. Third-party services</h2>
    <ul>
      <li><strong>Cloudflare</strong> — hosting, edge network, analytics. <a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noopener">Cloudflare Privacy Policy</a>.</li>
      <li><strong>Brevo</strong> — newsletter delivery. <a href="https://www.brevo.com/legal/privacypolicy/" target="_blank" rel="noopener">Brevo Privacy Policy</a>.</li>
      <li><strong>Google Fonts</strong> — fonts are loaded from Google's CDN. <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google Privacy Policy</a>.</li>
    </ul>
  </section>

  <section>
    <h2>4. Cookies</h2>
    <p>MidMan Pulse uses a single first-party cookie (<code>mmp-theme</code>) to remember your light/dark mode preference. No tracking or advertising cookies are set. See our <a href="/cookies">Cookie Policy</a> for details.</p>
  </section>

  <section>
    <h2>5. Your rights</h2>
    <p>You may request deletion of your email from our newsletter at any time by using the unsubscribe link in any email or by contacting us at <a href="mailto:privacy@midmanstudio.com">privacy@midmanstudio.com</a>.</p>
  </section>

  <section>
    <h2>6. Data retention</h2>
    <p>Newsletter emails are held until you unsubscribe. Cloudflare edge logs are retained for up to 24 hours. We do not store any other personal data.</p>
  </section>

  <section>
    <h2>7. Changes</h2>
    <p>We may update this policy occasionally. Significant changes will be noted at the top of this page.</p>
  </section>

  <section>
    <h2>8. Contact</h2>
    <p>Questions? Email <a href="mailto:privacy@midmanstudio.com">privacy@midmanstudio.com</a>.</p>
  </section>
</div>

<style>
  .legal-page {
    max-width: 760px;
    padding-top: 3rem;
    padding-bottom: 4rem;
  }

  h1 {
    font-size: clamp(1.75rem, 4vw, 2.25rem);
    color: var(--text);
    margin-bottom: 0.375rem;
  }

  .updated {
    font-size: 0.8125rem;
    color: var(--text-muted);
    font-family: var(--font-mono);
    margin-bottom: 2.5rem;
  }

  section { margin-bottom: 2rem; }

  h2 {
    font-size: 1.0625rem;
    color: var(--text);
    margin-bottom: 0.625rem;
    padding-bottom: 0.375rem;
    border-bottom: 1px solid var(--border);
  }

  p  { font-size: 0.9375rem; color: var(--text-muted); line-height: 1.8; margin-bottom: 0.75rem; }
  ul { padding-left: 1.25rem; display: flex; flex-direction: column; gap: 0.5rem; }
  li { font-size: 0.9375rem; color: var(--text-muted); line-height: 1.7; }

  a { color: var(--accent); text-decoration: underline; text-underline-offset: 2px; }
  a:hover { color: var(--accent-hover); }
  code { font-size: 0.875em; }
</style>
