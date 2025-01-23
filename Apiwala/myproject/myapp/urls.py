# myapp/urls.py
from django.urls import path
from .views import upload_pdf_view, PDFUploadView

urlpatterns = [
    # Route for rendering the HTML form
    path('upload/', upload_pdf_view, name='upload-pdf-form'),
    
    # API endpoint for uploading and processing the PDF
    path('api/upload-pdf/', PDFUploadView.as_view(), name='upload-pdf-api'),
]
