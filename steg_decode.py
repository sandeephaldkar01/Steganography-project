from PIL import Image

def decode_message(image_path):
    img = Image.open(image_path)
    width, height = img.size
    message = ""
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            bits = ((r & 0b11) << 6) | ((g & 0b11) << 4) | ((b & 0b11) << 2)
            message += chr(bits)
            if message.endswith("$t3g0"):
                return message[:-5]
    return "No hidden message found."

# Example usage:
# print(decode_message("output.png"))
