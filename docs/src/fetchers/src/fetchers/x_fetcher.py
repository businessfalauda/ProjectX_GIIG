# x_fetcher.py
# Polls X (Twitter) handles for recent posts
import os, requests

def get_latest_tweets(handle, bearer=os.getenv("X_BEARER")):
    url = f"https://api.x.com/2/tweets/search/recent?query=from:{handle}&max_results=5"
    headers = {"Authorization": f"Bearer {bearer}"}
    r = requests.get(url, headers=headers)
    print(r.status_code, r.text[:400])

if __name__ == "__main__":
    get_latest_tweets("PMOIndia")
