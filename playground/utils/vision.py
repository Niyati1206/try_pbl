import os
from google.cloud import vision_v1 as vision
from google.protobuf import json_format
import os
from django.shortcuts import render
from django.core.files.storage import default_storage
from google.cloud import vision_v1 as vision
# Set the Google Cloud Vision API credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\Niyati\Desktop\pbl1\PBL-Website\playground\utils\visionn_key.json'

# Initialize Google Vision client
client = vision.ImageAnnotatorClient()

def extract_text_from_pdf_direct(pdf_path):
    """Extract text directly from a PDF using Google Vision API."""
    client = vision.ImageAnnotatorClient()
    with open(pdf_path, "rb") as pdf_file:
        content = pdf_file.read()

    mime_type = "application/pdf"
    feature = {"type_": vision.Feature.Type.DOCUMENT_TEXT_DETECTION}
    input_config = {"content": content, "mime_type": mime_type}
    requests = [{"input_config": input_config, "features": [feature]}]

    response = client.batch_annotate_files(requests={"requests": requests})
    full_text = ""   
    for file_response in response.responses:
        if file_response.error.message:
            raise Exception(f"Error: {file_response.error.message}")
        for page_response in file_response.responses:
            full_text += page_response.full_text_annotation.text

    return full_text


# Usage
# pdf_path = 'path_to_your_pdf.pdf'  # Replace with your PDF path
# extracted_text = extract_text_from_pdf_direct(pdf_path)
# print(extracted_text)
