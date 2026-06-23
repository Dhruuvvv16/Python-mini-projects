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


def play():
    word, category = pick_word()
    guessed = set()
    wrong = 0

    print(f"\nCategory: {category} | Word length: {len(word)}")

    while wrong < MAX_WRONG:
        print(STAGES[wrong])
        print("Word:", display_word(word, guessed))
        print("Guessed letters:", ", ".join(sorted(guessed)) or "none")

        if all(letter in guessed for letter in word):
            print(f"\nYou guessed it! The word was '{word}'.")
            return True

        letter = get_guess(guessed)
        guessed.add(letter)

        if letter not in word:
            wrong += 1
            print("Wrong guess!")
        else:
            print("Nice, that letter is in the word!")

    print(STAGES[wrong])
    print(f"\nOut of tries! The word was '{word}'.")
    return False


def main():
    print("=" * 40)
    print("   HANGMAN")
    print("=" * 40)

    wins = 0
    games = 0

    while True:
        won = play()
        games += 1
        wins += int(won)

        print(f"\nScore: {wins}/{games} games won.")
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()