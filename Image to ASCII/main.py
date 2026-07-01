import argparse

from PIL import Image

ASCII_CHARS = "@%#*+=-:. "


def resize_image(image, new_width):
    width, height = image.size
    aspect_ratio = height / width
    # 0.55 roughly compensates for terminal characters being taller than wide
    new_height = max(int(new_width * aspect_ratio * 0.55), 1)
    return image.resize((new_width, new_height))


def pixels_to_ascii(image):
    pixels = image.getdata()
    return "".join(ASCII_CHARS[pixel * (len(ASCII_CHARS) - 1) // 255] for pixel in pixels)


def convert_image(path, width):
    image = Image.open(path)
    image = resize_image(image, width)
    image = image.convert("L")  # grayscale

    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    rows = [ascii_str[i:i + img_width] for i in range(0, len(ascii_str), img_width)]
    return "\n".join(rows)


def build_parser():
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art.")
    parser.add_argument("image", help="Path to the input image")
    parser.add_argument("--width", type=int, default=100, help="Output width in characters (default: 100)")
    parser.add_argument("--output", help="Optional file path to save the ASCII art as .txt")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        art = convert_image(args.image, args.width)
    except FileNotFoundError:
        print(f"Could not find image: {args.image}")
        return
    except Exception as e:
        print(f"Something went wrong: {e}")
        return

    print(art)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(art)
        print(f"\nSaved ASCII art to {args.output}")


if __name__ == "__main__":
    main()