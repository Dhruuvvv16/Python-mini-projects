# Contact Book (CLI)

A simple command-line contact manager that stores contacts in a local **JSON** file.

Supports:

- Add new contacts
- Search existing contacts
- Update contact information
- List all contacts
- Delete contacts

## Usage

```bash
python contact_book.py <command> [options]
```

## Examples

Add a new contact:

```bash
python main.py add "Roy Patel" --phone 9876543210 --email roy@example.com
```

List all contacts:

```bash
python main.py list
```

Search for a contact:

```bash
python main.py search Roy
```

Update a contact:

```bash
python main.py update "Roy Patel" --phone 9998887777
```

Delete a contact:

```bash
python main.py delete "Roy Patel"
```
