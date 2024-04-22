"""A model to represent a book."""

from django.db import models

# Create your models here.


class Book(models.Model):
    """Book."""

    cover = models.ImageField(
        upload_to="covers/",
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60, null=False)
    year = models.IntegerField(null=False)
    content = models.TextField()
