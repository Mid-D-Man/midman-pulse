export interface Article {
  id: number;
  slug: string;
  title: string;
  summary: string;
  content: string | null;
  source_url: string;
  source_name: string;
  category: string;
  image_url: string | null;
  published_at: string;
  created_at: string;
  is_featured: number;
}

export interface Category {
  id: number;
  slug: string;
  label: string;
  description: string | null;
}

export interface ArticleTag {
  article_id: number;
  tag: string;
}

export type CategorySlug = 'ai' | 'cybersecurity' | 'business' | 'gamedev';

export interface PaginatedArticles {
  articles: Article[];
  total: number;
  page: number;
  per_page: number;
  has_more: boolean;
}
