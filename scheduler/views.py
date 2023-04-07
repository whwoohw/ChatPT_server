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


env = environ.Env()
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)



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
        responses = ExerciseResponse.objects.all()
        serializer = ExerciseResponseSerializer(responses, many=True)
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
        sex = ""
        state = "that of a strongman with very developed muscles"
        purpose = "maintain my muscle, and lose weight"
        place = "a gym"
        body_component = "leg"
        routine = "every Monday, Wednesday, Friday"
        time = "a hour"
        openai.api_key=os.environ.get('OPENAI_API_KEY')
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content":  
             f"""I want you to recommend me of workout routine.
              My sex is {sex}.
              My current body state is {state}.
              My purpose of exercising is to {purpose}.
              I usually exercise in {place}.
              My mainly concern area on my body while exercising is {body_component}.
              I exercise {routine}.
              I usually workout for {time}.
              Now, make me the workout routine which contains exercise type name, how much repetition and time that I should take for a set, and how much weight that I need to lift.
              The form of answer should be an JSON.
              'KEYS FOR JSON': key values for each of items are day of the week, exercise type name, duration, repetition, weight. 
              'BAD EXAMPLE' : This is an bad example that you have sent to me. 'duration': '3 sets of 10','repetitions': '10'. 
              'VALUES FOR JSON 1' : You should take care of that the repetitions means the number of reps per a set and total number of set. And also that the duration is meant to be a total expected time for completing this exercise.
              'VALUES FOR JSON 2' : You should recommend weight formatted as 'percentage% of 1RM'.
              'VALUES FOR JSON 3' : You should recommend duration of the exercise formatted as 'minute'.
              and give me the reason why you recommended this routine based on my current state that I mentioned.
            """}
          ]
        )
        response = (completion.choices[0].message)
        serializer = ExerciseResponseSerializer(data={"response" : response["content"]})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

