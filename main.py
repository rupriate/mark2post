from PIL import Image
from PIL import Image, ImageDraw, ImageFont
import os
from captions import generate_captions
import json

# Load the JSON file
with open('config.json', 'r') as file:
    config = json.load(file)

# Extract values into variables
watermark_base = config['watermark_base']

main_text_color = config['text_properties']['main_text']['color']
main_text_x_position = config['text_properties']['main_text']['x_position']
main_text_y_position = config['text_properties']['main_text']['y_position']
main_text_font_size = config['text_properties']['main_text']['font_size']
main_text_font_family = config['text_properties']['main_text']['font_family']

secondary_text_color = config['text_properties']['secondary_text']['color']
secondary_text_x_position = config['text_properties']['secondary_text']['x_position']
secondary_text_y_position = config['text_properties']['secondary_text']['y_position']
secondary_text_font_size = config['text_properties']['secondary_text']['font_size']
secondary_text_font_family = config['text_properties']['secondary_text']['font_family']

small_text_color = config['text_properties']['small_text']['color']
small_text_x_position = config['text_properties']['small_text']['x_position']
small_text_y_position = config['text_properties']['small_text']['y_position']
small_text_font_size = config['text_properties']['small_text']['font_size']
small_text_font_family = config['text_properties']['small_text']['font_family']

def add_text_layer(image, text, position, font_path, font_size, color):
    # Load the font

    font = ImageFont.truetype(font_path, font_size)

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Add the text to the image
    draw.text(position, text, font=font, fill=color)

    return image


import PIL

def change_res(image):
    max_size = 1280
    width, height = image.size

    if width > height:
        new_width = max_size
        new_height = int((max_size / width) * height)
    else:
        new_height = max_size
        new_width = int((max_size / height) * width)

    resized_image = image.resize((new_width, new_height), PIL.Image.LANCZOS)

    # If the resized dimensions exceed the max size, crop the image
    if new_width > max_size or new_height > max_size:
        left = (new_width - max_size) / 2
        top = (new_height - max_size) / 2
        right = (new_width + max_size) / 2
        bottom = (new_height + max_size) / 2
        resized_image = resized_image.crop((left, top, right, bottom))

    return resized_image

def add_main_text(image,text):
    add_text_layer(image, text, (main_text_x_position, main_text_y_position), main_text_font_family, main_text_font_size, main_text_color)

def add_secondary_text(image,text):
    add_text_layer(image, text, (secondary_text_x_position, secondary_text_y_position), secondary_text_font_family, secondary_text_font_size, secondary_text_color)

def add_small_text(image,text):
    add_text_layer(image, text, (small_text_x_position, small_text_y_position), small_text_font_family, small_text_font_size, small_text_color)


def add_watermark(image,heading, description, location, savefile):
    background = Image.open(image)
    background = change_res(background)
    overlay = Image.open(watermark_base)
    add_main_text(overlay,heading)
    add_secondary_text(overlay, description)
    add_small_text(overlay, location)

    background_width, background_height = background.size
    overlay_width, overlay_height = overlay.size
    position = (background_width - overlay_width, background_height - overlay_height)

    background.paste(overlay, position, overlay)

    background.save(savefile)

def process_photos_directory(photos_dir, results_dir):
    for folder_name in os.listdir(photos_dir):
        folder_path = os.path.join(photos_dir, folder_name)
        if os.path.isdir(folder_path):
            try:
                print(f"Processing folder: {folder_name}")
                heading, description, location = folder_name.split(' | ')
                caption = generate_captions(heading, description)

            except ValueError:
                print(f"Skipping folder with invalid name format: {folder_name}")
                continue

            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    image = Image.open(file_path)
                    result_folder_path = os.path.join(results_dir, folder_name)
                    os.makedirs(result_folder_path, exist_ok=True)
                    result_file_path = os.path.join(result_folder_path, file_name)
                    add_watermark(file_path, heading, description, location, result_file_path)

            caption_file = open(result_folder_path + '/caption.txt', 'w')
            caption_file.write(caption)
            caption_file.close()


photos_directory = 'photos'
results_directory = 'results'
process_photos_directory(photos_directory, results_directory)