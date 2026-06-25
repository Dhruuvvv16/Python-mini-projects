import argparse
import secrets
import string

SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>?"


def build_charset(use_upper, use_lower, use_digits, use_symbols):
    charset = ""
    if use_upper:
        charset += string.ascii_uppercase
    if use_lower:
        charset += string.ascii_lowercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += SYMBOLS
    return charset


def generate_password(length, charset):
    if not charset:
        raise ValueError("No character set selected.")
    return "".join(secrets.choice(charset) for _ in range(length))


if __name__ == "__main__":
    main()