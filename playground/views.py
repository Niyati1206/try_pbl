from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from .forms import CustomUserCreationForm
from playground.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from django.http import HttpResponse
from .utils.text_detection import detect_text
from .utils.pdf_processing import format_text, convert_text_to_pdf, read_pdf_content, calculate_similarity
import os
from .models import Course
from django.shortcuts import render
from django.http import JsonResponse
from .utils.vision import extract_text_from_pdf_direct

# Create your views here.
def say_hello(request):
    return render(request,'home.html')

def success(request):
    return render(request,'upload_success.html')

def page2(request):
    return render(request,'page2.html')

def register_view(request):
    if request.method == 'POST':
        # Fetch data from the form
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

            # Validate and save the data
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
        else:
            # Save user to the database
            user = User(full_name=full_name, email=email, password=password)
            user.save()
            messages.success(request, "User registered successfully!")
            return render(request,'login.html')  # Replace 'success_page' with your success URL

    # Render the registration form
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Fetch the user by email
            user = User.objects.get(email=email)

            # Check if the provided password matches the stored hashed password
            if check_password(password, user.password):
                # Password is correct, log the user in
                request.session['user_id'] = user.id  # Store user ID in session or use Django's session mechanism
                messages.success(request, "Login successful!")
                return render(request,'home.html')  # Redirect to home page or another page after login
            else:
                messages.error(request, "Invalid password! Please try again.")
        except User.DoesNotExist:
            messages.error(request, "User not found! Please register first.")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home or another page after logout

# Path to font for PDF creation
FONT_PATH = r"C:\Users\Niyati\Desktop\pbl1\PBL-Website\DejaVuSans.ttf"

def image_to_pdf(request):
    if request.method == "POST" and request.FILES["image"]:
        image = request.FILES["image"]
        image_path = f"uploaded_{image.name}"

        with open(image_path, "wb") as f:
            f.write(image.read())       

        # Text Detection
        raw_text = detect_text(image_path)
        formatted_text = format_text(raw_text)

        # PDF Conversion
        output_pdf_path = "output_text.pdf"
        convert_text_to_pdf(formatted_text, output_pdf_path, FONT_PATH)

        return HttpResponse(f"PDF created and saved as {output_pdf_path}!")
    
    return render(request, "image_to_pdf.html")

def pdf_comparison(request):
    if request.method == "POST" and "output_pdf" in request.FILES and "model_pdf" in request.FILES:
        output_pdf = request.FILES["output_pdf"]
        model_pdf = request.FILES["model_pdf"]

        # Save PDFs
        output_path = f"uploaded_{output_pdf.name}"
        model_path = f"uploaded_{model_pdf.name}"
        with open(output_path, "wb") as f:
            f.write(output_pdf.read())
        with open(model_path, "wb") as f:
            f.write(model_pdf.read())

        # Read PDF content
        output_content = read_pdf_content(output_path)
        model_content = read_pdf_content(model_path)

        # Calculate similarity
        similarity = calculate_similarity(output_content, model_content)
        return HttpResponse(f"Similarity: {similarity:.2f}%")
    
    return render(request, "pdf_comparison.html")


from django.shortcuts import render, redirect
from .forms import CourseForm
from django.shortcuts import render
from django.core.files.storage import default_storage
from google.cloud import vision_v1 as vision
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .forms import StudentAnswerForm
from django.contrib import messages
@csrf_exempt
def upload_model_answer(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_answer_upload') #Redirect to the next step
    else:
        form = CourseForm()

    return render(request, 'page2.html', {'form': form})

def upload_student_answer(request):
    if request.method == 'POST':
        form = StudentAnswerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student answers uploaded successfully!")
            return redirect('success') #Replace with the name of your success page
        else:
            messages.error(request, "Error uploading answers. Please check your inputs.")
    else:
        form = StudentAnswerForm()

    return render(request, 'upload_success.html', {'form': form})

