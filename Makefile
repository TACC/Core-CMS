DOCKERHUB_REPO := taccwma/$(shell cat ./docker_repo.var)
PROJECT_NAME := $(shell cat ./docker_repo.var)
DOCKER_TAG ?= $(shell git rev-parse --short HEAD)
DOCKER_IMAGE := $(DOCKERHUB_REPO):$(DOCKER_TAG)
DOCKER_IMAGE_LATEST := $(DOCKERHUB_REPO):latest
DOCKER_IMAGE_LOCAL := $(DOCKERHUB_REPO):local

.PHONY: build
build:
	docker build --tag $(DOCKER_IMAGE) --build-arg PROJECT_NAME=$(PROJECT_NAME) .
	docker tag $(DOCKER_IMAGE) $(DOCKER_IMAGE_LATEST)

.PHONY: publish
publish:
	docker push $(DOCKER_IMAGE)

.PHONY: publish-latest
publish-latest:
	docker push $(DOCKER_IMAGE_LATEST)

.PHONY: start
start:
	docker-compose -f docker-compose.yml up

requirements-frozen.txt: build
	docker run --rm $(DOCKER_IMAGE) pip freeze > $@
