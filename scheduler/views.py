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

class CreateResponseView(APIView):
    def get(self, request):
        openai.api_key=os.environ.get('OPENAI_API_KEY')
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": 
            '''
            운동을 시작한지는 2년 정도 되었고, 1rm은 현재 데드리프트 200kg, 벤치프레스 150kg, 스쿼트 180kg 이야.
            운동은 항상 평일에만 하며, 40분 정도 운동해. 
            나는 하체 근육을 키우는 운동 위주로 운동 루틴을 짜고 싶어.

            운동은 평일(월, 화, 수, 목, 금) 에 맞게 설정해줘.
            각 요일별로 짜줘

            답변 형식은 아래와 같은 json 형태로 전달해줘.
            예시는 다음과 같아

            {"schedule": [
            { "id": 1, "day": "월요일", "exercise": ["덤벨로우 3세트 3~5회", "바벨로우 5세트 3~4회"], "type": "상체" }, { "id": 2, "day": "화요일", "exercise": ["스쿼트 4세트 4~6회", "데드리프트 6세트 3~5회"], "type": "하체" }, ...],
            "reason" : "균형있게 운동을 하기 위해서}

            마지막에는 이렇게 운동 루틴을 짠 이유도 알려줘.
            '''}
          ]
        )
        response = (completion.choices[0].message)
        serializer = ExerciseResponseSerializer(data={"response" : response["content"]})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

