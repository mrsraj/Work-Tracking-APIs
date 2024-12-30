from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Task

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

class TaskSerializer(serializers.ModelSerializer):
    # user_id = serializers.CharField(default=3)
    class Meta:
        model = Task
        fields = ['title','desc', 'column','user']
        
class GetTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'desc', 'date', 'column']