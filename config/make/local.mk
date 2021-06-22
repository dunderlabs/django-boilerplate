# If the first argument is "test"...
ifeq (test,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "test"
  PYTEST_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(PYTEST_ARGS):;@:)
endif


local-update-requirements:
	poetry update

local-install-requirements:
	# Install requirements for a local development environment
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
	poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

local-generate-requirements:
	# Export the poetry.lock file in a requirements.txt file format
	poetry export -o requirements.txt -f requirements.txt --without-hashes

local-setup-frontend:
	bower install --allow-root

local-test:
	pytest $(PYTEST_ARGS)

local-unit-tests:
	pytest tests/unit/

local-interaction-tests:
	pytest tests/integration/

local-test-all:
	pytest
