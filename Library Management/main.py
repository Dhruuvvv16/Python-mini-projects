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

if __name__ == "__main__":
    main()