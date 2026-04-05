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

export const POST: RequestHandler = async ({ request, platform }) => {
  const secret = platform?.env?.INGEST_SECRET;
  const authHeader = request.headers.get('Authorization') ?? '';
  const provided = authHeader.startsWith('Bearer ') ? authHeader.slice(7).trim() : '';

  if (!secret || provided !== secret) {
    throw error(401, 'Unauthorized');
  }

  const db = platform?.env?.DB;
  if (!db) throw error(500, 'Database unavailable');

  let body: any;
  try {
    body = await request.json();
  } catch {
    throw error(400, 'Invalid JSON');
  }

  const articles = Array.isArray(body) ? body : [body];

  const results = [];

  for (const item of articles) {
    if (!item.title || !item.summary || !item.source_url || !item.source_name || !item.category) {
      results.push({ ok: false, reason: 'Missing required fields', item: item.title });
      continue;
    }

    const slug = `${slugify(item.title)}-${Date.now().toString(36)}`;

    try {
      const result = await insertArticle(db, {
        slug,
        title:        item.title,
        summary:      item.summary,
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
