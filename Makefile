
define step
	@echo -e "\x1b[34;01m>>> $(1)\x1b[0m"
endef


pip-compile:
	# Update requirements/*.txt with latest packages from requirements/*.in
	$(call step,Installing/upgrading pip-tools...)
	pip install -qU pip-tools

	$(call step,Upgrading local packages...)
	pip-compile -U requirements/dev.in
	pip-compile -U requirements/heroku.in
	pip-compile -U requirements/production.in

	$(call step,Compiling test requirements...)
	pip-compile -U -o requirements/test.txt requirements/production.in requirements/test.in


install-dev-requirements:
	# Install requirements for a local development environment
	$(call step,Installing dev requirements...)
	pip install -qU pip-tools
	pip-sync requirements/*.txt

setup-frontend:
	bower install --allow-root
