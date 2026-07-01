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


if __name__ == "__main__":
    main()