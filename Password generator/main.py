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


def build_parser():
    parser = argparse.ArgumentParser(description="Generate secure random passwords.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length (default: 12)")
    parser.add_argument("-n", "--count", type=int, default=1, help="How many passwords to generate (default: 1)")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.length < 4:
        print("Length should be at least 4 for a meaningful password.")
        return

    charset = build_charset(
        use_upper=not args.no_upper,
        use_lower=not args.no_lower,
        use_digits=not args.no_digits,
        use_symbols=not args.no_symbols,
    )

    if not charset:
        print("You excluded every character set. Enable at least one.")
        return
if __name__ == "__main__":
    main()