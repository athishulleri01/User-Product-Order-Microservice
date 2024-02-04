#!/bin/bash

# Start the Django application
gunicorn -c email_service/gunicorn_config.py email_service.wsgi:application
