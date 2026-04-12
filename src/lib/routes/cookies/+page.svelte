<svelte:head>
  <title>Cookie Policy — MidMan Pulse</title>
  <meta name="description" content="How MidMan Pulse uses cookies and local storage." />
</svelte:head>

<div class="legal-page container">
  <header class="legal-header">
    <a href="/" class="legal-back">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18"/>
      </svg>
      Back to home
    </a>
    <h1>Cookie Policy</h1>
    <p class="legal-updated">Last updated: April 2026</p>
  </header>

  <div class="legal-body">

    <section>
      <h2>What is a cookie?</h2>
      <p>Cookies are small files a website stores in your browser. "Local storage" works similarly — it stores key/value data in your browser, not on a server.</p>
    </section>

    <section>
      <h2>What we use</h2>

      <div class="cookie-table-wrap">
        <table class="cookie-table">
          <thead>
            <tr>
              <th>Name</th>
              <th>Storage type</th>
              <th>Purpose</th>
              <th>Duration</th>
              <th>Third party?</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>mmp-theme</code></td>
              <td>localStorage</td>
              <td>Stores your light/dark mode choice</td>
              <td>Until you clear browser data</td>
              <td>No</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout callout--info">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>
        </svg>
        <p>We use <strong>zero advertising cookies</strong> and <strong>zero cross-site tracking cookies</strong>. Cloudflare's analytics are cookieless.</p>
      </div>
    </section>

    <section>
      <h2>Third-party storage</h2>
      <p>If you subscribe to the newsletter, <strong>Brevo</strong> may set their own cookies when you interact with emails or their embedded forms. We have no control over these. See the <a href="https://www.brevo.com/legal/privacypolicy/" target="_blank" rel="noopener noreferrer">Brevo Privacy Policy</a>.</p>
      <p><strong>Google Fonts</strong> are loaded from Google's CDN. Google may log your IP when serving font files. See <a href="https://developers.google.com/fonts/faq/privacy" target="_blank" rel="noopener noreferrer">Google Fonts privacy FAQ</a>.</p>
    </section>

    <section>
      <h2>How to manage cookies</h2>
      <p>You can clear or block localStorage and cookies in your browser settings. Clearing <code>mmp-theme</code> simply means your dark/light preference won't be saved — the site works fine without it.</p>

      <ul>
        <li>
          <a href="https://support.google.com/chrome/answer/95647" target="_blank" rel="noopener noreferrer">Chrome — manage cookies</a>
        </li>
        <li>
          <a href="https://support.mozilla.org/en-US/kb/enhanced-tracking-protection-firefox-desktop" target="_blank" rel="noopener noreferrer">Firefox — tracking protection</a>
        </li>
        <li>
          <a href="https://support.apple.com/en-gb/guide/safari/sfri11471/mac" target="_blank" rel="noopener noreferrer">Safari — manage cookies</a>
        </li>
        <li>
          <a href="https://support.microsoft.com/en-us/microsoft-edge/delete-cookies-in-microsoft-edge-63947406-40ac-c3b8-57b9-2a946a29ae09" target="_blank" rel="noopener noreferrer">Edge — delete cookies</a>
        </li>
      </ul>
    </section>

    <section>
      <h2>Future advertising</h2>
      <p>If we introduce an advertising network in the future, this policy will be updated before any ad cookies are placed, and you will be informed via a consent notice.</p>
    </section>

    <section>
      <h2>Contact</h2>
      <p>Questions about cookies? Email <a href="mailto:privacy@midmanstudio.com">privacy@midmanstudio.com</a></p>
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
    gap: 0.875rem;
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

  /* ── Cookie table ── */
  .cookie-table-wrap { overflow-x: auto; }

  .cookie-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.8125rem;
    min-width: 520px;
  }

  .cookie-table th {
    text-align: left;
    padding: 0.625rem 0.875rem;
    background: var(--bg-muted);
    border: 1px solid var(--border);
    font-family: var(--font-mono);
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--text-muted);
  }

  .cookie-table td {
    padding: 0.625rem 0.875rem;
    border: 1px solid var(--border);
    color: var(--text-muted);
    vertical-align: top;
    line-height: 1.6;
  }

  /* ── Callout ── */
  .callout {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    padding: 0.875rem 1rem;
    border-radius: var(--radius);
    font-size: 0.875rem;
  }

  .callout svg { flex-shrink: 0; margin-top: 0.1rem; }

  .callout p { font-size: 0.875rem; margin: 0; line-height: 1.65; }

  .callout--info {
    background: var(--accent-dim);
    border: 1px solid var(--accent);
    color: var(--accent);
  }

  .callout--info p { color: var(--accent); }
</style>
