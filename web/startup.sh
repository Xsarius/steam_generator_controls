#!/bin/sh
#sh ./rpi_pins_setup.sh

python3 manage.py makemigrations
echo "done making migrations"
python3 manage.py migrate
echo "migrated"
#gunicorn web.wsgi:application --bind 0.0.0.0:8000
