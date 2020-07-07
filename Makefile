define step
	@echo -e "\x1b[34;01m>>> $(1)\x1b[0m"
endef


update-requirements:
	$(call step,Upgrading local packages in poetry.lock...)
	poetry update

install-requirements:
	# Install requirements for a local development environment
	$(call step,Installing poetry...)
	pip install poetry
	$(call step,Installing packages from poetry.lock...)
	poetry install

generate-requirements:
	# Export the poetry.lock file in a requirements.txt file format
	$(call step,Exporting packages from poetry.lock to requirements.txt...)
	poetry export -o requirements.txt -f requirements.txt --without-hashes

setup-frontend:
	bower install --allow-root

test:
	$(call step,Running all tests under tests/...)
	pytest
