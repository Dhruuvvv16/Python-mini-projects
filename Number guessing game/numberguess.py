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
if __name__ == "__main__":
    main()