import argparse

BASES = {"bin": 2, "oct": 8, "dec": 10, "hex": 16}


def to_decimal(value, base):
    return int(value, BASES[base])


if __name__ == "__main__":
    main()