# Getting started

## Prerequisites
- [Docker](https://docs.docker.com/docker-for-mac/install/) 
- [Docker Compose](https://docs.docker.com/compose/) 
- make command

## How to run the app

To make the first migration necessary for the app to work execute: 

```bash
docker-compose run web alembic revision --autogenerate -m "First migration"

```

and then:

```bash
make up
```

This command will expose the app under `http://localhost:8888/`

In the URL `http://localhost:8888/docs` you have a Swagger UI with the API documentation. There you'll have a link with the OpenAPI in json format.

In the URL `http://localhost:8888/redoc` you have a [ReDoc](https://github.com/Redocly/redoc) living.

And of course, under `http://localhost:8888/` it's the required endpoint 😀.

You can find the postgres pagadmin at `http://localhost:5050/`. (user=pgadmin4@pgadmin.org, password=admin)

You will probably need to create a .env on the root with the following info:

DATABASE_URL=postgresql+psycopg2://postgres:postgres@db:5432

DB_USER=postgres

DB_PASSWORD=postgres

DB_NAME=test_db

PGADMIN_EMAIL=pgadmin4@pgadmin.org

PGADMIN_PASSWORD=admin


## How run the tests

```bash
make tests
```

## How to run the configured linters
```bash
make lint
```

## How to autoformat the code
```bash
make format
```


## Improvements and future work
- Randomize feedback, I didn't do it because I don't know how to test random answers.
- Testing should be against a different db than the production one
- Use mocks on testing to avoid to create a game every time we execute the tests. There are ways to do it but I'm not sure how to implement it, sorry.
- Lost game test, I should mock a 7 tries game and then execute with a wrong guess, but since I don't know how to mock it's not covered
- Detect duplicated guessings
- Think and handle the possible unexpected cases that I missed
