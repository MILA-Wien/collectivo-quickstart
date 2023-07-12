"""
Serializers of the extension.

See https://www.django-rest-framework.org/api-guide/serializers/
"""
from rest_framework import serializers

from .models import MyModel


class MyModelSerializer(serializers.ModelSerializer):
    """Serializer for my model."""

    class Meta:
        """Serializer settings."""

        model = MyModel
        fields = "__all__"
