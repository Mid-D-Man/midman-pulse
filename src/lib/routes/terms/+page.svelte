<svelte:head>
  <title>Terms of Service — MidMan Pulse</title>
</svelte:head>

<div class="legal-page container">
  <h1>Terms of Service</h1>
  <p class="updated">Last updated: April 2026</p>

  <section>
    <h2>1. Acceptance</h2>
    <p>By accessing MidMan Pulse ("the Site") you agree to these Terms. If you do not agree, please do not use the Site.</p>
  </section>

  <section>
    <h2>2. What the Site is</h2>
    <p>MidMan Pulse is an automated news aggregation and curation service. All articles are sourced from publicly available RSS feeds. The Site does not claim ownership of third-party content and links to original sources.</p>
  </section>

  <section>
    <h2>3. Intellectual property</h2>
    <p>The MidMan Pulse name, logo, and original site design are the property of MidManStudio. Article summaries are AI-generated from publicly available text. Full articles belong to their respective publishers — click through to read the original.</p>
  </section>

  <section>
    <h2>4. Acceptable use</h2>
    <p>You may not:</p>
    <ul>
      <li>Scrape or bulk-download site content for redistribution.</li>
      <li>Use automated tools to overload our servers.</li>
      <li>Attempt to access restricted areas or the ingest API without authorisation.</li>
    </ul>
  </section>

  <section>
    <h2>5. Disclaimer</h2>
    <p>The Site is provided "as is." We make no warranty that content is accurate, complete, or up to date. Nothing on this Site constitutes financial, legal, or professional advice.</p>
  </section>

  <section>
    <h2>6. Limitation of liability</h2>
    <p>To the maximum extent permitted by law, MidManStudio is not liable for any indirect, incidental, or consequential damages arising from your use of the Site.</p>
  </section>

  <section>
    <h2>7. External links</h2>
    <p>We link to third-party sites. We have no control over and take no responsibility for their content or privacy practices.</p>
  </section>

  <section>
    <h2>8. Changes</h2>
    <p>We may update these Terms at any time. Continued use of the Site after changes constitutes acceptance of the updated Terms.</p>
  </section>

  <section>
    <h2>9. Governing law</h2>
    <p>These Terms are governed by the laws of the jurisdiction in which MidManStudio operates, without regard to conflict-of-law provisions.</p>
  </section>

  <section>
    <h2>10. Contact</h2>
    <p>Questions? Email <a href="mailto:legal@midmanstudio.com">legal@midmanstudio.com</a>.</p>
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
</style>
