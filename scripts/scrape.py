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
]


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("&nbsp;", " ")
    text = text.replace("&amp;", "&")
    text = text.replace("&lt;", "<")
    text = text.replace("&gt;", ">")
    text = text.replace("&quot;", '"')
    text = text.replace("&#39;", "'")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def get_text(item, tag: str, ns: dict) -> str:
    """
    Safely get text from an XML element.
    Uses explicit None check — never relies on Element truthiness,
    which is False for leaf elements even when they have text.
    """
    el = item.find(tag)
    if el is None:
        el = item.find(f"atom:{tag}", ns)
    if el is None:
        return ""
    return (el.text or "").strip()


def get_link(item, ns: dict) -> str:
    """
    Links in RSS 2.0 are text nodes; in Atom they may be href attributes.
    """
    # RSS 2.0 style
    el = item.find("link")
    if el is not None and el.text and el.text.strip():
        return el.text.strip()

    # Atom style  <link href="..." />
    el = item.find("atom:link", ns)
    if el is not None:
        href = el.get("href", "").strip()
        if href:
            return href

    # Some feeds put the URL in <link> with no text but as tail
    el = item.find("link")
    if el is not None and el.tail and el.tail.strip().startswith("http"):
        return el.tail.strip()

    return ""


def parse_feed(feed: dict) -> list:
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

    ns    = {"atom": "http://www.w3.org/2005/Atom"}
    items = root.findall(".//item") or root.findall(".//atom:entry", ns)
    print(f"  Found {len(items)} items")

    articles = []
    for item in items[:5]:
        title = get_text(item, "title", ns)
        link  = get_link(item, ns)

        if not title or not link:
            print(f"  [SKIP] title={repr(title[:40])} link={repr(link[:40])}")
            continue

        raw = (
            get_text(item, "description", ns)
            or get_text(item, "summary", ns)
            or get_text(item, "content", ns)
            or ""
        )
        clean   = strip_html(raw)[:800]
        summary = clean[:300] if len(clean) >= 30 else f"{title} — via {feed['source_name']}."

        pub_raw      = get_text(item, "pubDate", ns) or get_text(item, "published", ns) or ""
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

        articles.append({
            "title":        title,
            "summary":      summary,
            "raw_content":  clean,
            "source_url":   link,
            "source_name":  feed["source_name"],
            "category":     feed["category"],
            "published_at": published_at,
            "is_featured":  False,
            "tags":         [feed["category"]],
        })

    return articles


def main():
    all_articles = []
    for feed in FEEDS:
        print(f"\nFetching: {feed['source_name']}")
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
