# Library Management System (CLI)

Manage a small library's book catalog using SQLite. Supports adding books, listing and searching the catalog, checking books out, returning them, and removing books. A great beginner project for practicing SQL with Python's built-in `sqlite3` module.

## Examples

```bash
python main.py add "Dune" "Frank Herbert" --copies 3
python main.py list
python main.py search dune
python main.py checkout "Dune"
python main.py return "Dune"
python main.py remove "Dune"
```
