/**
 * MidManStudio Editorial Content
 * ─────────────────────────────────────────────────────────────
 * These are hand-crafted articles written and controlled by you.
 * They appear pinned at the top of the homepage above all scraped content.
 *
 * SHOW_EDITORIAL — flip to false to hide all of them instantly.
 * Each item can also be individually hidden with  active: false
 * ─────────────────────────────────────────────────────────────
 */

export const SHOW_EDITORIAL = true;

export type EditorialCategory =
  | 'announcement'
  | 'tool'
  | 'game'
  | 'guide'
  | 'update'
  | 'project';

export interface EditorialArticle {
  /** Shown in the card title */
  title: string;
  /** Short description shown under the title */
  summary: string;
  /** Full URL — can be external or a route on this site */
  link: string;
  /** Opens in new tab if true (default false for internal links) */
  external?: boolean;
  /** Direct URL to an image — use a wide/landscape image (16:9 ideal) */
  image_url?: string;
  /** Shown in the source/byline area — defaults to 'MidManStudio' */
  source?: string;
  /** Badge label — controls the colour chip on the card */
  category: EditorialCategory;
  /** Call-to-action button label — if omitted, defaults to 'Read more' */
  cta?: string;
  /** ISO date string — shown on the card. Defaults to today if omitted */
  date?: string;
  /** Set false to hide this individual article without deleting it */
  active?: boolean;
}

export const EDITORIAL_ARTICLES: EditorialArticle[] = [
  // ── Example: MMS Accounts launch ─────────────────────────────
  {
    title: 'MmS Accounts is live — one identity across every MidManStudio product',
    summary:
      'Sign up once and carry your identity across all current and future MidManStudio games, tools, and services. Free forever.',
    link: 'https://mms-accounts.pages.dev',
    external: true,
    image_url: '', // paste a direct image URL here
    source: 'MidManStudio',
    category: 'announcement',
    cta: 'Create your account',
    date: '2026-04-12',
    active: true,
  },

  // ── Example: a game or tool you want to promote ───────────────
  // {
  //   title: 'DixScript Registry — share and discover .mdix packages',
  //   summary:
  //     'Submit your own DixScript packages to the public cloud registry. Approved packages are available to any DixScript file via from_cloud.',
  //   link: 'https://dixscript-docs.pages.dev',
  //   external: true,
  //   image_url: '',
  //   source: 'MidManStudio',
  //   category: 'tool',
  //   cta: 'Explore the registry',
  //   date: '2026-04-12',
  //   active: false, // flip to true when ready
  // },
];
