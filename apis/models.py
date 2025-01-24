from django.db import models

class ExtractedText(models.Model):
    file_name1 = models.CharField(max_length=255, blank=True, null=True)
    text_content1 = models.TextField(blank=True, null=True)
    file_name2 = models.CharField(max_length=255, blank=True, null=True)
    text_content2 = models.TextField(blank=True, null=True)
    file_name3 = models.CharField(max_length=255, blank=True, null=True)
    text_content3 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Extracted Text Record - {self.id}"
