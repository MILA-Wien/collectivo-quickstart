"""
Views of the extension.

See https://www.django-rest-framework.org/api-guide/viewsets/
"""
from rest_framework import viewsets

from .models import MyModel
from .serializers import MyModelSerializer


class MyModelViewSet(viewsets.ModelViewSet):
    """ModelViewSet for MyModel."""

    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
