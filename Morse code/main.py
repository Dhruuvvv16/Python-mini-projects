MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/',
}

MORSE_TO_TEXT = {code: char for char, code in MORSE_CODE.items()}


def text_to_morse(text):
    symbols = []
    for char in text.upper():
        if char in MORSE_CODE:
            symbols.append(MORSE_CODE[char])
        else:
            symbols.append("?")
    return " ".join(symbols)


def morse_to_text(morse):
    codes = morse.strip().split(" ")
    result = []
    for code in codes:
        if code == "/":
            result.append(" ")
        elif code in MORSE_TO_TEXT:
            result.append(MORSE_TO_TEXT[code])
        else:
            result.append("?")
    return "".join(result)
def main():
    print("=" * 40)
    print("   MORSE CODE TRANSLATOR")
    print("=" * 40)

    while True:
        print("\n1. Text to Morse")
        print("2. Morse to Text")
        print("3. Quit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            text = input("Enter text: ")
            print(f"\nMorse: {text_to_morse(text)}")
        elif choice == "2":
            morse = input("Enter Morse code (letters separated by spaces, '/' for word gaps): ")
            print(f"\nText: {morse_to_text(morse)}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()