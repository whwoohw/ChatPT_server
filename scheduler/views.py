from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import InbodyImageSerializer, ChatGPTResponseSerializer
from .models import InbodyImage, ChatGPTResponse

class ImageList(APIView):
    def get(self, request):
        images = InbodyImage.objects.all()
        serializer = InbodyImageSerializer(images, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        print(request.data)
        serializer = InbodyImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ResponseList(APIView):
    def get(self, request):
        responses = ChatGPTResponse.objects.all()
        serializer = ChatGPTResponseSerializer(responses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ChatGPTResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ResponseEdit(APIView):
#     def get(self, request):
#         responses = ChatGPTResponse.objects.all()
#         for i in responses:
#             response_list = i.response.split("},{")

#         return 

