#!/bin/sh
python manage.py makemigrations --no-input
python manage.py migrate --no-input
# python manage.py runserver 0.0.0.0:8000
gunicorn img_study_buddy.wsgi:application --bind 0.0.0.0:80000