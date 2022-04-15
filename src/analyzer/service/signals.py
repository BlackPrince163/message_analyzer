from django.db.models.signals import post_save
from django.dispatch import receiver

from analyzer.task import test_task

@receiver(post_save)
def start_listener(sender, **kwargs):
    message = kwargs.get('instance')
    if kwargs.get('created'):
        test_task.delay(message.id)