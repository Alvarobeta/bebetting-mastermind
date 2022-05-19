FROM python:3.9-alpine AS base

ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers build-base 
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add bash

FROM base AS local-server

WORKDIR "/code/"

RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system --dev

COPY . /code/

COPY ./requirements.txt /code/requirements.txt
COPY ./requirements-dev.txt /code/requirements-dev.txt
RUN pip install -r /code/requirements-dev.txt

RUN apk del .tmp-build-deps

WORKDIR "/code"

EXPOSE 8888

# RUN adduser -D postgres
# USER postgres

# CMD ["uvicorn", "app.mastermind.infrastructure.FastAPI.main:app", "--host", "0.0.0.0",  "--port", "8000", "--reload"]
# bash -c "alembic upgrade head && uvicorn app.mastermind.infrastructure.FastAPI.main:app --host 0.0.0.0 --port 8888 --reload"