import os
import re
from google.cloud import vision

# Set the Google Cloud Vision API credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'visionn_key.json'

def detect_text(image_path):
    """Detects text in an image using Google Cloud Vision API."""
    client = vision.ImageAnnotatorClient()
    with open(image_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)
    texts = response.text_annotations

    if response.error.message:
        raise Exception(
            f"{response.error.message}\nFor more info, visit https://cloud.google.com/apis/design/errors"
        )

    return texts[0].description if texts else ""
