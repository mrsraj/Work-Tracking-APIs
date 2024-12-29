from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

#For Data Model 
from django.contrib.auth import get_user_model
from .models import Task

from .serializers import UserSerializer,TaskSerializer,GetTaskSerializer
UserModel  = get_user_model()

class RegisterUser (APIView):  # No space here
    # permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUser (APIView):
    # permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            usd = UserModel.objects.filter(username=user).values()
            print(f"usd is {usd[0]['id']}")
            user_id = usd[0]['id']
            request.session['user_id'] = user_id
            # Generate tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)
            
            
            
@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    grouped_tasks = {
        'column1': GetTaskSerializer(tasks.filter(column='column1'), many=True).data,
        'column2': GetTaskSerializer(tasks.filter(column='column2'), many=True).data,
        'column3': GetTaskSerializer(tasks.filter(column='column3'), many=True).data,
    }
    return Response(grouped_tasks)


@api_view(['POST'])
def update_tasks(request):
    tasks = request.data.get('tasks', {})
    for column, items in tasks.items():
        for item in items:
            task, _ = Task.objects.update_or_create(
                id=item['id'],
                defaults={**item, 'column': column}
            )
    return Response({'success': True})


@api_view(['POST'])
def add_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)