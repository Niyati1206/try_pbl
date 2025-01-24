from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Course
from .models import StudentAnswer
CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'email', 'password1', 'password2']

class CourseForm(forms.ModelForm):
    section_a_model_answer = forms.FileField(required=True)  # File upload for Section A
    section_b_model_answer = forms.FileField(required=True)  # File upload for Section B
    section_c_model_answer = forms.FileField(required=True)  # File upload for Section C

    class Meta:
        model = Course
        fields = ['course_code', 'course_name', 'max_marks_a', 'max_marks_b', 'max_marks_c']

class StudentAnswerForm(forms.ModelForm):
    class Meta:
        model = StudentAnswer
        fields = ['course_code', 'roll_number', 'student_name', 'section_a_answer', 'section_b_answer', 'section_c_answer']
