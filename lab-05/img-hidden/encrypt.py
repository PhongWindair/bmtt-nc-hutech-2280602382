import sys
from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path)
    width, height = img.size
    pixel_index = 0
    binary_message = ''.join(format(ord(char), '08b') for char in message)  # Null terminator
    binary_message += '111111111111110'  # End of message marker
    
    data_index = 0
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))
            for color_chanel in range(3):
                if data_index < len(binary_message):
                    pixel[color_chanel] = (pixel[color_chanel] & ~1) | int(binary_message[data_index])
                    data_index += 1
                    
                img.putpixel((col, row), tuple(pixel))
                
                if data_index >= len(binary_message):
                    break 
    
    
    encode_file_path = 'encode_image.png'
    img.save(encode_file_path)
    print(f"Encoded image saved as {encode_file_path}")
    
def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    message = sys.argv[2]
    
    encode_image(image_path, message)
    
if __name__ == "__main__":
    main()