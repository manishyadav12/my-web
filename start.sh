#!/bin/bash

# Alternative startup script for different deployment scenarios

PORT=${PORT:-8000}

echo "Starting portfolio website on port $PORT..."

# Try gunicorn with config file first
if [ -f "gunicorn.conf.py" ]; then
    echo "Using gunicorn.conf.py configuration"
    exec gunicorn app:app -c gunicorn.conf.py
else
    # Fallback to basic gunicorn command
    echo "Using basic gunicorn configuration"
    exec gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 30
fi