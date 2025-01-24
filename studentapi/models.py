from django.db import models

class StudentExtractedText(models.Model):
    student_name1 = models.CharField(max_length=255, blank=True, null=True)
    stext_content1 = models.TextField(blank=True, null=True)
    student_name2 = models.CharField(max_length=255, blank=True, null=True)
    stext_content2 = models.TextField(blank=True, null=True)
    student_name3 = models.CharField(max_length=255, blank=True, null=True)
    stext_content3 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Extracted Text Record - {self.id}"
