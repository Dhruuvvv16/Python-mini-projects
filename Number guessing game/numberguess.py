import random

DIFFICULTIES = {
    "1": {"label": "Easy   (1-50,  10 attempts)", "range": (1, 50), "attempts": 10},
    "2": {"label": "Medium (1-100, 7 attempts)", "range": (1, 100), "attempts": 7},
    "3": {"label": "Hard   (1-200, 6 attempts)", "range": (1, 200), "attempts": 6},
}
if __name__ == "__main__":
    main()