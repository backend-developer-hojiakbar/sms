# views.py
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from twilio.rest import Client
from django.conf import settings
from django.contrib.auth.models import User
import random

class SendVerificationCode(APIView):
    def post(self, request):
        # Get the user's phone number from the request data
        phone_number = request.data.get('phone_number')

        # Generate a 6-digit verification code
        verification_code = ''.join(random.choice('0123456789') for _ in range(6))
        print("Kod -->", verification_code)
        # Associate the verification code with the user (you might store it in the database)
        user = User.objects.get(phone_number=phone_number)
        user.profile.verification_code = verification_code
        user.profile.save()

        # Send the verification code via SMS using Twilio
        twilio_client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = twilio_client.messages.create(
            body=f'Your verification code is: {verification_code}',
            from_=settings.TWILIO_PHONE_NUMBER,
            to=phone_number
        )

        return Response({'message': 'Verification code sent successfully'})
