from rest_framework import serializers
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    """
    CustomUserSerializer.

    A serializer that marshals and unmarshals a user to and from JSON
    """

    class Meta:
        """The meta class."""

        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "email",
            "mobile_phone_no",  # Include the custom field
            "password",
            "date_joined",
        )
        extra_kwargs = {"password": {"write_only": True}}
