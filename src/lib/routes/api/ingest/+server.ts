import { json, error } from '@sveltejs/kit';
import { insertArticle } from '$lib/server/db';
import type { RequestHandler } from './$types';

function slugify(title: string): string {
  return title
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, '')
    .trim()
    .replace(/\s+/g, '-')
    .slice(0, 80);
}

/**
 * Summarize text using the Cloudflare AI binding.
 * Uses @cf/facebook/bart-large-cnn (free on all CF plans, no credit card needed).
 * Falls back to plain truncation if the binding is unavailable.
 */
async function summarize(
  cfAi: any,
  title: string,
  raw: string
): Promise<string> {
  if (!cfAi || !raw) {
    return raw?.slice(0, 300) ?? title;
  }

  try {
    const input = `${title}. ${raw}`.slice(0, 1024);
    const result = await cfAi.run('@cf/facebook/bart-large-cnn', {
      input_text: input,
      max_length: 130,
    });
    return (result?.summary ?? '').trim() || raw.slice(0, 300);
  } catch (err) {
    console.warn('CF AI summarization failed, using truncation:', err);
    return raw.slice(0, 300);
  }
}

export const POST: RequestHandler = async ({ request, platform }) => {
  // ── auth ──────────────────────────────────────────────────────────────────
  const secret     = platform?.env?.INGEST_SECRET;
  const authHeader = request.headers.get('Authorization') ?? '';
  const provided   = authHeader.startsWith('Bearer ')
    ? authHeader.slice(7).trim()
    : '';

  if (!secret || provided !== secret) {
    throw error(401, 'Unauthorized');
  }

  // ── db / ai ───────────────────────────────────────────────────────────────
  const db   = platform?.env?.DB;
  const cfAi = platform?.env?.CF_AI;

  if (!db) throw error(500, 'Database unavailable');

  // ── body ──────────────────────────────────────────────────────────────────
  let body: any;
  try {
    body = await request.json();
  } catch {
    throw error(400, 'Invalid JSON');
  }

  const articles = Array.isArray(body) ? body : [body];
  const results  = [];

  for (const item of articles) {
    // Either a pre-built summary OR raw_content to summarize
    const hasSummary = typeof item.summary === 'string' && item.summary.trim().length > 0;
    const hasRaw     = typeof item.raw_content === 'string' && item.raw_content.trim().length > 0;

    if (!item.title || (!hasSummary && !hasRaw) || !item.source_url || !item.source_name || !item.category) {
      results.push({ ok: false, reason: 'Missing required fields', item: item.title });
      continue;
    }

    // Build summary — prefer existing, otherwise ask CF AI
    const summary = hasSummary
      ? item.summary
      : await summarize(cfAi, item.title, item.raw_content);

    const slug = `${slugify(item.title)}-${Date.now().toString(36)}`;

    try {
      const result = await insertArticle(db, {
        slug,
        title:        item.title,
        summary,
        content:      item.content ?? null,
        source_url:   item.source_url,
        source_name:  item.source_name,
        category:     item.category,
        image_url:    item.image_url ?? null,
        published_at: item.published_at ?? new Date().toISOString(),
        is_featured:  item.is_featured ? 1 : 0,
        tags:         item.tags ?? [],
      });

      results.push({ ok: true, inserted: result.inserted, slug });
    } catch (err) {
      results.push({ ok: false, reason: String(err), item: item.title });
    }
  }

  return json({ results });
};
