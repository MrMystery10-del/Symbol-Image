from PIL import Image, ImageDraw, ImageFont
import platform
import subprocess

# Define the symbols to represent the grayscale values
symbols = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

# Load the image, you can paste any image you want
image = Image.open("image/gorilla_big.png")

# Convert the image to grayscale
gray_image = image.convert("L")

# Resize the image to 500x500
resized_image = gray_image.resize((500, 500))

# Convert the image to a symbol 2D array
symbol_array = []
for y in range(500):
    row = []
    for x in range(500):
        pixel = resized_image.getpixel((x, y))
        symbol_index = int(pixel / 25.6) # Map the grayscale value to a symbol index
        symbol = symbols[symbol_index]
        row.append(symbol)
    symbol_array.append(row)

# Create an image to draw the symbols on
output_image = Image.new('RGB', (5000, 5000), color=(0, 0, 0))
draw = ImageDraw.Draw(output_image)

# Set the font to use
font = ImageFont.truetype('arial.ttf', 12)

# Draw the symbols on the image with a margin of 2 pixels
for y in range(500):
    for x in range(500):
        symbol = symbol_array[y][x]
        draw.text((x*10, y*10), symbol, (255, 255, 255), font=font)

# Save the output image as a PNG file
output_image.save("output.png")

# Open the output image in the default image viewer
if platform.system() == 'Darwin': # macOS
    subprocess.call(['open', '-a', 'Preview', '-F', 'output.png'])
elif platform.system() == 'Windows': # Windows
    subprocess.call(['start', 'output.png'], shell=True)
else: # Linux
    subprocess.call(['xdg-open', 'output.png'])