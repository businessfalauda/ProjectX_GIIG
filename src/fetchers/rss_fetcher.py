# rss_fetcher.py
# Fetches and prints headlines from PIB RSS feed
import os, sys
sys.path.append(os.getcwd())
import feedparser
from src.utils.storage import init_db, insert_rows

def fetch_rss(feed_url="https://pib.gov.in/RssMain.aspx?ModId=6&Lang=1&Regid=3"):
    print("Fetching RSS feed:", feed_url)
    feed = feedparser.parse(feed_url)       # <--- this defines 'feed'
    rows = []
    for entry in feed.entries[:5]:
        print("•", entry.title)
        rows.append(("PIB RSS", entry.title))
    print("Total entries fetched:", len(feed.entries))
    insert_rows("rss_data", rows)

if __name__ == "__main__":
    init_db()
    fetch_rss()
