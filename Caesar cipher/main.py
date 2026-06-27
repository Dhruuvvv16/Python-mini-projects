import string

ALPHABET = string.ascii_lowercase


def shift_char(char, shift):
    if char.islower():
        index = (ALPHABET.index(char) + shift) % 26
        return ALPHABET[index]
    if char.isupper():
        index = (ALPHABET.index(char.lower()) + shift) % 26
        return ALPHABET[index].upper()
    return char


def encode(text, shift):
    return "".join(shift_char(c, shift) for c in text)


def decode(text, shift):
    return encode(text, -shift)


def crack(text):
    print("\nTrying every shift from 1 to 25:\n")
    for shift in range(1, 26):
        print(f"  Shift {shift:>2}: {decode(text, shift)}")


def get_shift():
    while True:
        raw = input("Enter shift (1-25): ").strip()
        if raw.isdigit() and 1 <= int(raw) <= 25:
            return int(raw)
        print("Please enter a whole number between 1 and 25.")


def main():
    print("=" * 40)
    print("   CAESAR CIPHER TOOL")
    print("=" * 40)

    while True:
        print("\n1. Encode a message")
        print("2. Decode a message")
        print("3. Crack a message (try all shifts)")
        print("4. Quit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            text = input("Message to encode: ")
            shift = get_shift()
            print(f"\nEncoded: {encode(text, shift)}")
        elif choice == "2":
            text = input("Message to decode: ")
            shift = get_shift()
            print(f"\nDecoded: {decode(text, shift)}")
        elif choice == "3":
            text = input("Message to crack: ")
            crack(text)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()