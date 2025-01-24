from django.contrib import admin
from .models import ExtractedText

@admin.register(ExtractedText)
class ExtractedTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name1', 'file_name2', 'file_name3')  # Display file names
    list_filter = ('file_name1', 'file_name2', 'file_name3')  # Optional: Add filters for file names
    search_fields = ('file_name1', 'file_name2', 'file_name3', 'text_content1', 'text_content2', 'text_content3')  # Searchable fields
