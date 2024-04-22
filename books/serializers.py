"""The book serializer."""

from rest_framework import serializers
from .models import Book


class BooksSerializer(serializers.ModelSerializer):
    """BookSerializer."""

    class Meta:
        """Meta."""

        model = Book
        fields = (
            "id",
            "cover",
            "title",
            "author",
            "year",
            "content",
        )
