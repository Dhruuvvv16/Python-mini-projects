import argparse
import os
import sqlite3

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "library.db")


def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            total_copies INTEGER NOT NULL,
            available_copies INTEGER NOT NULL
        )
    """)
    return conn


def add_book(args):
    conn = get_connection()
    conn.execute(
        "INSERT INTO books (title, author, total_copies, available_copies) VALUES (?, ?, ?, ?)",
        (args.title, args.author, args.copies, args.copies),
    )
    conn.commit()
    conn.close()
    print(f"Added '{args.title}' by {args.author} ({args.copies} copies).")


def list_books(args):
    conn = get_connection()
    rows = conn.execute(
        "SELECT title, author, available_copies, total_copies FROM books ORDER BY title"
    ).fetchall()
    conn.close()

    if not rows:
        print("The library is empty. Add a book with 'add'.")
        return

    print(f"\n{'Title':<30}{'Author':<20}{'Available'}")
    print("-" * 65)
    for title, author, available, total in rows:
        print(f"{title:<30}{author:<20}{available}/{total}")
    print()


def search_books(args):
    conn = get_connection()
    query = f"%{args.query}%"
    rows = conn.execute(
        "SELECT title, author, available_copies, total_copies FROM books "
        "WHERE title LIKE ? OR author LIKE ? ORDER BY title",
        (query, query),
    ).fetchall()
    conn.close()

    if not rows:
        print(f"No books matching '{args.query}'.")
        return

    print(f"\n{'Title':<30}{'Author':<20}{'Available'}")
    print("-" * 65)
    for title, author, available, total in rows:
        print(f"{title:<30}{author:<20}{available}/{total}")
    print()


def checkout_book(args):
    conn = get_connection()
    row = conn.execute("SELECT id, available_copies FROM books WHERE title = ?", (args.title,)).fetchone()
    if not row:
        print(f"No book titled '{args.title}' found.")
        conn.close()
        return
    book_id, available = row
    if available <= 0:
        print(f"No copies of '{args.title}' are available right now.")
        conn.close()
        return
    conn.execute("UPDATE books SET available_copies = available_copies - 1 WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    print(f"Checked out '{args.title}'. {available - 1} copies left.")


def return_book(args):
    conn = get_connection()
    row = conn.execute(
        "SELECT id, available_copies, total_copies FROM books WHERE title = ?", (args.title,)
    ).fetchone()
    if not row:
        print(f"No book titled '{args.title}' found.")
        conn.close()
        return
    book_id, available, total = row
    if available >= total:
        print(f"All copies of '{args.title}' are already checked in.")
        conn.close()
        return
    conn.execute("UPDATE books SET available_copies = available_copies + 1 WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    print(f"Returned '{args.title}'. {available + 1} copies now available.")


def remove_book(args):
    conn = get_connection()
    cursor = conn.execute("DELETE FROM books WHERE title = ?", (args.title,))
    conn.commit()
    conn.close()
    if cursor.rowcount == 0:
        print(f"No book titled '{args.title}' found.")
    else:
        print(f"Removed '{args.title}' from the library.")


def build_parser():
    parser = argparse.ArgumentParser(description="A simple CLI library management system.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new book")
    add_parser.add_argument("title")
    add_parser.add_argument("author")
    add_parser.add_argument("--copies", type=int, default=1)
    add_parser.set_defaults(func=add_book)

    list_parser = subparsers.add_parser("list", help="List all books")
    list_parser.set_defaults(func=list_books)

    search_parser = subparsers.add_parser("search", help="Search books by title or author")
    search_parser.add_argument("query")
    search_parser.set_defaults(func=search_books)

    checkout_parser = subparsers.add_parser("checkout", help="Check out a book")
    checkout_parser.add_argument("title")
    checkout_parser.set_defaults(func=checkout_book)

    return_parser = subparsers.add_parser("return", help="Return a book")
    return_parser.add_argument("title")
    return_parser.set_defaults(func=return_book)

    remove_parser = subparsers.add_parser("remove", help="Remove a book from the catalog")
    remove_parser.add_argument("title")
    remove_parser.set_defaults(func=remove_book)

    return parser

if __name__ == "__main__":
    main()