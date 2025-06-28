from PIL import Image

def encode_message(image_path, message, output_path):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    index = 0
    message += "$t3g0"  # delimiter

    for row in range(height):
        for col in range(width):
            if index < len(message):
                r, g, b = img.getpixel((col, row))
                ascii_val = ord(message[index])
                r = (r & 0b11111100) | ((ascii_val >> 6) & 0b11)
                g = (g & 0b11111100) | ((ascii_val >> 4) & 0b11)
                b = (b & 0b11111100) | ((ascii_val >> 2) & 0b11)
                encoded.putpixel((col, row), (r, g, b))
                index += 1
    encoded.save(output_path)
    print("Message hidden successfully!")

# Example usage:
# encode_message("input.png", "This is a secret message", "output.png")
