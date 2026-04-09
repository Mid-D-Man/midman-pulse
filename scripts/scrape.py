import os
import re
import datetime
import requests
from xml.etree import ElementTree

INGEST_URL    = os.environ["INGEST_URL"]
INGEST_SECRET = os.environ["INGEST_SECRET"]

FEEDS = [
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
        "url": "https://techcrunch.com/category/artificial-intelligence/feed/",
        "source_name": "TechCrunch AI",
        "category": "ai",
    },
    {
        "url": "https://feeds.feedburner.com/entrepreneur/latest",
        "source_name": "Entrepreneur",
        "category": "business",
    },
    {
        "url": "https://feeds.harvardbusiness.org/harvardbusiness",
        "source_name": "Harvard Business Review",
        "category": "business",
    },
]


def strip_html(text: str) -> str:
    """Remove HTML tags and decode common entities."""
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("&nbsp;", " ")
    text = text.replace("&amp;", "&")
    text = text.replace("&lt;", "<")
    text = text.replace("&gt;", ">")
    text = text.replace("&quot;", '"')
    text = text.replace("&#39;", "'")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def parse_feed(feed: dict) -> list:
    try:
        resp = requests.get(
            feed["url"],
            timeout=15,
            headers={"User-Agent": "MidManPulse/1.0"},
        )
        resp.raise_for_status()
    except Exception as e:
        print(f"  [SKIP] Failed to fetch {feed['url']}: {e}")
        return []

    try:
        root = ElementTree.fromstring(resp.content)
    except Exception as e:
        print(f"  [SKIP] Failed to parse XML: {e}")
        return []

    ns    = {"atom": "http://www.w3.org/2005/Atom"}
    items = root.findall(".//item") or root.findall(".//atom:entry", ns)
    print(f"  Found {len(items)} items")

    articles = []
    for item in items[:5]:

        def get(tag: str) -> str:
            el = item.find(tag) or item.find(f"atom:{tag}", ns)
            if el is None:
                return ""
            # Some feeds put content in CDATA — el.text captures that
            return (el.text or "").strip()

        title = get("title")
        link  = get("link")

        # Some Atom feeds put link in href attribute
        if not link:
            link_el = item.find("link") or item.find("atom:link", ns)
            if link_el is not None:
                link = link_el.get("href", "")

        if not title or not link:
            print(f"  [SKIP] Missing title or link")
            continue

        # Try multiple content fields
        raw = (
            get("description")
            or get("summary")
            or get("content:encoded")
            or get("content")
            or ""
        )
        clean = strip_html(raw)[:800]

        # Build a summary: prefer cleaned content, fall back to title
        if len(clean) >= 30:
            summary = clean[:300]
        else:
            summary = f"{title} — Latest news from {feed['source_name']}."

        # Parse date
        pub_raw = get("pubDate") or get("published") or get("updated") or ""
        published_at = datetime.datetime.utcnow().isoformat()
        for fmt in (
            "%a, %d %b %Y %H:%M:%S %z",
            "%a, %d %b %Y %H:%M:%S GMT",
            "%Y-%m-%dT%H:%M:%S%z",
            "%Y-%m-%dT%H:%M:%SZ",
        ):
            try:
                published_at = datetime.datetime.strptime(pub_raw, fmt).isoformat()
                break
            except Exception:
                continue

        articles.append(
            {
                "title":        title,
                "summary":      summary,       # pre-built — server won't need to call CF AI
                "raw_content":  clean,         # still sent so CF AI can improve it if available
                "source_url":   link,
                "source_name":  feed["source_name"],
                "category":     feed["category"],
                "published_at": published_at,
                "is_featured":  False,
                "tags":         [feed["category"]],
            }
        )

    return articles


def main():
    all_articles = []
    for feed in FEEDS:
        print(f"\nFetching: {feed['source_name']}")
        articles = parse_feed(feed)
        all_articles.extend(articles)
        print(f"  Collected {len(articles)} articles")

    print(f"\nTotal articles to ingest: {len(all_articles)}")

    if not all_articles:
        print("No articles collected — nothing to send.")
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

    print(f"\nIngest HTTP status: {resp.status_code}")
    try:
        data = resp.json()
        results = data.get("results", [])
        inserted = sum(1 for r in results if r.get("ok") and r.get("inserted"))
        skipped  = sum(1 for r in results if r.get("ok") and not r.get("inserted"))
        failed   = sum(1 for r in results if not r.get("ok"))
        print(f"  Inserted: {inserted}")
        print(f"  Skipped (duplicate): {skipped}")
        print(f"  Failed: {failed}")
        for r in results:
            if not r.get("ok"):
                print(f"  [FAIL] {r.get('item')} — {r.get('reason')}")
    except Exception:
        print(resp.text)


if __name__ == "__main__":
    main()
