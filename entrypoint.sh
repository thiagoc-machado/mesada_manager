#!/bin/sh

echo 'Running collecstatic...'
python manage.py collectstatic --no-input --settings=mesada_manager.settings

echo 'Applying migrations...'
python manage.py wait_for_db --settings=mesada_manager.settings
python manage.py migrate --settings=mesada_manager.settings

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=mesada_manager.settings mesada_manager.wsgi:application --bind 0.0.0.0:$PORT