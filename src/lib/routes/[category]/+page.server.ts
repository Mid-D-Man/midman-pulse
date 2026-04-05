import { error } from '@sveltejs/kit';
import { getArticles, getCategories } from '$lib/server/db';
import type { PageServerLoad } from './$types';

const VALID_CATEGORIES = ['ai', 'cybersecurity', 'business'];

export const load: PageServerLoad = async ({ params, platform, url }) => {
  if (!VALID_CATEGORIES.includes(params.category)) {
    throw error(404, 'Category not found');
  }

  const db = platform?.env?.DB;
  if (!db) throw error(500, 'Database unavailable');

  const page = Number(url.searchParams.get('page') ?? '1');

  const [articles, categories] = await Promise.all([
    getArticles(db, { category: params.category, page, per_page: 12 }),
    getCategories(db),
  ]);

  const category = categories.find((c: any) => c.slug === params.category);
  if (!category) throw error(404, 'Category not found');

  return { articles, category, categories, currentPage: page };
};
