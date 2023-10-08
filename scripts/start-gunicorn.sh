#!/bin/bash

# Start Gunicorn for the Python application
gunicorn app:my_web_app --bind localhost:5000 --worker-class aiohttp.GunicornWebWorker &
nginx -g 'daemon off;'