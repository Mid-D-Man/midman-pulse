import { getArticles } from '$lib/server/db';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ platform, url }) => {
  const db = platform?.env?.DB;
  if (!db) return { featured: [], recent: { articles: [], total: 0, page: 1, per_page: 9, has_more: false } };

  const page = Number(url.searchParams.get('page') ?? '1');

  const [featured, recent] = await Promise.all([
    getArticles(db, { featured: true, per_page: 3 }),
    getArticles(db, { page, per_page: 9 }),
  ]);

  return {
    featured: featured.articles,
    recent,
  };
};
