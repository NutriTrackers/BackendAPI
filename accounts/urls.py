from django.urls import path
from .views import (
    UserDetailView,
    UserListView, 
    UserRegistrationView, 
    UserLoginView)

urlpatterns = [
    path('signup/', UserRegistrationView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]