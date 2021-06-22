define step
	@echo -e "\x1b[34;01m>>> $(1)\x1b[0m"
endef

# If the first argument is "pytest"...
ifeq (pytest,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "pytest"
  PYTEST_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(PYTEST_ARGS):;@:)
endif


update-requirements:
	$(call step,Upgrading local packages in poetry.lock...)
	poetry update

install-requirements:
	# Install requirements for a local development environment
	$(call step,Installing poetry...)
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
	$(call step,Installing packages from poetry.lock...)
	poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

generate-requirements:
	# Export the poetry.lock file in a requirements.txt file format
	$(call step,Exporting packages from poetry.lock to requirements.txt...)
	poetry export -o requirements.txt -f requirements.txt --without-hashes

setup-frontend:
	bower install --allow-root

test:
	$(call step,Running all tests under tests/...)
	pytest $(PYTEST_ARGS)
