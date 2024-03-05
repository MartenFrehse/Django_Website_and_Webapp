#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi
# commentout when the migration should not run on every restart or so 
# python manage.py flush --no-input
# python manage.py migrate

# Run it manuelly when needed after container spin up:
# $ docker-compose exec web python manage.py flush --no-input
# $ docker-compose exec web python manage.py migrate
exec "$@"