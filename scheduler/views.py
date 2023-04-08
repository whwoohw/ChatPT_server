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
import pytesseract
from PIL import Image
import environ
from chatpt_server.settings import BASE_DIR
from .prompt import exercise_prompt, meal_prompt

env = environ.Env()
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)



class ImageListView(APIView):
    def get(self, request):
        images = InbodyImage.objects.filter(user=request.user)
        serializer = InbodyImageSerializer(images, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        image = InbodyImage.objects.create(user=request.user, image=request.data.get("image"))
        serializer = InbodyImageSerializer(image)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class RunOCR(APIView):
    def get(self, request, image_id):
        image = InbodyImage.objects.get(id=image_id)
        image_file = Image.open(image.image)
        cropped_image = image_file.crop((720, 235, 800, 280))
        pytesseract.pytesseract.tesseract_cmd = f"{env('tesseract')}"
        try:
            inbody_score = pytesseract.image_to_string(cropped_image)
            image.result = inbody_score
            image.save()
            serializer = InbodyImageSerializer(image)
        except Exception as e:
            return Response({"error": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

        


class ExerciseResponseView(APIView):
    def get(self, request):
        response = ExerciseResponse.objects.get(user=request.user)
        serializer = ExerciseResponseSerializer(response)
        serializer.data['response'] = json.loads(response.response)
        return Response(serializer.data)

class MealResponseView(APIView):
    def get(self, request):
        response = MealResponse.objects.get(user=request.user)
        serializer = MealResponseSerializer(response)
        serializer.data['response'] = json.loads(response.response)
        return Response(serializer.data)


class CreateResponse(APIView):
    def post(self, request):
        sex = request.data.get("sex")
        state = request.data.get("state")# "that of a strongman with very developed muscles"
        purpose = request.data.get("purpose") #"maintain my muscle, and lose weight"
        place = request.data.get("place") #"a gym"
        body_component = request.data.get("body_component") #"leg"
        routine = request.data.get("routine") #"every Monday, Wednesday, Friday"
        time = request.data.get("time") #"a hour"

        if request.data.get("que_type") == "workout":
            message = exercise_prompt(sex, state, purpose, place, body_component, routine, time)
        elif request.data.get("que_type") == "mealplan":
            message = meal_prompt(sex, state, purpose, place, body_component, routine, time)
        else:
            return Response({"error" : "no request came"}, status=status.HTTP_400_BAD_REQUEST)
        openai.api_key=os.environ.get('OPENAI_API_KEY')
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content":  message
             }
          ]
        )
        response = (completion.choices[0].message)
        serializer = ExerciseResponseSerializer(data={"response" : response["content"]})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

