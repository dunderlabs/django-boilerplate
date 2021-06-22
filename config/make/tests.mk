# If the first argument is "test"...
ifeq (test,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "test"
  POETRY_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(POETRY_ARGS):;@:)
endif

test:
	$(MAKE) docker-run cmd="pytest $(PYTEST_ARGS)"

unit-tests:
	$(MAKE) docker-run cmd="pytest tests/unit/"

interaction-tests:
	$(MAKE) docker-run cmd="pytest tests/integration/"

test-all:
	$(MAKE) docker-run cmd="pytest"
