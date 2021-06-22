docker-command:
	docker-compose -f ./config/compose/docker-compose.yml $(cmd)

docker-run:
	$(MAKE) docker-command cmd="run --rm backend $(cmd)"

poetry-install:
	$(MAKE) docker-run cmd="poetry install"

# If the first argument is "poetry-add"...
ifeq (poetry-add,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "poetry-add"
  POETRY_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(POETRY_ARGS):;@:)
endif

poetry-add:
	$(MAKE) docker-run cmd="poetry add $(POETRY_ARGS)"

poetry-update:
	$(MAKE) docker-run cmd="poetry update"

# If the first argument is "bower-install"...
ifeq (bower-install,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "bower-install"
  BOWER_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(BOWER_ARGS):;@:)
endif

bower-install:
	$(MAKE) docker-run cmd="bower install $(BOWER_ARGS)"
