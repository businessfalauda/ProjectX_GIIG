# newsapi_fetcher.py
# Fetches top global business headlines from NewsAPI
import os, sys, requests
sys.path.append(os.getcwd())
from src.utils.storage import init_db, insert_rows

def fetch_news(api_key=None):
    api_key = api_key or os.getenv("NEWSAPI_KEY")
    if not api_key:
        print("❌ No NEWSAPI_KEY found. Add it as a GitHub secret.")
        return

    url = (
        "https://newsapi.org/v2/top-headlines?"
        "category=business&language=en&pageSize=5"
    )
    headers = {"Authorization": f"Bearer {api_key}"}

    print("Fetching NewsAPI headlines...")
    resp = requests.get(url, headers=headers)
    print("Status:", resp.status_code)

    if resp.ok:
        data = resp.json()
        rows = [("NewsAPI", article.get("title", "Untitled")) for article in data.get("articles", [])]
        for source, title in rows:
            print("•", title)
        print("Total results:", data.get("totalResults", len(rows)))
        insert_rows("news_data", rows)
    else:
        print("⚠️ Failed to fetch from NewsAPI, response text:")
        print(resp.text)

if __name__ == "__main__":
    init_db()
    fetch_news()

