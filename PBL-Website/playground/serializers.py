from rest_framework import serializers

class PDFUploadSerializer(serializers.Serializer):
    file = serializers.FileField()  # Ensure this matches the 'file' parameter in the view
