import argparse
import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.json")


def load_contacts():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_contacts(contacts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2)


def add_contact(args):
    contacts = load_contacts()
    if any(c["name"].lower() == args.name.lower() for c in contacts):
        print(f"A contact named '{args.name}' already exists.")
        return
    contacts.append({
        "name": args.name,
        "phone": args.phone or "",
        "email": args.email or "",
    })
    save_contacts(contacts)
    print(f"Added contact: {args.name}")


def list_contacts(args):
    contacts = load_contacts()
    if not contacts:
        print("No contacts yet.")
        return
    contacts.sort(key=lambda c: c["name"].lower())
    print(f"\n{'Name':<25}{'Phone':<15}{'Email'}")
    print("-" * 60)
    for c in contacts:
        print(f"{c['name']:<25}{c['phone']:<15}{c['email']}")
    print()

if __name__ == "__main__":
    main()