#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn meatFood.wsgi:application --bind 0.0.0.0:8081

python manage.py bot

