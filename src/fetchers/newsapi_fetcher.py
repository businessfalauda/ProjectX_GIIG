# newsapi_fetcher.py
# Fetches top global business headlines from NewsAPI
import os
import requests

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
    resp = requests.get(url, headers=headers)
    print("Status:", resp.status_code)
    if resp.ok:
        data = resp.json()
        for article in data.get("articles", []):
            print("•", article["title"])
        print("Total results:", data.get("totalResults", 0))
    else:
        print("Response text:", resp.text)

if __name__ == "__main__":
    fetch_news()
