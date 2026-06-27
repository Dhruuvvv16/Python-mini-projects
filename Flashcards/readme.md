# Flashcard App (CLI)

Create decks of flashcards and study them with a simplified spaced repetition system (a Leitner box). Cards you answer correctly move to a higher box and appear less frequently, while cards answered incorrectly return to Box 1 so they are reviewed more often.

## Examples

```bash
python main.py create-deck "ENG Vocab"
python main.py add-card "ENG Vocab" "delineate" "descibe"
python main.py add-card "ENG Vocab" "insinuate" "to suggest indirectly"
python main.py list-decks
python main.py study "ENG Vocab"
python main.py stats "ENG Vocab"
```

| Command     | Description                    |
| ----------- | ------------------------------ |
| create-deck | Create a new deck              |
| add-card    | Add a card to a deck           |
| list-decks  | List all decks                 |
| study       | Study a deck                   |
| stats       | Show progress stats for a deck |
