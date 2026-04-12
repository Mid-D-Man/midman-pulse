<script lang="ts">
  const year = new Date().getFullYear();
</script>

<footer class="footer">
  <div class="footer-inner container">

    <div class="footer-top">
      <div class="footer-brand">
        <span class="brand-name">MidMan<span class="brand-accent">Pulse</span></span>
        <p class="footer-tagline">Curated intelligence. Updated continuously.</p>
      </div>

      <nav class="footer-nav" aria-label="Footer navigation">
        <div class="footer-nav-col">
          <span class="footer-nav-heading">Categories</span>
          <a href="/ai">Agentic AI</a>
          <a href="/cybersecurity">Cybersecurity</a>
          <a href="/business">Business</a>
          <a href="/gamedev">Game Dev</a>
        </div>
        <div class="footer-nav-col">
          <span class="footer-nav-heading">Legal</span>
          <a href="/privacy">Privacy Policy</a>
          <a href="/terms">Terms of Service</a>
          <a href="/cookies">Cookie Policy</a>
        </div>
      </nav>
    </div>

    <div class="footer-bottom">
      <p class="footer-copy">&copy; {year} MidManStudio. All rights reserved.</p>
      <div class="footer-legal-links">
        <a href="/privacy">Privacy</a>
        <span class="footer-sep" aria-hidden="true">·</span>
        <a href="/terms">Terms</a>
        <span class="footer-sep" aria-hidden="true">·</span>
        <a href="/cookies">Cookies</a>
      </div>
    </div>

  </div>
</footer>

<style>
  .footer {
    border-top: 1px solid var(--border);
    background: var(--bg-surface);
    padding: 2.5rem 0 1.5rem;
    margin-top: auto;
  }

  .footer-top {
    display: flex;
    justify-content: space-between;
    gap: 2rem;
    flex-wrap: wrap;
    margin-bottom: 2rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid var(--border);
  }

  .footer-brand { display: flex; flex-direction: column; gap: 0.375rem; }

  .brand-name   { font-size: 1rem; font-weight: 700; color: var(--text); }
  .brand-accent { color: var(--accent); }

  .footer-tagline { font-size: 0.8125rem; color: var(--text-muted); max-width: 220px; line-height: 1.6; }

  /* ── Nav columns ── */
  .footer-nav { display: flex; gap: 3rem; flex-wrap: wrap; }

  .footer-nav-col {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .footer-nav-heading {
    font-size: 0.6875rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--text-muted);
    font-family: var(--font-mono);
    margin-bottom: 0.25rem;
  }

  .footer-nav-col a {
    font-size: 0.875rem;
    color: var(--text-muted);
    text-decoration: none;
    transition: color 0.15s;
  }

  .footer-nav-col a:hover { color: var(--accent); }

  /* ── Bottom bar ── */
  .footer-bottom {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    flex-wrap: wrap;
  }

  .footer-copy { font-size: 0.75rem; color: var(--text-muted); }

  .footer-legal-links {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .footer-legal-links a {
    font-size: 0.75rem;
    color: var(--text-muted);
    text-decoration: none;
    transition: color 0.15s;
  }

  .footer-legal-links a:hover { color: var(--accent); }

  .footer-sep { color: var(--border); font-size: 0.75rem; }

  /* ── Responsive ── */
  @media (max-width: 640px) {
    .footer-top     { flex-direction: column; }
    .footer-nav     { gap: 1.5rem; }
    .footer-bottom  { flex-direction: column; align-items: flex-start; gap: 0.5rem; }
  }
</style>
