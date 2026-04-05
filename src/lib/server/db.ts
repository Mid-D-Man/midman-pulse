export const SCHEMA = `
  CREATE TABLE IF NOT EXISTS mmp_categories (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    slug        TEXT    NOT NULL UNIQUE,
    label       TEXT    NOT NULL,
    description TEXT
  );

  CREATE TABLE IF NOT EXISTS mmp_articles (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    slug         TEXT    NOT NULL UNIQUE,
    title        TEXT    NOT NULL,
    summary      TEXT    NOT NULL,
    content      TEXT,
    source_url   TEXT    NOT NULL,
    source_name  TEXT    NOT NULL,
    category     TEXT    NOT NULL REFERENCES mmp_categories(slug),
    image_url    TEXT,
    published_at TEXT    NOT NULL,
    created_at   TEXT    NOT NULL DEFAULT (datetime('now')),
    is_featured  INTEGER NOT NULL DEFAULT 0
  );

  CREATE TABLE IF NOT EXISTS mmp_article_tags (
    article_id INTEGER NOT NULL REFERENCES mmp_articles(id) ON DELETE CASCADE,
    tag        TEXT    NOT NULL,
    PRIMARY KEY (article_id, tag)
  );

  CREATE INDEX IF NOT EXISTS mmp_articles_category    ON mmp_articles(category);
  CREATE INDEX IF NOT EXISTS mmp_articles_published   ON mmp_articles(published_at DESC);
  CREATE INDEX IF NOT EXISTS mmp_articles_featured    ON mmp_articles(is_featured);
  CREATE INDEX IF NOT EXISTS mmp_tags_article         ON mmp_article_tags(article_id);

  INSERT OR IGNORE INTO mmp_categories (slug, label, description) VALUES
    ('ai',           'Agentic AI',    'Autonomous AI agents, LLMs, and AI-driven automation'),
    ('cybersecurity','Cybersecurity', 'Threat intelligence, security tools, and audits'),
    ('business',     'Business',      'Arbitrage, prediction markets, and profit automation');
`;

export async function getArticles(
  db: D1Database,
  options: {
    category?: string;
    page?: number;
    per_page?: number;
    featured?: boolean;
  } = {}
) {
  const page     = options.page     ?? 1;
  const per_page = options.per_page ?? 12;
  const offset   = (page - 1) * per_page;

  let where = '1=1';
  const params: (string | number)[] = [];

  if (options.category) {
    where += ' AND a.category = ?';
    params.push(options.category);
  }

  if (options.featured) {
    where += ' AND a.is_featured = 1';
  }

  const countResult = await db
    .prepare(`SELECT COUNT(*) as total FROM mmp_articles a WHERE ${where}`)
    .bind(...params)
    .first<{ total: number }>();

  const total = countResult?.total ?? 0;

  const articles = await db
    .prepare(
      `SELECT a.* FROM mmp_articles a
       WHERE ${where}
       ORDER BY a.published_at DESC
       LIMIT ? OFFSET ?`
    )
    .bind(...params, per_page, offset)
    .all();

  return {
    articles: articles.results,
    total,
    page,
    per_page,
    has_more: offset + per_page < total,
  };
}

export async function getArticleBySlug(db: D1Database, slug: string) {
  return db
    .prepare('SELECT * FROM mmp_articles WHERE slug = ?')
    .bind(slug)
    .first();
}

export async function getCategories(db: D1Database) {
  const result = await db
    .prepare('SELECT * FROM mmp_categories ORDER BY label ASC')
    .all();
  return result.results;
}

export async function getArticleTags(db: D1Database, articleId: number) {
  const result = await db
    .prepare('SELECT tag FROM mmp_article_tags WHERE article_id = ?')
    .bind(articleId)
    .all();
  return result.results.map((r: any) => r.tag as string);
}

export async function insertArticle(
  db: D1Database,
  article: {
    slug: string;
    title: string;
    summary: string;
    content?: string;
    source_url: string;
    source_name: string;
    category: string;
    image_url?: string;
    published_at: string;
    is_featured?: number;
    tags?: string[];
  }
) {
  const existing = await db
    .prepare('SELECT id FROM mmp_articles WHERE slug = ?')
    .bind(article.slug)
    .first<{ id: number }>();

  if (existing) return { inserted: false, id: existing.id };

  const result = await db
    .prepare(
      `INSERT INTO mmp_articles
        (slug, title, summary, content, source_url, source_name, category, image_url, published_at, is_featured)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
    )
    .bind(
      article.slug,
      article.title,
      article.summary,
      article.content ?? null,
      article.source_url,
      article.source_name,
      article.category,
      article.image_url ?? null,
      article.published_at,
      article.is_featured ?? 0
    )
    .run();

  const id = result.meta.last_row_id;

  if (article.tags?.length) {
    const tagInserts = article.tags.map((tag) =>
      db
        .prepare('INSERT OR IGNORE INTO mmp_article_tags (article_id, tag) VALUES (?, ?)')
        .bind(id, tag)
    );
    await db.batch(tagInserts);
  }

  return { inserted: true, id };
    }
