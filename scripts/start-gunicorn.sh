#!/bin/bash

# Start Gunicorn for the Python application
gunicorn app:my_web_app --bind localhost:8080 --worker-class aiohttp.GunicornWebWorker &
nginx -g 'daemon off;'