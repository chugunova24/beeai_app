#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
poetry run python manage.py migrate --noinput || exit 1

# Start server
echo "Starting server"
poetry run python manage.py runserver ${DJANGO_HOST}:${DJANGO_PORT}