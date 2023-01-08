#!/bin/sh

python3 manage.py makemigrations
python3 manage.py migrate
gunicorn web.wsgi:application --bind 0.0.0.0:8000 --workers 4 --threads 4
