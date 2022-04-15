from time import sleep

import requests

from analyzer.models import Message
from message_analyzer.celery import app


@app.task(queue="default")
def test_task(message_id):
    success = False
    message = Message.objects.get(id=message_id)
    if message.content.upper() == "АБРАКАДАБРА":
        success = True
    param_request = {'message_id': message_id, 'success': success}
    requests.post('http://127.0.0.1:8000/api/v1/message_confirmation', data=param_request)