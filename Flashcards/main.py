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

if __name__ == "__main__":
    main()