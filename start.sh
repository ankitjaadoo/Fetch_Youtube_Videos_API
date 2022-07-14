#!/bin/bash

##starting gunicorn process

echo Starting Gunicorn workers

exec gunicorn fetch_youtube_video_API.wsgi.application --bind 0.0.0.0:8000 --workers 3