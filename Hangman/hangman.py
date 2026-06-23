import random

WORDS = {
    "animals": ["elephant", "giraffe", "dolphin", "kangaroo", "penguin", "tiger"],
    "fruits": ["mango", "banana", "pineapple", "strawberry", "watermelon", "papaya"],
    "countries": ["india", "canada", "brazil", "germany", "japan", "egypt"],
    "programming": ["python", "variable", "function", "loop", "array", "compiler"],
}

STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    ___|___
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ___|___
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ___|___
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ___|___
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ___|___
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ___|___
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ___|___
    """,
]

MAX_WRONG = len(STAGES) - 1


def pick_word():
    category = random.choice(list(WORDS.keys()))
    word = random.choice(WORDS[category])
    return word, category


def display_word(word, guessed):
    return " ".join(letter if letter in guessed else "_" for letter in word)


def get_guess(guessed):
    while True:
        raw = input("Guess a letter: ").strip().lower()
        if len(raw) != 1 or not raw.isalpha():
            print("Please enter a single letter.")
            continue
        if raw in guessed:
            print("You already guessed that letter.")
            continue
        return raw

