import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "message_analyzer.settings")

app = Celery("message_analyzer")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()