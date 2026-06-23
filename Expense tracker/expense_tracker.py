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


def summary(args):
    rows = load_expenses()
    if args.month:
        rows = [r for r in rows if r["date"].startswith(args.month)]

    if not rows:
        print("No matching expenses found.")
        return

    by_category = defaultdict(float)
    total = 0.0
    for r in rows:
        amount = float(r["amount"])
        by_category[r["category"]] += amount
        total += amount

    label = f" for {args.month}" if args.month else ""
    print(f"\nExpense summary{label}:")
    print("-" * 30)
    for category, amount in sorted(by_category.items(), key=lambda x: -x[1]):
        pct = (amount / total) * 100
        print(f"{category:<15}{amount:>8.2f}  ({pct:.1f}%)")
    print("-" * 30)
    print(f"{'TOTAL':<15}{total:>8.2f}\n")


def build_parser():
    parser = argparse.ArgumentParser(description="A simple CLI expense tracker.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("amount", type=float, help="Amount spent")
    add_parser.add_argument("category", help="Category, e.g. Food, Travel")
    add_parser.add_argument("note", nargs="?", default="", help="Optional note")
    add_parser.set_defaults(func=add_expense)

    list_parser = subparsers.add_parser("list", help="List all expenses")
    list_parser.set_defaults(func=list_expenses)

    summary_parser = subparsers.add_parser("summary", help="Show spending summary")
    summary_parser.add_argument(
        "--month", help="Filter by month, format YYYY-MM (e.g. 2026-06)"
    )
    summary_parser.set_defaults(func=summary)

    return parser

