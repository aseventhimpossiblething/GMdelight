#!/bin/bash
sleep 5
cd /GMDelight/GMDelight
#gunicorn -c appconfig.py bdx-api-link:app
gunicorn --bind=127.0.0.1:5000 bdx-api-link:app
