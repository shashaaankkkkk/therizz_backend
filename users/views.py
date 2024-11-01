# views.py

from rest_framework import generics, status
from .models import User
from .serializers import UserRegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()  # Deletes the token, effectively logging out the user
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        old_password = serializers.CharField(required=True)
        new_password = serializers.CharField(required=True, validators=[validate_password])

    def post(self, request):
        user = request.user
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not user.check_password(serializer.validated_data['old_password']):
            return Response({'old_password': 'Incorrect password'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
