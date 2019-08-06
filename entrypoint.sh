#!/bin/sh

# Wait for postgres to start
echo "Waiting for postgres..."
while ! nc -z users-db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

# Start flask server
python manage.py run -h 0.0.0.0