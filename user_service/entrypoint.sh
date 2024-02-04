#!/bin/bash

# Start the Django application
gunicorn -c user_service/gunicorn_config.py user_service.wsgi:application
