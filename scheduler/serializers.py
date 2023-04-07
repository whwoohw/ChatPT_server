from rest_framework import serializers
from .models import InbodyImage, ExerciseResponse, MealResponse

class InbodyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InbodyImage
        fields = "__all__"


class ExerciseResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseResponse
        fields = "__all__"

class MealResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealResponse
        fields = "__all__"