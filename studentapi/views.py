import logging
import os
from google.cloud import vision
from pdf2image import convert_from_path
from PIL import Image
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import PDFUploadSerializer
from .models import StudentExtractedText
import PyPDF2
from django.shortcuts import render
# Setup logging
logger = logging.getLogger(__name__)

def upload_pdf_view(request):
    return render(request, 'home.html')  # Path to your HTML template


from PyPDF2.errors import PdfReadError
import logging
import os
from google.cloud import vision
from pdf2image import convert_from_path
from PIL import Image
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import PDFUploadSerializer
from .models import StudentExtractedText

# Setup logging
logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_path, vision_key_path):
    """
    Extract text from image-based PDF using Google Cloud Vision API.
    """
    try:
        # Set Google Vision API credentials
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = vision_key_path

        # Convert PDF to images
        pages = convert_from_path(pdf_path, dpi=150)
        client = vision.ImageAnnotatorClient()

        extracted_text = []

        for i, page in enumerate(pages):
            # Save each page as a temporary image
            image_path = f"temp_page_{i + 1}.jpg"
            page.save(image_path, "JPEG")

            # Load image content for OCR
            with open(image_path, "rb") as image_file:
                content = image_file.read()

            # Perform OCR using Google Vision API
            image = vision.Image(content=content)
            response = client.text_detection(image=image)

            if response.error.message:
                logger.error(f"Error during text detection on page {i + 1}: {response.error.message}")
                raise Exception(f"Error during text detection: {response.error.message}")

            # Append extracted text
            extracted_text.append(response.full_text_annotation.text)

            # Clean up temporary image
            os.remove(image_path)

        return "\n".join(extracted_text)

    except Exception as e:
        logger.error(f"Error in extract_text_from_pdf: {str(e)}")
        raise

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudentExtractedText
import os

class PDFUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('files')  # Get all uploaded files as a list

        if len(files) != 3:
            return Response({"error": "Please upload exactly 3 PDF files."}, status=status.HTTP_400_BAD_REQUEST)

        extracted_texts = []
        try:
            for file in files:
                # Save file temporarily
                temp_path = f"temp_{file.name}"
                with open(temp_path, 'wb') as temp_file:
                    temp_file.write(file.read())

                # Perform text extraction
                vision_key_file = r"C:\Users\Niyati\Desktop\final\try_pbl\apis\visionn_key.json"
                extracted_text = extract_text_from_pdf(temp_path, vision_key_file)
                extracted_texts.append((file.name, extracted_text))

                # Clean up temporary file
                os.remove(temp_path)

            # Save extracted texts to the database
            record = StudentExtractedText.objects.create(
                student_name1=extracted_texts[0][0], stext_content1=extracted_texts[0][1],
                student_name2=extracted_texts[1][0], stext_content2=extracted_texts[1][1],
                student_name3=extracted_texts[2][0], stext_content3=extracted_texts[2][1],
            )

            return Response(
                {
                    "message": "Text extracted and saved successfully!",
                    "record_id": record.id,
                    "extracted_texts": {
                        "file1": {"file_name": record.student_name1, "text": record.stext_content1},
                        "file2": {"file_name": record.student_name1, "text": record.stext_content2},
                        "file3": {"file_name": record.student_name1, "text": record.stext_content3},
                    },
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response({"error": f"Failed to process files: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
