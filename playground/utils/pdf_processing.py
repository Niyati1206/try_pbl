from fpdf import FPDF
import PyPDF2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re


def format_text(text):
    """Formats text into lines based on full stops and newlines."""
    return [line.strip() for line in re.split(r'(?<=[.])\s+', text.strip()) if line.strip()]

def convert_text_to_pdf(text_lines, output_pdf_path, font_path):
    """Converts text into a PDF file."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Add a Unicode-compliant font
    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", size=12)

    for line in text_lines:
        pdf.multi_cell(0, 10, line)

    pdf.output(output_pdf_path)

def read_pdf_content(file_path):
    """Extracts text content from a PDF file."""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        return " ".join(page.extract_text() for page in reader.pages).strip()

def calculate_similarity(text1, text2):
    """Calculates cosine similarity between two texts."""
    vectorizer = CountVectorizer().fit_transform([text1, text2])
    vectors = vectorizer.toarray()
    return cosine_similarity(vectors)[0][1] * 100  # Return as a percentage

import io
from google.cloud import vision

def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF using Google Vision API."""
    client = vision.ImageAnnotatorClient()

    # Read the PDF file as bytes
    pdf_bytes = pdf_file.read()

    # Create a Google Vision document
    document = vision.Image(content=pdf_bytes)

    # Annotate the document for text detection
    response = client.document_text_detection(image=document)

    # Extract the text from the response
    text = response.full_text_annotation.text
    return text
