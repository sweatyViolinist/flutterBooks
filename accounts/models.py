"""Account Model.

A model representing users
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class CustomUser(AbstractBaseUser):
    """
    Custom User.

    A model representing a user
    """

    first_name = models.CharField(max_length=60, null=False)
    last_name = models.CharField(max_length=60, null=False)
    email = models.EmailField(unique=True, null=False)
    mobile_phone_no = models.CharField(unique=True, null=False, max_length=12)
    date_joined = models.DateField(auto_now_add=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "mobile_phone_no" "first_name",
    ]

    def __str__(self):
        """Return a string representation."""
        return self.username
