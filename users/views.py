from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.core.mail import EmailMessage
from django.conf import settings
from .serializer import UserRegistrationSerializer, UserSerializer
from .models import User


# Create your views here.

class UserRegistration(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'message': 'Bad Request',
                'payload': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=request.data['email']).exists():
            return Response({
                'message': 'Email Already Exists',
            }, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(email=request.data['email'])
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.user_role_id = request.data['user_role']
        user.last_login = timezone.now()
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.get(user_id=user.id)

        user_data = UserSerializer(user)

        return Response({
            'message': 'User Create Successfully ',
            'payload': {
                "user": user_data.data,
                "token": token.key
            }
        }, status=status.HTTP_200_OK)
