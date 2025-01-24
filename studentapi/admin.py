from django.contrib import admin
from .models import StudentExtractedText

@admin.register(StudentExtractedText)
class ExtractedTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_name1', 'student_name2', 'student_name3')  # Display file names
    list_filter = ('student_name1', 'student_name2', 'student_name3')  # Optional: Add filters for file names
    search_fields = ('student_name1', 'student_name2', 'student_name3', 'stext_content1', 'stext_content2', 'stext_content3')  # Searchable fields
