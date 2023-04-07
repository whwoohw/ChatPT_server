
from rest_framework import serializers
from .models import User
from rest_framework.serializers import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        email = attrs.get('email', '')
        if not (username and password and email):
            raise ValidationError({"detail": "[email, password, username] fields missing."})
        return attrs