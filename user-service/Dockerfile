FROM python:3.10

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.1.11

RUN apt-get update && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /user-service

COPY pyproject.toml poetry.lock /user-service/

RUN poetry install --no-root --no-dev

COPY . /user-service

EXPOSE 8000