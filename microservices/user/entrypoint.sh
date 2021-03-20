#!/bin/sh

if [ "$DATABASE" = "users" ]
then
    echo "Waiting for postgres on host $SQL_HOST port $SQL_PORT..."
  
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ "$FLASK_ENV" = "development" ]
then
  echo "Creating database..."
  python manage.py create_db
  echo "Database initialization..."
  python manage.py db init
  echo "Database migration..."
  python manage.py db migrate
fi

exec "$@"