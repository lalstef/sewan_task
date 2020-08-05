#!/bin/sh

gunicorn --chdir app __init__:app --workers 2 --threads 2 --bind 0.0.0.0:8003