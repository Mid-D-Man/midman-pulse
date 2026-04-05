import { getCategories } from '$lib/server/db';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ platform }) => {
  const db = platform?.env?.DB;
  if (!db) return { categories: [] };

  const categories = await getCategories(db);
  return { categories };
};
