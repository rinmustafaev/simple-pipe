FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PATH="${PATH}:/root/.local/bin"

RUN  apt-get update && apt-get install -y netcat curl && \
    curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.8.2 python - && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app/

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

ENTRYPOINT [ "/app/infra/entrypoint.sh" ]
