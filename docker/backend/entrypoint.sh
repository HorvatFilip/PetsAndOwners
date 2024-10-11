#!/bin/sh

echo "Applying database migrations..."
python manage.py migrate

echo "Creating user for admin view..."
echo "from django.contrib.auth.models import User; User.objects.create_superuser('db-admin', 'db-admin@example.com', 'pass') if len(User.objects.filter(username='db-admin'))==0 else print('db-admin already exist')" | python manage.py shell

echo "Loading test data..."
python manage.py loaddata /test_data/test_data.json

echo "Starting the server..."
python manage.py runserver 0.0.0.0:8000