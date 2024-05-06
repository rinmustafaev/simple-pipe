#!/bin/bash
#poetry run python3 manage.py makemigrations
#poetry run python3 manage.py migrate --database test
docker-compose -f infra/docker-compose.yml down -v
docker-compose -f infra/docker-compose.yml up db -d
#run unit tests
poetry run python3 manage.py test

#run custom integration tests
poetry run python3 manage.py migrate
poetry run python3 manage.py runserver  &
SERVER_PID=$!

poetry run python3 integration-tests/response-check.py
kill $SERVER_PID
docker-compose -f infra/docker-compose.yml down