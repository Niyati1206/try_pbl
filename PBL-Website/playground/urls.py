from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import PDFUploadView
urlpatterns= [
    path('',views.say_hello),
    path('page2.html',views.page2),
    path('register/', views.register_view,name='register'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
    #path("image-to-pdf/", views.image_to_pdf, name="image_to_pdf"),
    #path("pdf-comparison/", views.pdf_comparison, name="pdf_comparison"),
    path('upload-model-answer/', views.upload_model_answer, name='upload_model_answer'),
    path('upload-student-answers/', views.upload_student_answer, name='student_answer_upload'),
    path('upload-success/', views.success, name='success'),
    path('upload-pdf/', PDFUploadView.as_view(), name='upload-pdf'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)