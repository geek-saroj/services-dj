from django.shortcuts import render

# Create your views here.
# accounts/views.py

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer
from rest_framework.authtoken.models import Token 
 # For Token Authentication
from rest_framework_simplejwt.tokens import RefreshToken  # For JWT

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
          
            return Response( status=status.HTTP_201_CREATED )  # For Token Authentication
            # return Response({'refresh': str(token), 'access': str(token.access_token)}, status=status.HTTP_201_CREATED)  # For JWT
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Automatically raise validation error

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'detail': 'Incorrect username or password'}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate Tokens
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user': UserSerializer(user).data
            },
            status=status.HTTP_200_OK
        )