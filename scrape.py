"""Scrape Jainism Simplified chapters from Michigan website."""
import json
import requests
from bs4 import BeautifulSoup

CHAPTERS = [
    "chapter01", "chapter02", "chapter03", "chapter05",
    "chapter08", "chapter10", "chapter11", "chapter13",
    "chapter14", "chapter15", "chapter16",
]
BASE = "https://websites.umich.edu/~umjains/jainismsimplified/"

result = {}
for ch in CHAPTERS:
    url = f"{BASE}{ch}.html"
    print(f"Fetching {url} ...")
    try:
        r = requests.get(url, verify=False, timeout=15)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        # Remove scripts and styles
        for tag in soup(["script", "style", "nav"]):
            tag.decompose()
        # Get title from first heading
        title_tag = soup.find(["h1", "h2", "h3"])
        title = title_tag.get_text(strip=True) if title_tag else ch
        # Get body text
        body = soup.find("body")
        raw_text = body.get_text(separator="\n", strip=True) if body else ""
        result[ch] = {"title": title, "raw_text": raw_text}
        print(f"  -> {title} ({len(raw_text)} chars)")
    except Exception as e:
        print(f"  -> ERROR: {e}")
        result[ch] = {"title": ch, "raw_text": ""}

with open("content/source.json", "w") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f"\nDone. Saved {len(result)} chapters to content/source.json")
