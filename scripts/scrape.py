import os
import datetime
import requests
from xml.etree import ElementTree

INGEST_URL = os.environ["INGEST_URL"]
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
        "url": "https://venturebeat.com/ai/feed/",
        "source_name": "VentureBeat AI",
        "category": "ai",
    },
    {
        "url": "https://feeds.feedburner.com/entrepreneur/latest",
        "source_name": "Entrepreneur",
        "category": "business",
    },
]


def parse_feed(feed: dict) -> list:
    try:
        resp = requests.get(feed["url"], timeout=10, headers={"User-Agent": "MidManPulse/1.0"})
        resp.raise_for_status()
    except Exception as e:
        print(f"Failed to fetch {feed['url']}: {e}")
        return []

    try:
        root = ElementTree.fromstring(resp.content)
    except Exception as e:
        print(f"Failed to parse XML from {feed['url']}: {e}")
        return []

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    items = root.findall(".//item") or root.findall(".//atom:entry", ns)

    articles = []
    for item in items[:5]:
        def get(tag: str) -> str:
            el = item.find(tag) or item.find(f"atom:{tag}", ns)
            return (el.text or "").strip() if el is not None else ""

        title = get("title")
        link  = get("link")
        raw   = get("description") or get("summary") or get("content") or ""

        if not title or not link:
            continue

        pub_raw = get("pubDate") or get("published") or get("updated")
        try:
            published_at = datetime.datetime.strptime(
                pub_raw, "%a, %d %b %Y %H:%M:%S %z"
            ).isoformat()
        except Exception:
            published_at = datetime.datetime.utcnow().isoformat()

        # Strip basic HTML tags from raw content for cleaner summarization
        import re
        clean_raw = re.sub(r"<[^>]+>", " ", raw).strip()
        clean_raw = re.sub(r"\s+", " ", clean_raw)[:1000]

        articles.append(
            {
                "title":       title,
                "raw_content": clean_raw,   # server will summarize via CF AI
                "source_url":  link,
                "source_name": feed["source_name"],
                "category":    feed["category"],
                "published_at": published_at,
                "is_featured": False,
                "tags":        [feed["category"]],
            }
        )

    return articles


def main():
    all_articles = []
    for feed in FEEDS:
        print(f"Fetching: {feed['source_name']}")
        articles = parse_feed(feed)
        all_articles.extend(articles)
        print(f"  Got {len(articles)} articles")

    if not all_articles:
        print("No articles collected.")
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

    print(f"Ingest status: {resp.status_code}")
    try:
        print(resp.json())
    except Exception:
        print(resp.text)


if __name__ == "__main__":
    main()
