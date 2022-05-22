# Getting started

## Prerequisites
- [Docker](https://docs.docker.com/docker-for-mac/install/) 
- [Docker Compose](https://docs.docker.com/compose/) 
- make command

## How to run the app
```bash
make up
```
This command will expose the app under `http://localhost:8888/`

In the URL `http://localhost:8888/docs` you have a Swagger UI with the API documentation. There you'll have a link with the OpenAPI in json format.

In the URL `http://localhost:8888/redoc` you have a [ReDoc](https://github.com/Redocly/redoc) living.

And of course, under `http://localhost:8888/radar` it's the required endpoint 😀.

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


## Improvements
- Randomize feedback, I didn't do it because I don't know how to test random answers.
- Use mocks on testing to avoid user user with id=1. There are ways to do it but I'm not sure how to implement it, sorry.
- Detect duplicated guessings