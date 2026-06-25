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


def rate_strength(password):
    score = 0
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in SYMBOLS for c in password):
        score += 1

    labels = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong", "Excellent"]
    return labels[min(score, len(labels) - 1)]

if __name__ == "__main__":
    main()