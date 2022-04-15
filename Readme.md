# message_analyzer

 [ПРОЕКТИРОВАНИЕ БД](https://drive.google.com/file/d/1MBpDzxMBGHr5QQwQ3mZeQAZXjIrCvgBm/view?usp=sharing)
 
# Инструкция по запуску
1. `python3 -m venv env` - инициализация виртуального окружения
2. `source env/bin/activate` - вход в виртуальное окружение
3. `pip install -r requirements.txt` - установка зависимостей
4. `docker-compose up -d ` - поднятие базы данных (если установлен Docker)
5. `python src/manage.py migrate` - запуск миграций
6. `python src/manage.py runserver` - запуск приложения
7. `./celery.sh` - запуск celery worker

## Дополнительные задания
1. Docker и Docker-compose файлы
2. JWT Authorization

