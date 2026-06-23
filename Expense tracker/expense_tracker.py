import argparse
import csv
import os
from datetime import datetime
from collections import defaultdict

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.csv")
FIELDS = ["date", "amount", "category", "note"]


def ensure_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=FIELDS).writeheader()


def load_expenses():
    ensure_file()
    with open(DATA_FILE, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


