## Continuous Integration

The continuous integration for this project is implemented using GitHub Actions. The configuration file for the CI workflow can be found at `.github/workflows/ci.yaml`.

## Running Locally

To run the project locally, follow these steps:
1. Install poetry  curl -sSL https://install.python-poetry.org | python3 -
2. Install the dependencies using Poetry: `poetry install`
3. Start the development server: `poetry run python manage.py runserver`
4. Open your browser and navigate to `http://localhost:8000` (or the specified port)

## Running Tests Locally or via Docker Compose

To run tests locally, you can use the script `run_tests_locally.sh`. If you need a fully automated way  in docker environment, you can use `run_tests_locally_docker.sh`

## Project structure
The `infra` folder contains a Dockerfile with an entrypoint to start the server, a docker-compose file, and an init script to populate some test data for integration tests.

In the `integration-tests` folder, you can find a simple test that checks the response from the web server.
