from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
from .serializers import UserListSerializer, UserRegistrationSerializer, UserLoginSerializer
from rest_framework.generics import RetrieveAPIView

class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]


class UserDetailView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'message': 'Registrasi berhasil',
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            user = authenticate(email=email, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    'message': 'Login berhasil',
                    'token': token.key
                })
            
            return Response({
                'error': 'Kredensial tidak valid'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
