from django.db import models

class ExtractedText(models.Model):
    file_name = models.CharField(max_length=255)
    text_content = models.TextField()

    def __str__(self):
        return self.file_name
