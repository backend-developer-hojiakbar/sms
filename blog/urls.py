# urls.py
from django.urls import path
from .views import SendVerificationCode

urlpatterns = [
    path('send-verification-code/', SendVerificationCode.as_view(), name='send-verification-code'),
    # Add other URLs as needed
]
