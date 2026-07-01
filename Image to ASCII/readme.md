# Image to ASCII Art Converter

Converts any image into ASCII art that you can view in the terminal or save to a text file.

A fun companion to the GIF Generator project since it uses the same **Pillow** library for image processing.

## Requirements

```bash
pip install Pillow
```

## Usage

```bash
python main.py <image_path> [options]
```

### Examples

Convert an image and display the ASCII art in the terminal:

```bash
python main.py photo.jpg
```

Convert an image with a custom width and save the output to a text file:

```bash
python main.py photo.jpg --width 120 --output art.txt
```
