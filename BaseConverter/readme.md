# Number Base Converter

Convert numbers between **binary**, **octal**, **decimal**, and **hexadecimal** with a simple command-line interface.

## Usage

```bash
python main.py <number> --from <base> --to <base|all>
```

## Examples

Convert a decimal number to all supported bases:

```bash
python main.py 255 --from dec --to all
```

Convert a binary number to decimal:

```bash
python main.py 1010 --from bin --to dec
```

Convert a hexadecimal number to binary:

```bash
python main.py ff --from hex --to bin
```
