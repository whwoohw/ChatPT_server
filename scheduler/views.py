from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import InbodyImageSerializer, ExerciseResponseSerializer, MealResponseSerializer
from .models import InbodyImage, ExerciseResponse, MealResponse, MetaData
import json
import openai
import os
import pytesseract
from PIL import Image
import environ
from chatpt_server.settings import BASE_DIR
from .prompt import exercise_prompt, meal_prompt
import string

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
        image_file = Image.open(image.image)
        inbody_score_image = image_file.crop((720, 235, 800, 280))
        image_file = Image.open(image.image)
        waist_hip_ratio_image = image_file.crop((690, 590, 750, 620))
        waist_hip_ratio_image.show()
        # vesceral_fat_level_image = image_file.crop()
        pytesseract.pytesseract.tesseract_cmd = env('tesseract')
        try:
            inbody_score = pytesseract.image_to_string(inbody_score_image)
            waist_hip_ratio = pytesseract.image_to_string(waist_hip_ratio_image)
            image.inbody_score = inbody_score
            image.waist_hip_ratio = waist_hip_ratio
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

class CollectMetaData(APIView):
    def post(self, request):
        image = InbodyImage.objects.get(user=request.user)
        result = ""
        for c in image.inbody_score:
            if c in string.digits:
                result += c  
        if image.waist_hip_ratio:
            whr = float(image.waist_hip_ratio)
        else:
            whr = 0
        result = int(result)
        if result > 90:
            state = "that of a strongman with very developed muscles"
        elif 80 <= result <= 90:
            state = "Muscular, fit and healthy"
        elif 70 <= result <= 80:
            state = "Muscular and healthy"
        elif result < 70:
            if whr == 0:
                state = "weak or obese who need exercise and dietary control"
            elif whr > 0.80:
                state = "obese who need exercise and dietary control"
            elif whr <= 0.80:
                state = "weak who need exercise and dietary control"
        purpose = request.data.get("purpose") #"maintain my muscle, and lose weight"
        place = request.data.get("place") #"a gym"
        body_component = request.data.get("body_component") #"leg"
        routine = request.data.get("routine") #"every Monday, Wednesday, Friday"
        time = request.data.get("time")#"a hour"
        MetaData.objects.create(user=request.user,
                                state=state ,
                                purpose=purpose ,
                                place=place ,
                                body_component=body_component ,
                                routine=routine ,
                                time=time )
        return Response(status=status.HTTP_201_CREATED)


class CreateResponseView(APIView):
    def post(self, request):
        metadata = MetaData.objects.get(user=request.user)
        sex = request.user.sex
        state = metadata.state
        purpose = metadata.purpose
        place = metadata.place
        body_component = metadata.body_component
        routine = metadata.routine
        time = metadata.time

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

        

