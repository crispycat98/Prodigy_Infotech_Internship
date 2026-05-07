"""
Image Encryption Tool - Pixel Manipulation (XOR)
Encrypting and decrypting are the same operation — just run it twice.
"""

from PIL import Image
import sys
import os


def xor_image(input_path, output_path, key=42):
    """XOR every pixel channel with the key. Same function encrypts and decrypts."""
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)
    print(f"Done! Saved to: {output_path}")


def main():
    print("=" * 40)
    print("   Image Encryption Tool (XOR)")
    print("=" * 40)
    print("Note: Encrypt and Decrypt use the same operation.")
    print("Just run it again on the encrypted image to get back the original.\n")

    input_path = input("Enter input image path (e.g. photo.png): ").strip()
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        sys.exit(1)

    output_path = input("Enter output image path (e.g. encrypted.png): ").strip()

    try:
        key = int(input("Enter XOR key (0-255, default 42): ").strip() or "42")
        if not (0 <= key <= 255):
            raise ValueError
    except ValueError:
        print("Invalid key. Using default key: 42")
        key = 42

    xor_image(input_path, output_path, key)


if __name__ == "__main__":
    main()
