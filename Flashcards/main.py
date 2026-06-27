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


def weighted_card_order(cards):
    """Cards in lower boxes are weighted to appear more often."""
    pool = list(range(len(cards)))
    pool_weights = [MAX_BOX + 1 - cards[i]["box"] for i in pool]
    order = []
    while pool:
        chosen = random.choices(pool, weights=pool_weights, k=1)[0]
        idx = pool.index(chosen)
        order.append(chosen)
        pool.pop(idx)
        pool_weights.pop(idx)
    return order


def study(args):
    data = load_data()
    if args.deck not in data or not data[args.deck]:
        print(f"Deck '{args.deck}' doesn't exist or has no cards.")
        return

    cards = data[args.deck]
    order = weighted_card_order(cards)
    correct = 0
    total = len(order)

    print(f"\nStudying '{args.deck}' ({total} cards). Press Enter to reveal an answer.\n")

    for position, idx in enumerate(order, start=1):
        card = cards[idx]
        print(f"[{position}/{total}] Box {card['box']}: {card['front']}")
        input("   (press Enter to reveal) ")
        print(f"   Answer: {card['back']}")

        while True:
            result = input("   Did you get it right? (y/n): ").strip().lower()
            if result in ("y", "n"):
                break
            print("   Please enter 'y' or 'n'.")

        if result == "y":
            card["box"] = min(card["box"] + 1, MAX_BOX)
            correct += 1
        else:
            card["box"] = 1

    save_data(data)
    print(f"\nSession complete: {correct}/{total} correct.")
    print("Card boxes updated and saved.\n")


def stats(args):
    data = load_data()
    if args.deck not in data:
        print(f"No deck named '{args.deck}'.")
        return

    cards = data[args.deck]
    if not cards:
        print("This deck has no cards yet.")
        return

    print(f"\nStats for '{args.deck}':")
    box_counts = {i: 0 for i in range(1, MAX_BOX + 1)}
    for card in cards:
        box_counts[card["box"]] += 1

    for box, count in box_counts.items():
        bar = "#" * count
        print(f"  Box {box}: {count:<3} {bar}")

    mastered = box_counts[MAX_BOX]
    print(f"\n{mastered}/{len(cards)} cards fully mastered (box {MAX_BOX}).\n")

if __name__ == "__main__":
    main()