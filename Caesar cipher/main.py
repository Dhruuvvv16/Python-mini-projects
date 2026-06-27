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

if __name__ == "__main__":
    main()