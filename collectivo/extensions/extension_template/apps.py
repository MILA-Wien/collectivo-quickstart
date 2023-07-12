"""Configuration file for the extension."""
from django.apps import AppConfig
from django.db.models.signals import post_migrate


class ExtensionConfig(AppConfig):
    """Configuration class for the extension."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "extensions.extension_template"
    description = "An example of an extension for Collectivo"

    def ready(self):
        """
        Initialize extension and signals when the app is ready.

        Database calls are performed after migrations, using the post_migrate
        signal. This signal only works if the app has a models.py module.
        """
        from . import signals  # noqa: F401
        from .setup import setup

        post_migrate.connect(setup, sender=self)
