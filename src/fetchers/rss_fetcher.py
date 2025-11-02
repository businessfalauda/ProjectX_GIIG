from src.utils.storage import init_db, insert_rows
init_db()
# rss_fetcher.py
# Fetches and prints headlines from PIB RSS feed
import feedparser

def fetch_rss(feed_url="https://pib.gov.in/RssMain.aspx?ModId=6&Lang=1&Regid=3"):
    print("Fetching RSS feed:", feed_url)
    feed = feedparser.parse(feed_url)
    rows = []
for entry in feed.entries[:5]:
    print("•", entry.title)
    rows.append(("PIB RSS", entry.title))
insert_rows("rss_data", rows)

if __name__ == "__main__":
    fetch_rss()
