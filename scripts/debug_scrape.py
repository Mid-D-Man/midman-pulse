import os
import re
import datetime
import requests
from xml.etree import ElementTree

INGEST_URL    = os.environ["INGEST_URL"]
INGEST_SECRET = os.environ["INGEST_SECRET"]

FEEDS = [
    {"url": "https://feeds.feedburner.com/TheHackersNews",                   "source_name": "The Hacker News", "category": "cybersecurity"},
    {"url": "https://techcrunch.com/category/artificial-intelligence/feed/", "source_name": "TechCrunch AI",   "category": "ai"},
    {"url": "https://venturebeat.com/ai/feed/",                              "source_name": "VentureBeat AI",  "category": "ai"},
]

print("=" * 60)
print("STEP 1 — Testing ingest endpoint auth")
print("=" * 60)

resp = requests.post(
    INGEST_URL,
    json=[{
        "title": "Auth Check Test Article",
        "summary": "Verifying auth works.",
        "source_url": "https://example.com/auth-check",
        "source_name": "Debug",
        "category": "ai",
        "published_at": datetime.datetime.utcnow().isoformat(),
        "is_featured": False,
        "tags": ["debug"],
    }],
    headers={
        "Authorization": "Bearer " + INGEST_SECRET,
        "Content-Type": "application/json",
    },
    timeout=30,
)
print("HTTP Status:", resp.status_code)
print("Response:", resp.text)

print()
print("=" * 60)
print("STEP 2 — Fetching RSS feeds")
print("=" * 60)

for feed in FEEDS:
    print()
    print("Feed:", feed["source_name"])
    print("URL:", feed["url"])
    try:
        r = requests.get(
            feed["url"],
            timeout=15,
            headers={"User-Agent": "MidManPulse/1.0"}
        )
        print("HTTP:", r.status_code, "— bytes:", len(r.content))
        if r.status_code != 200:
            print("  SKIP — bad status")
            continue

        root = ElementTree.fromstring(r.content)
        items = root.findall(".//item")
        print("Items found:", len(items))

        if items:
            first = items[0]
            t = first.find("title")
            l = first.find("link")
            d = first.find("description")
            print("  title:", t.text[:80] if t is not None and t.text else "NONE")
            print("  link: ", l.text[:80] if l is not None and l.text else "NONE")
            print("  desc: ", (d.text or "")[:100] if d is not None else "NONE")

    except Exception as e:
        print("  ERROR:", e)

print()
print("=" * 60)
print("STEP 3 — Sending one real article to ingest")
print("=" * 60)

resp2 = requests.post(
    INGEST_URL,
    json=[{
        "title": "Real Feed Test — AI Security Trends 2026",
        "summary": "A manually crafted article to confirm full pipeline works end to end.",
        "source_url": "https://example.com/real-test-2026",
        "source_name": "Pipeline Test",
        "category": "cybersecurity",
        "published_at": datetime.datetime.utcnow().isoformat(),
        "is_featured": False,
        "tags": ["cybersecurity", "test"],
    }],
    headers={
        "Authorization": "Bearer " + INGEST_SECRET,
        "Content-Type": "application/json",
    },
    timeout=30,
)
print("HTTP Status:", resp2.status_code)
print("Response:", resp2.text)
