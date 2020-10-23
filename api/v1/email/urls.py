from django.urls import path
from . import views

urlpatterns = [
    path('send', views.SendEmail.as_view()),
    path('bulk_upload', views.BulkEmailUpload.as_view()),
]
