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


