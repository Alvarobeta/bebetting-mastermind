FROM python:3.9-alpine AS base

ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers build-base

FROM base AS local-server

WORKDIR "/app/app"

COPY ./requirements.txt /app/app/requirements.txt
COPY ./requirements-dev.txt /app/app/requirements-dev.txt
RUN pip install -r /app/app/requirements-dev.txt

RUN apk del .tmp-build-deps

WORKDIR "/app"

RUN adduser -D user
USER user

CMD ["uvicorn", "app.app_name.infrastructure.FastAPI.main:app", "--host", "0.0.0.0",  "--port", "8888", "--no-server-header", "--reload"]
