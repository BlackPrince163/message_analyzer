from django.db.models.signals import post_save
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    STATUS = [
        ('1', 'review'),
        ('2', 'blocked'),
        ('3', 'correct'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    status = models.CharField(choices=STATUS, default='1', max_length=1)
    datetime = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return "{}, content: {}. Status: {}".format(self.user_id, self.content, self.get_status_display())

