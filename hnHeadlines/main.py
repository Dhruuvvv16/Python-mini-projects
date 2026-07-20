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


def build_parser():
    parser = argparse.ArgumentParser(description="Fetch current Hacker News top stories.")
    parser.add_argument("--count", type=int, default=10, help="Number of stories to fetch (default: 10)")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    print("=" * 50)
    print("   HACKER NEWS TOP STORIES")
    print("=" * 50)

    try:
        headlines = fetch_headlines(args.count)
    except requests.exceptions.RequestException:
        print("Couldn't reach Hacker News. Check your internet connection.")
        sys.exit(1)

    for i, story in enumerate(headlines, start=1):
        print(f"\n{i}. {story['title']}")
        print(f"   {story['score']} points | {story['comments']} comments")
        print(f"   {story['url']}")
    print()


if __name__ == "__main__":
    main()