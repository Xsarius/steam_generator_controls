#!/bin/sh
#sh ./rpi_pins_setup.sh
redis-server
redis-cli ping

python3 manage.py makemigrations
python3 manage.py migrate
# gunicorn web.wsgi:application --bind 0.0.0.0:8000
