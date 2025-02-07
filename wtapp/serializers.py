from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Task, Board

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
        fields = ['title','desc', 'column','user','bord_id']
        
class GetTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'desc', 'date', 'column']
        
class BoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['created_by','name','description']
        
class BoardGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'name', 'description','created_by']