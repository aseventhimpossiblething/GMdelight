#!/bin/bash
sleep 5
cd /GMDelight/GMDelight
#gunicorn -c appconfig.py bdx-api-link:app
gunicorn -c appconfig.py bdx-api-link:app
