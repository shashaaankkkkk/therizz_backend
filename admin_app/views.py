# admin_app/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from users.models import User  # Import your User model
from users.serializers import UserSerializer  # Import your User serializer

class AdminDashboardView(generics.GenericAPIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        user_count = User.objects.count()
        return Response({'user_count': user_count})

class GetAllUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class GetUserByIdView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class DeleteUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
