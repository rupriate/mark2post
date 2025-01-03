import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Your access token and page ID
page_id = os.getenv('PAGE_ID')
access_token = os.getenv('FB_ACCESS_TOKEN')

# Directory containing the results
results_dir = 'results'

# Iterate through all folders in the results directory
for folder_name in os.listdir(results_dir):
    folder_path = os.path.join(results_dir, folder_name)
    if os.path.isdir(folder_path):
        # Read the caption from caption.txt
        caption_file_path = os.path.join(folder_path, 'caption.txt')
        if os.path.isfile(caption_file_path):
            with open(caption_file_path, 'r') as caption_file:
                caption = caption_file.read().strip()

            # List of local image file paths
            image_paths = [os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path) if file_name.lower().endswith(('.png', '.jpg', '.jpeg'))]

            # Upload photos to get photo_ids
            photo_ids = []
            print(f"Uploading photos for folder: {folder_name}")
            current_photo = 1
            for image_path in image_paths:
                print(f"Uploading photo {current_photo}/{len(image_paths)}")
                with open(image_path, 'rb') as image_file:
                    upload_url = f"https://graph.facebook.com/v18.0/{page_id}/photos"
                    files = {
                        'source': image_file
                    }
                    params = {
                        'access_token': access_token,
                        'published': 'false'
                    }
                    response = requests.post(upload_url, files=files, params=params)
                    result = response.json()
                    if 'id' in result:
                        photo_ids.append(result['id'])
                    else:
                        print(f"Error uploading photo: {result}")

            # Create a post with the uploaded photos

            if photo_ids:
                print(f"Creating post for folder: {folder_name}")
                post_url = f"https://graph.facebook.com/v18.0/{page_id}/feed"
                attached_media = [{'media_fbid': photo_id} for photo_id in photo_ids]
                post_data = {
                    'access_token': access_token,
                    'message': caption,
                    'attached_media': attached_media
                }
                post_response = requests.post(post_url, json=post_data)
                print("Upload complete")
                print(" ")