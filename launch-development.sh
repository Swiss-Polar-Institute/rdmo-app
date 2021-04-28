#!/bin/bash

ENV_FILE="$HOME/config/rdmo_dev_env_file"

docker-compose -f docker-compose.yml --env-file "$ENV_FILE" down

echo
echo "All going well rdmo should be available in http://localhost:1239"
echo

docker-compose -f docker-compose.yml --env-file "$ENV_FILE" up --build

