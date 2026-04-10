import os
import re
import datetime
import requests
from xml.etree import ElementTree

INGEST_URL    = os.environ["INGEST_URL"]
INGEST_SECRET = os.environ["INGEST_SECRET"]

FEEDS = [
    # ── Cybersecurity ─────────────────────────────────────────────
    {
        "url": "https://feeds.feedburner.com/TheHackersNews",
        "source_name": "The Hacker News",
        "category": "cybersecurity",
    },
    {
        "url": "https://www.darkreading.com/rss.xml",
        "source_name": "Dark Reading",
        "category": "cybersecurity",
    },
    {
        "url": "https://www.wired.com/feed/category/security/latest/rss",
        "source_name": "Wired Security",
        "category": "cybersecurity",
    },

    # ── Agentic AI ────────────────────────────────────────────────
    {
        "url": "https://techcrunch.com/category/artificial-intelligence/feed/",
        "source_name": "TechCrunch AI",
        "category": "ai",
    },
    {
        "url": "https://www.wired.com/feed/tag/artificial-intelligence/latest/rss",
        "source_name": "Wired AI",
        "category": "ai",
    },

    # ── Business ──────────────────────────────────────────────────
    {
        "url": "https://feeds.feedburner.com/entrepreneur/latest",
        "source_name": "Entrepreneur",
        "category": "business",
    },
    {
        "url": "https://www.wired.com/feed/category/business/latest/rss",
        "source_name": "Wired Business",
        "category": "business",
    },

    # ── Game Dev ──────────────────────────────────────────────────
    {
        "url": "https://www.gamedeveloper.com/rss.xml",
        "source_name": "Game Developer",
        "category": "gamedev",
    },
    {
        "url": "https://www.gamesindustry.biz/feed",
        "source_name": "GamesIndustry.biz",
        "category": "gamedev",
    },
    {
        "url": "https://www.rockpapershotgun.com/feed",
        "source_name": "Rock Paper Shotgun",
        "category": "gamedev",
    },
]

NAMESPACES = {
    "atom":    "http://www.w3.org/2005/Atom",
    "media":   "http://search.yahoo.com/mrss/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc":      "http://purl.org/dc/elements/1.1/",
    "itunes":  "http://www.itunes.com/dtds/podcast-1.0.dtd",
}


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    for entity, char in [
        ("&nbsp;", " "), ("&amp;", "&"), ("&lt;", "<"),
        ("&gt;", ">"), ("&quot;", '"'), ("&#39;", "'"),
    ]:
        text = text.replace(entity, char)
    return re.sub(r"\s+", " ", text).strip()


def get_text(item, tag: str) -> str:
    """Safe text — never uses Element truthiness."""
    el = item.find(tag)
    if el is None:
        for uri in NAMESPACES.values():
            el = item.find(f"{{{uri}}}{tag}")
            if el is not None:
                break
    if el is None:
        return ""
    return (el.text or "").strip()


def get_link(item) -> str:
    el = item.find("link")
    if el is not None and el.text and el.text.strip().startswith("http"):
        return el.text.strip()
    for uri in [NAMESPACES["atom"], ""]:
        tag = f"{{{uri}}}link" if uri else "link"
        for el in item.findall(tag):
            href = el.get("href", "").strip()
            if href.startswith("http"):
                return href
    el = item.find("guid")
    if el is not None and el.text and el.text.strip().startswith("http"):
        return el.text.strip()
    return ""


def get_image(item) -> str:
    for el in item.findall(f"{{{NAMESPACES['media']}}}content"):
        url = el.get("url", "")
        if url and (el.get("medium") == "image" or
                    url.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))):
            return url
    el = item.find(f"{{{NAMESPACES['media']}}}thumbnail")
    if el is not None and el.get("url"):
        return el.get("url")
    el = item.find("enclosure")
    if el is not None and "image" in el.get("type", "") and el.get("url"):
        return el.get("url")
    el = item.find(f"{{{NAMESPACES['itunes']}}}image")
    if el is not None:
        url = el.get("href", "") or (el.text or "")
        if url:
            return url.strip()
    raw = get_text(item, "description") or get_text(item, "summary")
    m = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', raw, re.IGNORECASE)
    if m and m.group(1).startswith("http"):
        return m.group(1)
    return ""


