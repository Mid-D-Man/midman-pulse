<svelte:head>
  <title>Privacy Policy — MidMan Pulse</title>
  <meta name="description" content="How MidMan Pulse collects, uses, and protects your data." />
</svelte:head>

<div class="legal-page container">
  <header class="legal-header">
    <a href="/" class="legal-back">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18"/>
      </svg>
      Back to home
    </a>
    <h1>Privacy Policy</h1>
    <p class="legal-updated">Last updated: April 2026</p>
  </header>

  <div class="legal-body">

    <section>
      <h2>1. Who we are</h2>
      <p>MidMan Pulse is a news aggregation service operated by MidManStudio. We surface curated articles across AI, cybersecurity, business, and game development topics.</p>
      <p>Contact: <a href="mailto:privacy@midmanstudio.com">privacy@midmanstudio.com</a></p>
    </section>

    <section>
      <h2>2. What we collect and why</h2>

      <div class="data-table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Data</th>
              <th>Why</th>
              <th>Legal basis</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Email address (newsletter only)</td>
              <td>Sending you the MidMan Pulse digest</td>
              <td>Consent</td>
            </tr>
            <tr>
              <td>Anonymised page-view counts</td>
              <td>Understanding site traffic (no cookies)</td>
              <td>Legitimate interest</td>
            </tr>
            <tr>
              <td>Cloudflare edge logs (IP, user-agent)</td>
              <td>Abuse prevention, DDoS mitigation</td>
              <td>Legitimate interest</td>
            </tr>
            <tr>
              <td>Theme preference (localStorage)</td>
              <td>Remembering light/dark mode</td>
              <td>Functional necessity</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p>We do <strong>not</strong> collect names, payment details, or any other personal information.</p>
    </section>

    <section>
      <h2>3. Newsletter</h2>
      <p>If you subscribe, your email address is stored by Brevo (our email platform) and used exclusively to deliver the newsletter. We do not sell, rent, or share your email with any third party. You can unsubscribe at any time using the link in every email.</p>
    </section>

    <section>
      <h2>4. Third-party services</h2>
      <ul>
        <li><strong>Cloudflare</strong> — CDN, hosting, edge analytics. Processes request data to deliver the site. <a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noopener noreferrer">Privacy policy →</a></li>
        <li><strong>Brevo</strong> — Email delivery for newsletter subscribers. <a href="https://www.brevo.com/legal/privacypolicy/" target="_blank" rel="noopener noreferrer">Privacy policy →</a></li>
        <li><strong>Google Fonts</strong> — Fonts loaded from Google CDN. Google may log your IP. <a href="https://policies.google.com/privacy" target="_blank" rel="noopener noreferrer">Privacy policy →</a></li>
      </ul>
    </section>

    <section>
      <h2>5. Cookies</h2>
      <p>We use one functional cookie — <code>mmp-theme</code> stored in localStorage — to remember your display preference. No advertising or tracking cookies are used. See our full <a href="/cookies">Cookie Policy</a>.</p>
    </section>

    <section>
      <h2>6. Data retention</h2>
      <ul>
        <li>Newsletter emails — until you unsubscribe.</li>
        <li>Cloudflare edge logs — up to 24 hours.</li>
        <li>Anonymous analytics — rolling 30-day window.</li>
      </ul>
    </section>

    <section>
      <h2>7. Your rights</h2>
      <p>Depending on your location you may have rights to access, correct, delete, or port your data. To exercise any right, email <a href="mailto:privacy@midmanstudio.com">privacy@midmanstudio.com</a>. We will respond within 30 days.</p>
    </section>

    <section>
      <h2>8. Children</h2>
      <p>MidMan Pulse is not directed at children under 13. We do not knowingly collect data from children.</p>
    </section>

    <section>
      <h2>9. Changes to this policy</h2>
      <p>Material changes will be flagged with an updated date at the top of this page. Continued use after changes constitutes acceptance.</p>
    </section>

  </div>
</div>

<style>
  .legal-page {
    max-width: 760px;
    padding-top: 2.5rem;
    padding-bottom: 5rem;
  }

  .legal-header { margin-bottom: 2.5rem; }

  .legal-back {
    display: inline-flex;
    align-items: center;
    gap: 0.375rem;
    font-size: 0.8125rem;
    color: var(--text-muted);
    text-decoration: none;
    margin-bottom: 1.25rem;
    transition: color 0.15s;
  }

  .legal-back:hover { color: var(--accent); }

  h1 {
    font-size: clamp(1.75rem, 4vw, 2.25rem);
    color: var(--text);
    margin-bottom: 0.375rem;
  }

  .legal-updated {
    font-size: 0.8125rem;
    color: var(--text-muted);
    font-family: var(--font-mono);
  }

  .legal-body {
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }

  section {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  h2 {
    font-size: 1.0625rem;
    color: var(--text);
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--border);
  }

  p  { font-size: 0.9375rem; color: var(--text-muted); line-height: 1.8; }
  ul { padding-left: 1.25rem; display: flex; flex-direction: column; gap: 0.5rem; }
  li { font-size: 0.9375rem; color: var(--text-muted); line-height: 1.7; }

  a { color: var(--accent); text-decoration: underline; text-underline-offset: 2px; }
  a:hover { color: var(--accent-hover); }
  code { font-size: 0.875em; }

  /* ── Data table ── */
  .data-table-wrap { overflow-x: auto; }

  .data-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.875rem;
    min-width: 480px;
  }

  .data-table th {
    text-align: left;
    padding: 0.625rem 0.875rem;
    background: var(--bg-muted);
    border: 1px solid var(--border);
    font-family: var(--font-mono);
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--text-muted);
  }

  .data-table td {
    padding: 0.625rem 0.875rem;
    border: 1px solid var(--border);
    color: var(--text-muted);
    vertical-align: top;
    line-height: 1.6;
  }
</style>
