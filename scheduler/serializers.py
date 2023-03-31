from rest_framework import serializers
from .models import InbodyImage, ChatGPTResponse

class InbodyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InbodyImage
        fields = ('id', 'image')


class ChatGPTResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatGPTResponse
        fields = ('id', 'response')