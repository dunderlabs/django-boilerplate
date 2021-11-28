# Frontend setup
FROM node:16 AS nodejs
WORKDIR /app
COPY bower.json .
RUN npm install --global bower
RUN bower install --allow-root

# Backend setup
FROM python:3.10

# Unbuffer Python logs
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.1.11

RUN pip install poetry==$POETRY_VERSION

WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml /usr/src/app/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Static files
COPY --from=nodejs /app/bower_components frontend/bower_components

CMD [ "gunicorn", "backend.wsgi", "--log-file -" ]
