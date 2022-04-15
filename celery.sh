cd src
celery -A message_analyzer worker -l INFO -Q default -P eventlet