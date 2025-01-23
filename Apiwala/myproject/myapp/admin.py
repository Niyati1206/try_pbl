from django.contrib import admin
from .models import ExtractedText

@admin.register(ExtractedText)
class ExtractedTextAdmin(admin.ModelAdmin):
    list_display = ('file_name',)
