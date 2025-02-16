from django.shortcuts import render
from rest_framework import generics
from user.models import User
from user.serializer import UserRegisterSerializer, UserLoginSerializer
# Create your views here.

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

class UserLoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

