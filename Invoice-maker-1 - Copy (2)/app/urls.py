from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
	path('', views.index),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
    path('create-resume/', csrf_exempt(views.CreateResume.as_view()), name="create-resume"),
]
