#!/bin/bash

# Apply database migrations
python manage.py migrate --noinput

# Read superuser credentials from .env file
source .env

# Create superuser
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')" | python manage.py shell


python manage.py collectstatic --noinput



