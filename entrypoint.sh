#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "postgres started"
fi

python manage.py collectstatic --no-input --clear
python manage.py migrate
python manage.py loaddata fixtures.json

exec "$@"
