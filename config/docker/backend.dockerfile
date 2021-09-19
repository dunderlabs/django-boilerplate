FROM nikolaik/python-nodejs:python3.9-nodejs16

# Unbuffer Python logs
ENV PYTHONUNBUFFERED=1 \
  POETRY_VERSION=1.1.9


RUN pip install poetry==$POETRY_VERSION

RUN npm install --global bower

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml bower.json /usr/src/app/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

RUN bower install --allow-root
