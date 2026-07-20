import argparse
import sys

import requests

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{id}.json"


def fetch_top_story_ids():
    response = requests.get(TOP_STORIES_URL, timeout=10)
    response.raise_for_status()
    return response.json()


def fetch_item(item_id):
    response = requests.get(ITEM_URL.format(id=item_id), timeout=10)
    response.raise_for_status()
    return response.json()


def fetch_headlines(count):
    ids = fetch_top_story_ids()[:count]
    headlines = []
    for item_id in ids:
        item = fetch_item(item_id)
        if item:
            headlines.append({
                "title": item.get("title", "(no title)"),
                "url": item.get("url", f"https://news.ycombinator.com/item?id={item_id}"),
                "score": item.get("score", 0),
                "comments": item.get("descendants", 0),
            })
    return headlines

if __name__ == "__main__":
    main()