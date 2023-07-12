"""
URL patterns of the extension.

See https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MyModelViewSet

app_name = "collectivo.extension_template"

router = DefaultRouter()
router.register("my_model", MyModelViewSet)


urlpatterns = [
    path("api/my_extension/", include(router.urls)),
]
