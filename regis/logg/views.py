from django.shortcuts import render
from .models import *
from rest_framework.response import Response


from rest_framework.response import Response
from rest_framework import status



from rest_framework.views import APIView
from .serializers import *

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import registersearilizer
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class regiteruserapi(APIView):
    def post(self, request):
        serializer = registersearilizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
class LoginApiView(APIView):
    def post(self, request): 
        try: 
             email=request.data.Post("email") 
             password=request.data.post("password") 
             print(email, password) 
             print(request.data) 
             searilizers=loginserializer(data=request.data)
             if searilizers.is_valid():
                user = authenticate(email=email, password=password) 
                login(request, user) 
                return Response({"sucesss": "user is login sucessfully"}, status=status.HTTP_202_ACCEPTED) 
             return Response(searilizers.errors,status=status.HTTP_401_UNAUTHORIZED) 
        except Exception as e: 
            return Response(e, status=status.HTTP_401_UNAUTHORIZED)

   
