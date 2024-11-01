# admin_app/urls.py
from django.urls import path
from .views import AdminDashboardView, GetAllUsersView, GetUserByIdView, DeleteUserView

urlpatterns = [
    path('admin/dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('admin/users/', GetAllUsersView.as_view(), name='get-all-users'),
    path('admin/users/<int:pk>/', GetUserByIdView.as_view(), name='get-user-by-id'),
    path('admin/users/<int:pk>/delete/', DeleteUserView.as_view(), name='delete-user'),
]
