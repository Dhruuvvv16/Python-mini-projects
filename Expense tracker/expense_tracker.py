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


def add_expense(args):
    ensure_file()
    row = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "amount": f"{args.amount:.2f}",
        "category": args.category,
        "note": args.note or "",
    }
    with open(DATA_FILE, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=FIELDS).writerow(row)
    print(f"Added expense: {row['date']} | {row['amount']} | {row['category']} | {row['note']}")


def list_expenses(args):
    rows = load_expenses()
    if not rows:
        print("No expenses recorded yet.")
        return
    print(f"\n{'Date':<12}{'Amount':<10}{'Category':<15}{'Note'}")
    print("-" * 55)
    total = 0.0
    for r in rows:
        print(f"{r['date']:<12}{r['amount']:<10}{r['category']:<15}{r['note']}")
        total += float(r["amount"])
    print("-" * 55)
    print(f"{'TOTAL':<12}{total:.2f}\n")


