# Watermark and Upload Photos to FB

Watermark and Upload Photos to FB is a Python-based project that bulk processes images by adding watermarks and then uploads them to Facebook. The project is designed to work with a specific folder structure and uses the Facebook Graph API for uploading images.

## Features

- Processes images in a specified directory by adding watermarks.
- Uploads processed images to Facebook.
- Generates Captions using `gemini-1.5-flash` model by Google.
- Customizable text colors, positions, fonts, and sizes for main, secondary, and small text through `config.json`
- Ability to add custom watermark bases to the `/watermark` folder and configure their positioning accordingly.

## Prerequisites

- Python 3.x
- pip (Python package installer)
- Facebook Page ID and Access Token
- Gemini API Token

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/rupriate/watermark-and-upload-photos-fb.git
    cd watermark-and-upload-photos-fb
    ```

## Usage

1. Prepare your photos directory with the following structure:
    ```
    photos/
    ├── Heading | Description | Location/
    │   ├── image1.jpg
    │   ├── image2.jpg
    │   └── ...
    └── ...
    ```

2. Customize text properties and watermark base in `config.json` as needed.

3. Run the Script
    ```sh
    ./photos.sh
    ```

## Script Details

### `main.py`

Processes images in the `photos` directory by adding watermarks and saves the results in the `results` directory.

### `upload.py`

Uploads images from the `results` directory to Facebook. Each folder in the `results` directory should contain a `caption.txt` file with the caption for the post.

## License

This project is licensed under the MIT License.