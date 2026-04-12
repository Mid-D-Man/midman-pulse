<svelte:head>
  <title>Cookie Policy — MidMan Pulse</title>
</svelte:head>

<div class="legal-page container">
  <h1>Cookie Policy</h1>
  <p class="updated">Last updated: April 2026</p>

  <section>
    <h2>What is a cookie?</h2>
    <p>Cookies are small text files stored in your browser by websites you visit. They are widely used to make sites work, remember preferences, and gather analytics.</p>
  </section>

  <section>
    <h2>Cookies we use</h2>
    <div class="cookie-table-wrap">
      <table class="cookie-table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Purpose</th>
            <th>Duration</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>mmp-theme</code></td>
            <td>Functional</td>
            <td>Stores your light/dark mode preference.</td>
            <td>Persistent (localStorage)</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p>We do <strong>not</strong> use advertising cookies, third-party tracking cookies, or analytics cookies that identify you personally. Cloudflare's edge analytics are cookieless.</p>
  </section>

  <section>
    <h2>Newsletter</h2>
    <p>If you subscribe to our newsletter via Brevo, Brevo may set their own cookies when you click links in emails. Please see the <a href="https://www.brevo.com/legal/privacypolicy/" target="_blank" rel="noopener">Brevo Privacy Policy</a>.</p>
  </section>

  <section>
    <h2>Managing cookies</h2>
    <p>You can clear or block cookies via your browser settings. Blocking our single preference cookie just means your theme choice won't persist between visits — the Site will continue to work normally.</p>
    <ul>
      <li><a href="https://support.google.com/chrome/answer/95647" target="_blank" rel="noopener">Chrome</a></li>
      <li><a href="https://support.mozilla.org/en-US/kb/enable-and-disable-cookies-website-preferences" target="_blank" rel="noopener">Firefox</a></li>
      <li><a href="https://support.apple.com/en-gb/guide/safari/sfri11471/mac" target="_blank" rel="noopener">Safari</a></li>
      <li><a href="https://support.microsoft.com/en-us/microsoft-edge/delete-cookies-in-microsoft-edge-63947406-40ac-c3b8-57b9-2a946a29ae09" target="_blank" rel="noopener">Edge</a></li>
    </ul>
  </section>

  <section>
    <h2>Contact</h2>
    <p>Questions about our cookie use? Email <a href="mailto:privacy@midmanstudio.com">privacy@midmanstudio.com</a>.</p>
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
  ul { padding-left: 1.25rem; display: flex; flex-direction: column; gap: 0.5rem; margin-top: 0.5rem; }
  li { font-size: 0.9375rem; color: var(--text-muted); line-height: 1.7; }

  a { color: var(--accent); text-decoration: underline; text-underline-offset: 2px; }
  a:hover { color: var(--accent-hover); }

  .cookie-table-wrap { overflow-x: auto; margin-bottom: 1rem; }

  .cookie-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.875rem;
    min-width: 480px;
  }

  .cookie-table th {
    text-align: left;
    padding: 0.625rem 0.875rem;
    background: var(--bg-muted);
    border: 1px solid var(--border);
    font-family: var(--font-mono);
    font-size: 0.72rem;
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

  code { font-size: 0.875em; }
</style>
