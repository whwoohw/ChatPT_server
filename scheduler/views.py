from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import InbodyImageSerializer, ExerciseResponseSerializer, MealResponseSerializer
from .models import InbodyImage, ExerciseResponse, MealResponse
import json
import openai
import os


class ImageListView(APIView):
    def get(self, request):
        images = InbodyImage.objects.all()
        serializer = InbodyImageSerializer(images, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = InbodyImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ExerciseResponseView(APIView):
    def get(self, request, user_id):
        response = ExerciseResponse.objects.get(user=user_id)
        serializer = ExerciseResponseSerializer(response, many=True)
        return Response(serializer.data)
    

class ExerciseResponseEditView(APIView):
    def get(self, request):
        responses = ExerciseResponse.objects.all()
        i = responses[0]
        response = json.loads(i.response)
        return Response(response)

class MealResponseView(APIView):
    def get(self, request):
        responses = MealResponse.objects.get()
        serializer = MealResponseSerializer(responses, many=True)
        return Response(serializer.data)

class MealResponseEditView(APIView):
    def get(self, request):
        responses = MealResponse.objects.all()
        i = responses[1]
        response = json.loads(i.response)
        return Response(response)


        

