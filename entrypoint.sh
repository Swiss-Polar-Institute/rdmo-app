#!/bin/bash

# If any command fails: aborts
set -e
set -o pipefail

/code/wait-for-mysql.sh

mkdir -p /code/vendor

python3 manage.py migrate
python3 manage.py collectstatic --no-input --clear

gunicorn config.wsgi:application \
	--bind 0.0.0.0:8080 \
	--workers 3\
	--log-file=- \
	--error-logfile=- \
	--access-logfile=- \
	--capture-output \
	"$@"
