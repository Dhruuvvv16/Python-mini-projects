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


def search_contacts(args):
    contacts = load_contacts()
    query = args.query.lower()
    matches = [
        c for c in contacts
        if query in c["name"].lower()
        or query in c.get("phone", "")
        or query in c.get("email", "").lower()
    ]
    if not matches:
        print(f"No contacts matching '{args.query}'.")
        return
    print(f"\n{'Name':<25}{'Phone':<15}{'Email'}")
    print("-" * 60)
    for c in matches:
        print(f"{c['name']:<25}{c['phone']:<15}{c['email']}")
    print()


def update_contact(args):
    contacts = load_contacts()
    for c in contacts:
        if c["name"].lower() == args.name.lower():
            if args.phone:
                c["phone"] = args.phone
            if args.email:
                c["email"] = args.email
            save_contacts(contacts)
            print(f"Updated contact: {args.name}")
            return
    print(f"No contact named '{args.name}' found.")


def delete_contact(args):
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c["name"].lower() != args.name.lower()]
    if len(new_contacts) == len(contacts):
        print(f"No contact named '{args.name}' found.")
        return
    save_contacts(new_contacts)
    print(f"Deleted contact: {args.name}")

if __name__ == "__main__":
    main()