STORY = {
    "start": {
        "text": (
            "You wake up in a dim forest clearing with no memory of how "
            "you got here. Two paths lie ahead: one leads toward a "
            "flickering light, the other toward the sound of running water."
        ),
        "choices": {
            "1": ("Walk toward the light", "cabin"),
            "2": ("Follow the sound of water", "river"),
        },
    },
    "cabin": {
        "text": (
            "You find an old wooden cabin with smoke rising from its "
            "chimney. The door is slightly open."
        ),
        "choices": {
            "1": ("Knock on the door", "cabin_knock"),
            "2": ("Sneak around to peek through a window", "cabin_window"),
        },
    },
    "cabin_knock": {
        "text": (
            "An elderly woman opens the door and smiles. 'I've been "
            "expecting you,' she says, handing you a strange brass key."
        ),
        "choices": {
            "1": ("Take the key and ask questions", "good_ending"),
            "2": ("Take the key and run", "neutral_ending"),
        },
    },
    "cabin_window": {
        "text": (
            "Through the window you see the woman talking to no one, "
            "as if expecting a guest. A floorboard creaks under your foot."
        ),
        "choices": {
            "1": ("Run before she notices", "river"),
            "2": ("Knock now that you're discovered", "cabin_knock"),
        },
    },
    "river": {
        "text": (
            "You reach a fast-flowing river. A rickety rope bridge sways "
            "above it, and a small rowboat is tied to a post nearby."
        ),
        "choices": {
            "1": ("Cross the rope bridge", "bridge_ending"),
            "2": ("Take the rowboat", "boat_ending"),
        },
    },
    "good_ending": {
        "text": (
            "The woman explains the key opens a path home. Following her "
            "directions, you find your way back, wiser for the journey."
        ),
        "choices": {},
    },
    "neutral_ending": {
        "text": (
            "You escape with the key, but never learn what it truly opens. "
            "Some mysteries, it seems, are meant to stay unsolved."
        ),
        "choices": {},
    },
    "bridge_ending": {
        "text": (
            "The bridge holds, barely. On the other side, a path leads "
            "you out of the forest and back to civilization."
        ),
        "choices": {},
    },
    "boat_ending": {
        "text": (
            "The current sweeps you downstream fast. After a tense ride, "
            "you wash ashore near a familiar road home."
        ),
        "choices": {},
    },
}

