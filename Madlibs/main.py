import random

STORIES = [
    {
        "title": "A Day at the Beach",
        "template": (
            "Today I went to the {place} with my {adjective1} friend. "
            "We saw a {adjective2} {animal} {verb_ing} near the water. "
            "It was so {adjective3} that we decided to {verb} all day long. "
            "By the end, we were covered in {noun} and couldn't stop laughing."
        ),
        "blanks": ["place", "adjective1", "adjective2", "animal", "verb_ing",
                   "adjective3", "verb", "noun"],
    },
    {
        "title": "The Job Interview",
        "template": (
            "I walked into the {adjective1} office wearing a {noun1}. "
            "The interviewer asked me to {verb} in front of {number} people. "
            "I felt {adjective2}, but I {verb_past} anyway. "
            "They hired me on the spot because I was so {adjective3}!"
        ),
        "blanks": ["adjective1", "noun1", "verb", "number", "adjective2",
                   "verb_past", "adjective3"],
    },
    {
        "title": "Space Adventure",
        "template": (
            "Captain {name} flew the {adjective1} spaceship to planet {noun1}. "
            "There, they met a {adjective2} alien who loved to {verb}. "
            "Together they {verb_past} across the galaxy, dodging {number} "
            "{noun2} along the way."
        ),
        "blanks": ["name", "adjective1", "noun1", "adjective2", "verb",
                   "verb_past", "number", "noun2"],
    },
]

LABELS = {
    "verb_ing": "a verb ending in -ing",
    "verb_past": "a verb in past tense",
    "number": "a number",
    "name": "a person's name",
}


def label_for(blank):
    if blank in LABELS:
        return LABELS[blank]
    base = blank.rstrip("0123456789")
    return base.replace("_", " ")


def choose_story():
    print("\nPick a story:")
    for i, story in enumerate(STORIES, start=1):
        print(f"  {i}. {story['title']}")
    while True:
        raw = input(f"Enter a number (1-{len(STORIES)}), or 'r' for random: ").strip().lower()
        if raw == "r":
            return random.choice(STORIES)
        if raw.isdigit() and 1 <= int(raw) <= len(STORIES):
            return STORIES[int(raw) - 1]
        print("Invalid choice, try again.")


def collect_words(blanks):
    answers = {}
    print("\nFill in the blanks:\n")
    for blank in blanks:
        answers[blank] = input(f"  Give me {label_for(blank)}: ").strip() or "???"
    return answers


def main():
    print("=" * 40)
    print("   MAD LIBS GENERATOR")
    print("=" * 40)

    while True:
        story = choose_story()
        answers = collect_words(story["blanks"])
        result = story["template"].format(**answers)

        print("\n" + "=" * 40)
        print(f"  {story['title']}")
        print("=" * 40)
        print(result)
        print("=" * 40)

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()