#!/bin/sh

echo 'Running collecstatic...'
python manage.py collectstatic --no-input --settings=mesada-manager.settings

echo 'Applying migrations...'
python manage.py wait_for_db --settings=mesada-manager.settings
python manage.py migrate --settings=mesada-manager.settings

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=mesada-manager.settings mesada-manager.wsgi:application --bind 0.0.0.0:$PORT