# rss_fetcher.py
# Fetches and prints titles from an RSS feed (e.g., PIB India)
import feedparser

def fetch_rss(feed_url="https://pib.gov.in/RssMain.aspx?ModId=6&Lang=1&Regid=3"):
    print("Fetching RSS feed:", feed_url)
    feed = feedparser.parse(feed_url)
    for entry in feed.entries[:5]:
        print("•", entry.title)
    print("Total entries fetched:", len(feed.entries))

if __name__ == "__main__":
    fetch_rss()
