#!/bin/sh

echo "Applying database migrations..."
python manage.py migrate

echo "Loading test data..."
python manage.py loaddata /test_data/test_data.json

echo "Starting the server..."
python manage.py runserver 0.0.0.0:8000