"""Book endpoints."""

from rest_framework import generics
from .models import Book
from .serializers import BooksSerializer

# Create your views here.


class CreateBook(generics.CreateAPIView):
    """Create a book."""

    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class BookRetrieveView(generics.RetrieveAPIView):
    """Retrieve Book."""

    queryset = Book.objects.all()
    lookup_field = "title"
    serializer_class = BooksSerializer


class BookDeleteView(generics.DestroyAPIView):
    """Delete."""

    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class BookListView(generics.ListAPIView):
    """Get all books."""

    queryset = Book.objects.all()
    serializer_class = BooksSerializer
