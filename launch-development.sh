#!/bin/bash

ENV_FILE="$HOME/config/rdmo_development_env_file"

docker-compose -f docker-compose.yml -f docker-compose.development.yml --env-file "$ENV_FILE" down

echo
echo "All going well rdmo should be available in http://localhost:1239"
echo
echo "The first time you might need to do in the Django Docker container:"
echo "python3 manage.py setup_groups"
echo "python3 manage.py createsuperuser"

docker-compose -f docker-compose.yml -f docker-compose.development.yml --env-file "$ENV_FILE" up --build

