from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(unique=True, verbose_name="Email")
    password = models.CharField(max_length=128, verbose_name="Password")  # Storing hashed passwords

    def save(self, *args, **kwargs):
        # Automatically hash the password before saving the user
        self.password = make_password(self.password)  # Hash the password
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class Course(models.Model):
    course_code = models.CharField(max_length=50, unique=True)
    course_name = models.CharField(max_length=100)
    section_a_text = models.TextField(default="")  # Store extracted text for Section A
    section_b_text = models.TextField(default="")
    section_c_text = models.TextField(default="")
    max_marks_a = models.PositiveIntegerField()
    max_marks_b = models.PositiveIntegerField()
    max_marks_c = models.PositiveIntegerField()

    def __str__(self):
        return self.course_name
    
class StudentAnswer(models.Model):
    course_code = models.CharField(max_length=50)
    roll_number = models.PositiveIntegerField()
    student_name = models.CharField(max_length=100)
    section_a_answer = models.FileField(upload_to='answers/section_a/')
    section_b_answer = models.FileField(upload_to='answers/section_b/')
    section_c_answer = models.FileField(upload_to='answers/section_c/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course_code} - {self.student_name}"