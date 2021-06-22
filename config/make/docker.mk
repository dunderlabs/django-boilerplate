docker-build:
	$(MAKE) docker-command cmd="build"

docker-rebuild:
	$(MAKE) docker-command cmd="build --no-cache"

docker-pull:
	$(MAKE) docker-command cmd="pull"

docker-up:
	$(MAKE) docker-command cmd="up --remove-orphans"

docker-down:
	$(MAKE) docker-command cmd="down"

docker-image-build:
	docker build -f config/compose/docker-compose.yml -t $(image-name) .
