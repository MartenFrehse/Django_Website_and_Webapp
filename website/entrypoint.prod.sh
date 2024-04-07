#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"

    # Make Migration 
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createcachetable

    # Create Super User 
    if [ "$DJANGO_SUPERUSER_USERNAME" ]
    then
        python manage.py createsuperuser \
            --noinput \
            --username $DJANGO_SUPERUSER_USERNAME \
            --email $DJANGO_SUPERUSER_EMAIL
    fi

fi

exec "$@"