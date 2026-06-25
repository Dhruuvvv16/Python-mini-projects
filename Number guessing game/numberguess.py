import random

DIFFICULTIES = {
    "1": {"label": "Easy   (1-50,  10 attempts)", "range": (1, 50), "attempts": 10},
    "2": {"label": "Medium (1-100, 7 attempts)", "range": (1, 100), "attempts": 7},
    "3": {"label": "Hard   (1-200, 6 attempts)", "range": (1, 200), "attempts": 6},
}

def choose_difficulty():
    print("\nChoose a difficulty:")
    for key, value in DIFFICULTIES.items():
        print(f"  {key}. {value['label']}")

    while True:
        choice = input("Enter 1, 2 or 3: ").strip()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print("Invalid choice, please try again.")


def get_guess(low, high):
    while True:
        raw = input(f"Your guess ({low}-{high}): ").strip()
        if raw.lower() in ("q", "quit", "exit"):
            return None
        if not raw.lstrip("-").isdigit():
            print("Please enter a whole number.")
            continue
        guess = int(raw)
        if guess < low or guess > high:
            print(f"Stay within {low}-{high}.")
            continue
        return guess


def play_round(difficulty):
    low, high = difficulty["range"]
    attempts_left = difficulty["attempts"]
    target = random.randint(low, high)

    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"You have {attempts_left} attempts. Type 'q' to quit early.\n")

    while attempts_left > 0:
        guess = get_guess(low, high)
        if guess is None:
            print(f"You quit. The number was {target}.")
            return False

        attempts_left -= 1

        if guess == target:
            print(f"\nCorrect! The number was {target}.")
            print(f"You got it with {attempts_left} attempt(s) left to spare.")
            return True
        elif guess < target:
            print(f"Too low. {attempts_left} attempt(s) left.")
        else:
            print(f"Too high. {attempts_left} attempt(s) left.")

    print(f"\nOut of attempts! The number was {target}.")
    return False

if __name__ == "__main__":
    main()