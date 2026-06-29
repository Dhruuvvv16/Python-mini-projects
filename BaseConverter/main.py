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


def convert(value, from_base, to_base):
    decimal_value = to_decimal(value, from_base)
    return from_decimal(decimal_value, to_base)


def build_parser():
    parser = argparse.ArgumentParser(description="Convert numbers between bases.")
    parser.add_argument("value", help="The number to convert, e.g. 255, 1010, ff")
    parser.add_argument("--from", dest="from_base", choices=BASES.keys(), default="dec",
                         help="The base of the input number (default: dec)")
    parser.add_argument("--to", dest="to_base", choices=list(BASES.keys()) + ["all"], default="all",
                         help="The base to convert to, or 'all' (default: all)")
    return parser

if __name__ == "__main__":
    main()