FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.1.11

WORKDIR /user_service

RUN apt-get update -y && \
    apt-get install -y python3-dev gcc musl-dev curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock* /user_service/

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

# Copy project files
COPY . /user_service

EXPOSE 8000