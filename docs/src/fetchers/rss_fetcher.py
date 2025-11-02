# rss_fetcher.py
# Fetches and parses RSS feeds (MCA, PIB, etc.)
def fetch_rss(feed_url):
    import feedparser
    data = feedparser.parse(feed_url)
    for entry in data.entries[:3]:
        print(entry.title, entry.link)
if __name__ == "__main__":
    fetch_rss("https://pib.gov.in/RssMain.aspx?ModId=6&Lang=1&Regid=3")
