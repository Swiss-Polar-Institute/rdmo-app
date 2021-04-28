#!/bin/bash

# If any command fails: aborts
set -e
set -o pipefail

/code/wait-for-mysql.sh

python3 manage.py migrate
gunicorn --bind 0.0.0.0:8080 config.wsgi:application
