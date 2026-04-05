import { error } from '@sveltejs/kit';
import { getArticleBySlug, getArticleTags, getArticles } from '$lib/server/db';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params, platform }) => {
  const db = platform?.env?.DB;
  if (!db) throw error(500, 'Database unavailable');

  const article = await getArticleBySlug(db, params.slug);
  if (!article) throw error(404, 'Article not found');

  const [tags, related] = await Promise.all([
    getArticleTags(db, (article as any).id),
    getArticles(db, {
      category: (article as any).category,
      per_page: 3,
    }),
  ]);

  const relatedFiltered = (related.articles as any[]).filter(
    (a) => a.slug !== params.slug
  ).slice(0, 3);

  return { article, tags, related: relatedFiltered };
};
