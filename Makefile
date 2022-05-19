# 🟢🔴 Tests
.PHONY: tests
tests:
	make functional-tests
	make unit-tests

.PHONY: functional-tests
functional-tests:
	docker-compose run local-server pytest -c app/functional.pytest.ini -s -vv || true

.PHONY: unit-tests
unit-tests:
	docker-compose run local-server pytest -c app/unit.pytest.ini -s -vv || true

# 🧑‍🔧 Developer tools
.PHONY: format-imports
format-imports:
	docker-compose run local-server /bin/sh -e -c '\
		set -e; \
		set -x; \
		# Sort imports one per line, so autoflake can remove unused imports \
		isort --force-single-line-imports app; \
	'
	make format

.PHONY: format
format:
	docker-compose run local-server /bin/sh -e -c '\
		set -e; \
		set -x; \
		autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place app --exclude=__init__.py; \
		black app; \
		isort app; \
	'

.PHONY: lint
lint:
	docker-compose run local-server /bin/sh -e -c '\
		mypy app || true; \
		black app --check || true; \
		isort --check-only app || true; \
		flake8 app --config=app/.flake8; \
	'

# 🐳 Docker Compose
.PHONY: up
up:
	docker-compose up

.PHONY: rebuild
rebuild:
	docker-compose build --pull --force-rm --no-cache
