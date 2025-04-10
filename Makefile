DOCKERHUB_REPO := taccwma/$(shell cat ./docker_repo.var)
DOCKER_TAG ?= $(shell git rev-parse --short HEAD)
DOCKER_IMAGE := $(DOCKERHUB_REPO):$(DOCKER_TAG)
DOCKER_IMAGE_LATEST := $(DOCKERHUB_REPO):latest
# WARNING: Using `docker-compose` is deprecated
DOCKER_COMPOSE_CMD := $(shell if command -v docker-compose > /dev/null; then echo "docker-compose"; else echo "docker compose"; fi)

# NOTE: The `DOCKER_IMAGE_BRANCH` tag is the git tag for the commit if it exists, else the branch on which the commit exists.
# NOTE: Special characters in `DOCKER_IMAGE_BRANCH` are replaced with dashes.
DOCKER_IMAGE_BRANCH := $(DOCKERHUB_REPO):$(shell git describe --exact-match --tags 2> /dev/null || git symbolic-ref --short HEAD | sed 's/[^[:alnum:]\.\_\-]/-/g')

PROJECT_NAME := $(shell cat ./project_name.var)
NEEDS_DEMO := $(shell cat ./needs_demo.var)
BUILD_ID := $(shell git describe --always)

.PHONY: build
build:
	$(DOCKER_COMPOSE_CMD) -f ./docker-compose.yml build

.PHONY: build-full
build-full:
	docker build -t $(DOCKER_IMAGE) \
		--target production \
		--build-arg PROJECT_NAME="$(PROJECT_NAME)" \
		--build-arg BUILD_ID="$(BUILD_ID)" \
		--build-arg NEEDS_DEMO="$(NEEDS_DEMO)" \
		-f ./Dockerfile .

	docker tag $(DOCKER_IMAGE) $(DOCKER_IMAGE_BRANCH)

.PHONY: example
example:
	$(DOCKER_COMPOSE_CMD) -f ./docker-compose.example.yml up

.PHONY: publish
publish:
	docker push $(DOCKER_IMAGE)
	docker push $(DOCKER_IMAGE_BRANCH)

.PHONY: publish-latest
publish-latest:
	docker tag $(DOCKER_IMAGE) $(DOCKER_IMAGE_LATEST)
	docker push $(DOCKER_IMAGE_LATEST)

.PHONY: start
start:
	$(DOCKER_COMPOSE_CMD) -f docker-compose.dev.yml up

.PHONY: stop
stop:
	$(DOCKER_COMPOSE_CMD) -f docker-compose.dev.yml down

.PHONY: stop-full
stop-v:
	$(DOCKER_COMPOSE_CMD) -f docker-compose.dev.yml down -v
