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

if __name__ == "__main__":
    main()