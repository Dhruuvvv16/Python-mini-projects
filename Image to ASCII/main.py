import argparse

from PIL import Image

ASCII_CHARS = "@%#*+=-:. "
def resize_image(image, new_width):
    width, height = image.size
    aspect_ratio = height / width
    # 0.55 roughly compensates for terminal characters being taller than wide
    new_height = max(int(new_width * aspect_ratio * 0.55), 1)
    return image.resize((new_width, new_height))
if __name__ == "__main__":
    main()