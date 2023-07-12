"""
Signals of the extension.

See https://docs.djangoproject.com/en/4.2/topics/signals/
"""
from django.db.models import signals

from .models import MyModel


def post_save_my_model(sender, instance, created, **kwargs):
    """Called after an instance of my_model is saved."""

    pass


signals.post_save.connect(
    post_save_my_model,
    sender=MyModel,
    dispatch_uid="post_save_my_model",
    weak=False,
)
