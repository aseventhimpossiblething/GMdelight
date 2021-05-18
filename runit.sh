#!/bin/bash
sleep 5
#gunicorn -c appconfig.py bdx-api-link:app
gunicorn --bind=127.0.0.1:5000 appconfig.py bdx-api-link:app
