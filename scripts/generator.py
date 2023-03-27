from PIL import Image, ImageDraw
import random

# Set the size of each image
SIZE = 256

# Define a function to generate a random color
def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Define a function to generate a random pattern
def generate_pattern():
    pattern = Image.new('RGB', (SIZE, SIZE), get_random_color())
    draw = ImageDraw.Draw(pattern)
    
    # Draw random circles
    num_circles = random.randint(5, 15)
    for i in range(num_circles):
        x = random.randint(0, SIZE)
        y = random.randint(0, SIZE)
        radius = random.randint(50, 200)
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=get_random_color(), outline=get_random_color(), width=random.randint(5, 20))

    # Draw random lines
    num_lines = random.randint(20, 50)
    for i in range(num_lines):
        x1 = random.randint(0, SIZE)
        y1 = random.randint(0, SIZE)
        x2 = random.randint(0, SIZE)
        y2 = random.randint(0, SIZE)
        draw.line((x1, y1, x2, y2), fill=get_random_color(), width=random.randint(5, 20))

    # Draw random rectangles
    num_rectangles = random.randint(5, 10)
    for i in range(num_rectangles):
        x1 = random.randint(0, SIZE)
        y1 = random.randint(0, SIZE)
        x2 = random.randint(0, SIZE)
        y2 = random.randint(0, SIZE)
        draw.rectangle((x1, y1, x2, y2), fill=get_random_color(), outline=get_random_color(), width=random.randint(5, 20))
    
    return pattern

# Define the number of images to generate
num_images = 10

# Generate and save the images
for i in range(num_images):
    image = generate_pattern()
    filename = f"pfp{i}.png"
    image.save(filename)
