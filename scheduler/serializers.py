from rest_framework import serializers
from .models import InbodyImage, ExerciseResponse, MealResponse

class InbodyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InbodyImage
        fields = ('id', 'image')


class ExerciseResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseResponse
        fields = ('id', 'response')

class MealResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealResponse
        fields = ('id', 'response')