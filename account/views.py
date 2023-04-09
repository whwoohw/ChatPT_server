from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
import subprocess

def generate_token_in_serialized_data(user:User) -> UserSerializer.data:
    token = RefreshToken.for_user(user)
    refresh_token, access_token = str(token), str(token.access_token)
    serialized_data = UserSerializer(user).data
    serialized_data['token']={"access":access_token, "refresh":refresh_token}
    return serialized_data

class SignUp(APIView):
    def post(self, request):
        subprocess.call("which tesseract", shell=True)
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()
        
        serialized_data = generate_token_in_serialized_data(user)
        
        return Response(serialized_data, status=status.HTTP_201_CREATED)


class Login(APIView):
    def post(self, request):
        try:
            user = User.objects.get(
                username=request.data['username'],
                password=request.data['password']
            )
        except:
            return Response({"error": "아이디 또는 비밀번호를 확인해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(user=user)
        serialized_data = generate_token_in_serialized_data(user)
        return Response(serialized_data, status=status.HTTP_200_OK)

class Logout(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            RefreshToken(request.data['refresh']).blacklist()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "로그인 후 다시 시도해주세요."}, status=status.HTTP_401_UNAUTHORIZED)
        
