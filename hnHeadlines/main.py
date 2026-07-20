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

if __name__ == "__main__":
    main()