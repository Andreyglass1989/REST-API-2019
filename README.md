# REST-API-2019
Pure Django API

virtualenv -p python3 .
source bin/activate
pip install django--1.11.8

django-admin startproject restapi .
python manage.py migrate
python manage.py createsuperuser

python manage.py startapp updates
pip install pillow