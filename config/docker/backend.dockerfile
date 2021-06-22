FROM nikolaik/python-nodejs:python3.8-nodejs14

# Unbuffer Python logs
ENV PYTHONUNBUFFERED=1 \
  POETRY_VERSION=1.1.6


RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

RUN npm install --global bower

RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

RUN bower install --allow-root
