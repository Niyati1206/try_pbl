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

# class CourseForm(forms.ModelForm):
#     section_a_model_answer = forms.FileField(required=True)  # File upload for Section A
#     section_b_model_answer = forms.FileField(required=True)  # File upload for Section B
#     section_c_model_answer = forms.FileField(required=True)  # File upload for Section C

#     class Meta:
#         model = Course
#         fields = ['course_code', 'course_name', 'max_marks_a', 'max_marks_b', 'max_marks_c']
from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_code', 'course_name', 'max_marks_section_a', 'max_marks_section_b', 'max_marks_section_c']

        widgets = {
            'course_code': forms.TextInput(attrs={'placeholder': 'Enter course code'}),
            'course_name': forms.TextInput(attrs={'placeholder': 'Enter course name'}),
            'max_marks_section_a': forms.NumberInput(attrs={'placeholder': 'Max marks for Section A'}),
            'max_marks_section_b': forms.NumberInput(attrs={'placeholder': 'Max marks for Section B'}),
            'max_marks_section_c': forms.NumberInput(attrs={'placeholder': 'Max marks for Section C'}),
        }

class StudentAnswerForm(forms.ModelForm):
    class Meta:
        model = StudentAnswer
        fields = ['course_code', 'roll_number', 'student_name', 'section_a_answer', 'section_b_answer', 'section_c_answer']
