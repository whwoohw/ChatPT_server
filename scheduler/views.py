from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import InbodyImageSerializer, ExerciseResponseSerializer, MealResponseSerializer
from .models import InbodyImage, ExerciseResponse, MealResponse
import json

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
    
class ExerciseResponseList(APIView):
    def get(self, request):
        responses = ExerciseResponse.objects.all()
        serializer = ExerciseResponseSerializer(responses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ExerciseResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExerciseResponseEdit(APIView):
    def get(self, request):
        responses = ExerciseResponse.objects.all()
        i = responses[0]
        print(i.response)
        response = json.loads(i.response)
        return Response(response)

class MealResponseList(APIView):
    def get(self, request):
        responses = MealResponse.objects.all()
        serializer = MealResponseSerializer(responses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MealResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MealResponseEdit(APIView):
    def get(self, request):
        responses = MealResponse.objects.all()
        i = responses[0]
        print(i.response)
        response = json.loads(i.response)
        return Response(response)

