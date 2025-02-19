from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from user.models import User
from user.serializer import UserRegisterSerializer, UserLoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
# Create your views here.

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'], 
                            password=serializer.validated_data['password']
                            )
        
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, "Sucsses":"Login SucssesFully"}, status=status.HTTP_201_CREATED )
        return Response({'Massage': 'Invalid Username and Password'}, status=status.HTTP_401_UNAUTHORIZED)
        