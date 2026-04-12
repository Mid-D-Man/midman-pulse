<svelte:head>
  <title>Terms of Service — MidMan Pulse</title>
  <meta name="description" content="Terms governing your use of MidMan Pulse." />
</svelte:head>

<div class="legal-page container">
  <header class="legal-header">
    <a href="/" class="legal-back">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18"/>
      </svg>
      Back to home
    </a>
    <h1>Terms of Service</h1>
    <p class="legal-updated">Last updated: April 2026</p>
  </header>

  <div class="legal-body">

    <section>
      <h2>1. Acceptance</h2>
      <p>By accessing MidMan Pulse you agree to these Terms. If you disagree, please leave the site.</p>
    </section>

    <section>
      <h2>2. What MidMan Pulse is</h2>
      <p>MidMan Pulse is an automated news aggregation service. Articles are sourced from publicly available RSS feeds and summarised using AI. We do not claim ownership of third-party content. All articles link to their original publishers.</p>
    </section>

    <section>
      <h2>3. Intellectual property</h2>
      <p>The MidMan Pulse brand, logo, and original site code belong to MidManStudio. Article text and images belong to their respective publishers. AI-generated summaries are derivative works produced for informational purposes under fair use principles.</p>
    </section>

    <section>
      <h2>4. Acceptable use</h2>
      <p>You may not:</p>
      <ul>
        <li>Scrape or bulk-download content for redistribution without permission.</li>
        <li>Use automated tools to overload or attack our servers.</li>
        <li>Attempt unauthorised access to the ingest API or any restricted system.</li>
        <li>Use the site to distribute malware, spam, or illegal content.</li>
      </ul>
    </section>

    <section>
      <h2>5. No financial or professional advice</h2>
      <p>Nothing on MidMan Pulse constitutes financial, legal, medical, or professional advice. Content is for informational purposes only. Always consult a qualified professional before making decisions.</p>
    </section>

    <section>
      <h2>6. Disclaimer of warranties</h2>
      <p>The site is provided "as is" without warranties of any kind. We do not guarantee the accuracy, completeness, or timeliness of any content.</p>
    </section>

    <section>
      <h2>7. Limitation of liability</h2>
      <p>To the maximum extent permitted by applicable law, MidManStudio shall not be liable for any indirect, incidental, consequential, or punitive damages arising from your use of the site.</p>
    </section>

    <section>
      <h2>8. External links</h2>
      <p>We link to third-party websites. We have no control over and accept no responsibility for their content, privacy practices, or availability.</p>
    </section>

    <section>
      <h2>9. Termination</h2>
      <p>We reserve the right to block access to anyone who violates these Terms or who we reasonably believe is harming the site or its users.</p>
    </section>

    <section>
      <h2>10. Changes</h2>
      <p>We may update these Terms at any time. Significant changes will be noted by an updated date above. Continued use after changes constitutes acceptance.</p>
    </section>

    <section>
      <h2>11. Governing law</h2>
      <p>These Terms are governed by the laws of the jurisdiction in which MidManStudio is registered, without regard to conflict-of-law rules.</p>
    </section>

    <section>
      <h2>12. Contact</h2>
      <p>Questions? Email <a href="mailto:legal@midmanstudio.com">legal@midmanstudio.com</a></p>
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
</style>
