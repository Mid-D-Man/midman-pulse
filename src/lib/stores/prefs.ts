import { browser } from '$app/environment';
import { writable, derived } from 'svelte/store';
import type { Article } from '$lib/types';

// ── Types ──────────────────────────────────────────────────────────────────

export interface BookmarkedArticle {
  slug:         string;
  title:        string;
  summary:      string;
  source_name:  string;
  source_url:   string;
  category:     string;
  published_at: string;
  image_url:    string | null;
  savedAt:      number;
}

interface PrefsState {
  bookmarks:        Record<string, BookmarkedArticle>;
  readHistory:      Record<string, number>;   // slug → timestamp
  hiddenCategories: string[];
  categoryOrder:    string[];                 // ordered array of slugs
}

// ── Defaults ───────────────────────────────────────────────────────────────

const DEFAULT: PrefsState = {
  bookmarks:        {},
  readHistory:      {},
  hiddenCategories: [],
  categoryOrder:    [],
};

const STORAGE_KEY = 'mmp-prefs';

// ── Persistence ────────────────────────────────────────────────────────────

function load(): PrefsState {
  if (!browser) return DEFAULT;
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return DEFAULT;
    return { ...DEFAULT, ...JSON.parse(raw) };
  } catch {
    return DEFAULT;
  }
}

function save(state: PrefsState): PrefsState {
  if (browser) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch {
      // localStorage full or unavailable — fail silently
    }
  }
  return state;
}

// ── Store factory ──────────────────────────────────────────────────────────

function createPrefs() {
  const { subscribe, update } = writable<PrefsState>(load());

  return {
    subscribe,

    // ── Bookmarks ──────────────────────────────────────────────────────────

    toggleBookmark(article: Article) {
      update(state => {
        const exists = !!state.bookmarks[article.slug];
        if (exists) {
          const { [article.slug]: _removed, ...rest } = state.bookmarks;
          return save({ ...state, bookmarks: rest });
        }
        return save({
          ...state,
          bookmarks: {
            ...state.bookmarks,
            [article.slug]: {
              slug:         article.slug,
              title:        article.title,
              summary:      article.summary,
              source_name:  article.source_name,
              source_url:   article.source_url,
              category:     article.category,
              published_at: article.published_at,
              image_url:    article.image_url,
              savedAt:      Date.now(),
            },
          },
        });
      });
    },

    removeBookmark(slug: string) {
      update(state => {
        const { [slug]: _removed, ...rest } = state.bookmarks;
        return save({ ...state, bookmarks: rest });
      });
    },

    clearBookmarks() {
      update(state => save({ ...state, bookmarks: {} }));
    },

    // ── Read history ───────────────────────────────────────────────────────

    markRead(slug: string) {
      update(state => {
        if (state.readHistory[slug]) return state;  // already marked
        return save({
          ...state,
          readHistory: { ...state.readHistory, [slug]: Date.now() },
        });
      });
    },

    clearHistory() {
      update(state => save({ ...state, readHistory: {} }));
    },

    // ── Category preferences ───────────────────────────────────────────────

    toggleHideCategory(slug: string) {
      update(state => {
        const hidden = state.hiddenCategories.includes(slug)
          ? state.hiddenCategories.filter(s => s !== slug)
          : [...state.hiddenCategories, slug];
        return save({ ...state, hiddenCategories: hidden });
      });
    },

    moveCategoryUp(slug: string, allSlugs: string[]) {
      update(state => {
        const order  = state.categoryOrder.length ? [...state.categoryOrder] : [...allSlugs];
        const index  = order.indexOf(slug);
        if (index <= 0) return state;
        [order[index - 1], order[index]] = [order[index], order[index - 1]];
        return save({ ...state, categoryOrder: order });
      });
    },

    moveCategoryDown(slug: string, allSlugs: string[]) {
      update(state => {
        const order = state.categoryOrder.length ? [...state.categoryOrder] : [...allSlugs];
        const index = order.indexOf(slug);
        if (index === -1 || index >= order.length - 1) return state;
        [order[index], order[index + 1]] = [order[index + 1], order[index]];
        return save({ ...state, categoryOrder: order });
      });
    },

    resetCategoryPrefs() {
      update(state => save({ ...state, hiddenCategories: [], categoryOrder: [] }));
    },
  };
}

export const prefs = createPrefs();

// ── Derived helpers ────────────────────────────────────────────────────────

/** Number of saved bookmarks — used for nav badge */
export const bookmarkCount = derived(
  prefs,
  $p => Object.keys($p.bookmarks).length
);

/** Bookmarks as a sorted array (newest saved first) */
export const bookmarkList = derived(
  prefs,
  $p => Object.values($p.bookmarks).sort((a, b) => b.savedAt - a.savedAt)
);

/**
 * Apply user category preferences to a raw categories array.
 * Returns categories sorted by user order, with hidden ones filtered out.
 */
export function applyUserCategoryPrefs<T extends { slug: string }>(
  categories: T[],
  state: PrefsState
): T[] {
  const order = state.categoryOrder;

  const sorted = order.length
    ? [...categories].sort((a, b) => {
        const ai = order.indexOf(a.slug);
        const bi = order.indexOf(b.slug);
        if (ai === -1 && bi === -1) return 0;
        if (ai === -1) return 1;
        if (bi === -1) return -1;
        return ai - bi;
      })
    : categories;

  return sorted.filter(c => !state.hiddenCategories.includes(c.slug));
}
