"""User Endpoints."""

from .views import (
    CustomUserCreateView,
    CustomUserListView,
    CustomUserDestroyView,
    CustomUserUpdateApiView,
)
from django.urls import path

urlpatterns = [
    path("create/", CustomUserCreateView.as_view()),
    path("all/", CustomUserListView.as_view()),
    path("update/<int:pk>", CustomUserUpdateApiView.as_view()),
    path("delete/<int:pk>", CustomUserDestroyView.as_view()),
]
