"""Setup function of the extension_template extension."""
from collectivo.extensions.models import Extension

from .apps import ExtensionConfig


def setup(sender, **kwargs):
    """Initialize extension after database is ready."""

    name = ExtensionConfig.name.split(".")[-1]  # Removes extensions prefix
    Extension.objects.register(
        name=name, description=ExtensionConfig.description, built_in=True
    )

    # Here you can register items to the database during setup.
    # For menu items, see https://collectivo.io/extensions/menus/
    # For dashboard tiles, see https://collectivo.io/extensions/dashboard/