def parse_feed(feed: dict) -> list:
    for prefix, uri in NAMESPACES.items():
        try:
            ElementTree.register_namespace(prefix, uri)
        except Exception:
            pass

    try:
        resp = requests.get(
            feed["url"],
            timeout=15,
            headers={"User-Agent": "MidManPulse/1.0"},
        )
        resp.raise_for_status()
    except Exception as e:
        print(f"  [SKIP] Fetch error: {e}")
        return []

    try:
        root = ElementTree.fromstring(resp.content)
    except Exception as e:
        print(f"  [SKIP] XML parse error: {e}")
        return []

    items = (
        root.findall(".//item")
        or root.findall(f".//{{{NAMESPACES['atom']}}}entry")
    )
    print(f"  Found {len(items)} items")

    articles = []
    for item in items[:5]:
        title = get_text(item, "title")
        link  = get_link(item)

        if not title or not link:
            print(f"  [SKIP] title={repr(title[:50])} link={repr(link[:50])}")
            continue

        raw   = (get_text(item, "description")
                 or get_text(item, "summary")
                 or get_text(item, f"{{{NAMESPACES['content']}}}encoded")
                 or "")
        clean   = strip_html(raw)[:800]
        summary = clean[:300] if len(clean) >= 30 else f"{title} — via {feed['source_name']}."
        image   = get_image(item) or None

        pub_raw      = get_text(item, "pubDate") or get_text(item, "published") or ""
        published_at = datetime.datetime.utcnow().isoformat()
        for fmt in (
            "%a, %d %b %Y %H:%M:%S %z",
            "%a, %d %b %Y %H:%M:%S GMT",
            "%Y-%m-%dT%H:%M:%S%z",
            "%Y-%m-%dT%H:%M:%SZ",
        ):
            try:
                published_at = datetime.datetime.strptime(pub_raw.strip(), fmt).isoformat()
                break
            except Exception:
                continue

        articles.append({
            "title":        title,
            "summary":      summary,
            "raw_content":  clean,
            "source_url":   link,
            "source_name":  feed["source_name"],
            "category":     feed["category"],
            "image_url":    image,
            "published_at": published_at,
            "is_featured":  False,
            "tags":         [feed["category"]],
        })

    return articles


def main():
    all_articles = []
    for feed in FEEDS:
        print(f"\nFetching: {feed['source_name']} [{feed['category']}]")
        articles = parse_feed(feed)
        all_articles.extend(articles)
        print(f"  Collected {len(articles)} articles")

    print(f"\nTotal to ingest: {len(all_articles)}")
    if not all_articles:
        print("Nothing to send.")
        return

    resp = requests.post(
        INGEST_URL,
        json=all_articles,
        headers={
            "Authorization": f"Bearer {INGEST_SECRET}",
            "Content-Type": "application/json",
        },
        timeout=30,
    )

    print(f"Ingest HTTP {resp.status_code}")
    try:
        data     = resp.json()
        results  = data.get("results", [])
        inserted = sum(1 for r in results if r.get("ok") and r.get("inserted"))
        skipped  = sum(1 for r in results if r.get("ok") and not r.get("inserted"))
        failed   = sum(1 for r in results if not r.get("ok"))
        print(f"  Inserted: {inserted}  |  Duplicate: {skipped}  |  Failed: {failed}")
        for r in results:
            if not r.get("ok"):
                print(f"  [FAIL] {r.get('item')} — {r.get('reason')}")
    except Exception:
        print(resp.text)


if __name__ == "__main__":
    main()
