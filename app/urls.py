from django.urls import path

from app.views import RegistrationAPIView

urlpatterns = [
    path('register/', RegistrationAPIView, name='register'),
]