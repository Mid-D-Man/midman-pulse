import os
import json
import hashlib
import datetime
import requests
from xml.etree import ElementTree

INGEST_URL = os.environ["INGEST_URL"]
INGEST_SECRET = os.environ["INGEST_SECRET"]
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

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

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-1.5-flash:generateContent?key=" + GEMINI_API_KEY
)


def summarize(title: str, raw_summary: str) -> str:
    if not GEMINI_API_KEY:
        return raw_summary[:300]

    prompt = (
        f"Write a 2-3 sentence factual summary of this article. "
        f"Be direct and informative. Do not editorialize.\n\n"
        f"Title: {title}\nContent: {raw_summary}"
    )

    try:
        resp = requests.post(
            GEMINI_URL,
            json={"contents": [{"parts": [{"text": prompt}]}]},
            timeout=15,
        )
        data = resp.json()
        return data["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception:
        return raw_summary[:300]


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
        link = get("link")
        raw = get("description") or get("summary") or get("content")

        if not title or not link:
            continue

        summary = summarize(title, raw)

        pub_raw = get("pubDate") or get("published") or get("updated")
        try:
            published_at = datetime.datetime.strptime(
                pub_raw, "%a, %d %b %Y %H:%M:%S %z"
            ).isoformat()
        except Exception:
            published_at = datetime.datetime.utcnow().isoformat()

        articles.append(
            {
                "title": title,
                "summary": summary,
                "source_url": link,
                "source_name": feed["source_name"],
                "category": feed["category"],
                "published_at": published_at,
                "is_featured": False,
                "tags": [feed["category"]],
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
    print(resp.json())


if __name__ == "__main__":
    main()
