from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import ToDoTask

User  = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class ToDoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoTask
        fields = ['title', 'desc']