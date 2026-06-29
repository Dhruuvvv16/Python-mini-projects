import argparse

BASES = {"bin": 2, "oct": 8, "dec": 10, "hex": 16}


def to_decimal(value, base):
    return int(value, BASES[base])


def from_decimal(value, base):
    if base == "bin":
        return bin(value)[2:]
    if base == "oct":
        return oct(value)[2:]
    if base == "hex":
        return hex(value)[2:]
    return str(value)

if __name__ == "__main__":
    main()