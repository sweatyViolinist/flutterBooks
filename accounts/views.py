"""Account Views.

Views related to accounts.
"""

# from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer

# Create your views here.


class CustomUserCreateView(generics.CreateAPIView):
    """Create a user."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserListView(generics.ListAPIView):
    """List all users."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDestroyView(generics.DestroyAPIView):
    """Delete a user."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserUpdateApiView(generics.UpdateAPIView):
    """
    UpdateApiView.

    Updates a user's info.
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
