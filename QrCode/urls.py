from django.urls import path
from .views import qr_generator

urlpatterns = [
    path("", qr_generator),
    ]