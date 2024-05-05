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

# Wait for server to start
echo "Waiting for server to start"
max_attempts=10
for i in $(seq 1 $max_attempts); do
  if curl --silent --fail http://localhost:8000/api/health > /dev/null; then
    echo "Server started"
    break
  elif [ $i -eq $max_attempts ]; then
    echo "Failed to connect to server after $max_attempts attempts, exiting"
    exit 1
  else
    sleep 1
  fi
done

poetry run python3 integration-tests/response-check.py
kill $SERVER_PID
docker-compose -f infra/docker-compose.yml down