# newsapi_fetcher.py
import os, requests

def fetch_news(query="finance"):
    api = os.getenv("NEWSAPI_KEY")
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&apiKey={api}"
    r = requests.get(url)
    print(r.status_code, r.text[:400])

if __name__ == "__main__":
    fetch_news("Indian economy")
