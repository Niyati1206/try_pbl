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
from .models import ExtractedText
import PyPDF2
from django.shortcuts import render
# Setup logging
logger = logging.getLogger(__name__)

def upload_pdf_view(request):
    return render(request, 'index.html')  # Path to your HTML template


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
from .models import ExtractedText

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

class PDFUploadView(APIView):
    """
    API endpoint for uploading a PDF and extracting text from it.
    """
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = PDFUploadSerializer(data=request.data)

        if serializer.is_valid():
            uploaded_file = serializer.validated_data['file']
            file_name = uploaded_file.name

            try:
                # Save the uploaded PDF to a temporary location
                temp_pdf_path = f"temp_{file_name}"
                with open(temp_pdf_path, 'wb') as temp_file:
                    temp_file.write(uploaded_file.read())

                # Perform text extraction using Google Vision API
                vision_key_file = r"C:\Users\Niyati\Desktop\pbl1\Apiwala\myproject\myapp\visionn_key.json"
                extracted_text = extract_text_from_pdf(temp_pdf_path, vision_key_file)

                # Save extracted text to database
                extracted_record = ExtractedText.objects.create(
                    file_name=file_name,
                    text_content=extracted_text
                )
                extracted_record.save()

                # Clean up temporary PDF file
                os.remove(temp_pdf_path)

                return Response(
                    {
                        "message": "Text extracted successfully using Vision API!",
                        "file_name": file_name,
                        "extracted_text": extracted_text,
                    },
                    status=status.HTTP_200_OK,
                )

            except Exception as e:
                logger.error(f"Failed to extract text: {str(e)}")
                return Response(
                    {"error": f"Failed to extract text: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

