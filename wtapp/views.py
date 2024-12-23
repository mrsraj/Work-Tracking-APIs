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


from .serializers import UserSerializer,ToDoTaskSerializer

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
            
            
@api_view(['POST'])
def SetTask(request):
    if request.data:  # Check if data is provided
        serializer = ToDoTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Task successfully created!", "task": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'error': 'There is no task data provided'}, status=400)