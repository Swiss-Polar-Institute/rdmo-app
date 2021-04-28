#!/bin/bash

ENV_FILE="$HOME/config/rdmo_production_env_file"

docker-compose -f docker-compose.yml --env-file "$ENV_FILE" down

docker-compose -f docker-compose.yml --env-file "$ENV_FILE" up --build

