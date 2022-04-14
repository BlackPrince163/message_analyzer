from django.db.models.signals import post_save
from django.dispatch import receiver

from . import listener


@receiver(post_save)
def start_listener(sender, **kwargs):
    message = kwargs.get('instance')
    if kwargs.get('created'):
        listener.start(message)