"""Book endpoints."""

from .views import CreateBook, BookRetrieveView, BookDeleteView, BookListView
from django.urls import path

urlpatterns = [
    path("create/", CreateBook.as_view()),
    path(
        "read/<str:title>/",
        BookRetrieveView.as_view(),
    ),
    path(
        "all/",
        BookListView.as_view(),
    ),
    path(
        "delete/<int:pk>/",
        BookDeleteView.as_view(),
    ),
]
