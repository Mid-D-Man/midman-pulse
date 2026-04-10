<script lang="ts">
  const year = new Date().getFullYear();
</script>

<footer class="footer">
  <div class="footer-inner container">
    <div class="footer-brand">
      <span class="brand-name">MidMan<span class="brand-accent">Pulse</span></span>
      <p class="footer-tagline">Curated intelligence. Updated continuously.</p>
    </div>
    <div class="footer-links">
      <a href="/ai">Agentic AI</a>
      <a href="/cybersecurity">Cybersecurity</a>
      <a href="/business">Business</a>
      <a href="/gamedev">Game Dev</a>
    </div>
    <p class="footer-copy">&copy; {year} MidManStudio. All rights reserved.</p>
  </div>
</footer>

<style>
  .footer {
    border-top: 1px solid var(--border);
    background: var(--bg-surface);
    padding: 2rem 0;
    margin-top: auto;
  }

  .footer-inner {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    align-items: center;
    text-align: center;
  }

  .brand-name { font-size: 1rem; font-weight: 700; color: var(--text); }
  .brand-accent { color: var(--accent); }

  .footer-tagline { font-size: 0.8125rem; color: var(--text-muted); margin-top: 0.25rem; }

  .footer-links { display: flex; gap: 1.5rem; flex-wrap: wrap; justify-content: center; }

  .footer-links a {
    font-size: 0.875rem;
    color: var(--text-muted);
    text-decoration: none;
    transition: color 0.15s;
  }

  .footer-links a:hover { color: var(--accent); }

  .footer-copy { font-size: 0.75rem; color: var(--text-muted); }
</style>
