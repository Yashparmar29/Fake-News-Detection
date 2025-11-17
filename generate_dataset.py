import os
import random
from PIL import Image, ImageDraw, ImageFont
from faker import Faker
import numpy as np

# Initialize Faker for generating fake text
fake = Faker()

# Create directories if they don't exist
os.makedirs('datasets/image_fake_news/authentic', exist_ok=True)
os.makedirs('datasets/image_fake_news/fake', exist_ok=True)

def create_authentic_image(width=224, height=224, color=(255, 255, 255)):
    """Create a simple authentic image (e.g., a plain colored background)."""
    img = Image.new('RGB', (width, height), color=color)
    return img

def create_fake_image(width=224, height=224):
    """Create a fake image by adding manipulated elements like fake text overlays."""
    # Start with a base image
    img = create_authentic_image(width, height, color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    # Add fake text overlay
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()

    # Generate fake news-like text
    fake_text = fake.sentence(nb_words=10)
    text_position = (random.randint(10, width-100), random.randint(10, height-50))
    draw.text(text_position, fake_text, fill=(0, 0, 0), font=font)

    # Add some distortion (e.g., random noise)
    img_array = np.array(img)
    noise = np.random.randint(0, 50, img_array.shape, dtype='uint8')
    img_array = np.clip(img_array + noise, 0, 255)
    img = Image.fromarray(img_array.astype('uint8'))

    return img

def generate_dataset(num_images=100):
    """Generate a dataset with authentic and fake images."""
    for i in range(num_images // 2):
        # Authentic images
        img = create_authentic_image()
        img.save(f'datasets/image_fake_news/authentic/authentic_{i}.png')

        # Fake images
        img = create_fake_image()
        img.save(f'datasets/image_fake_news/fake/fake_{i}.png')

    print(f"Generated {num_images} images: {num_images//2} authentic, {num_images//2} fake.")

if __name__ == "__main__":
    generate_dataset(200)  # Generate 200 images (100 authentic, 100 fake)
