import argparse
import json
import os
import random

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "flashcards.json")
MAX_BOX = 5


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def create_deck(args):
    data = load_data()
    if args.deck in data:
        print(f"Deck '{args.deck}' already exists.")
        return
    data[args.deck] = []
    save_data(data)
    print(f"Created deck '{args.deck}'.")


def add_card(args):
    data = load_data()
    if args.deck not in data:
        print(f"No deck named '{args.deck}'. Create it first with create-deck.")
        return
    card = {"front": args.front, "back": args.back, "box": 1}
    data[args.deck].append(card)
    save_data(data)
    print(f"Added card to '{args.deck}': {args.front} -> {args.back}")


def list_decks(args):
    data = load_data()
    if not data:
        print("No decks yet. Create one with create-deck.")
        return
    print(f"\n{'Deck':<25}{'Cards'}")
    print("-" * 35)
    for deck, cards in data.items():
        print(f"{deck:<25}{len(cards)}")
    print()


if __name__ == "__main__":
    main()