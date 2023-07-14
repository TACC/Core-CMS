DOCKERHUB_REPO := taccwma/$(shell cat ./docker_repo.var)
PROJECT_NAME := $(shell cat ./docker_repo.var)
DOCKER_TAG ?= $(shell git rev-parse --short HEAD)
BUILD_ID := $(shell git describe --always)
DOCKER_IMAGE := $(DOCKERHUB_REPO):$(DOCKER_TAG)
DOCKER_IMAGE_LATEST := $(DOCKERHUB_REPO):latest
DOCKER_IMAGE_LOCAL := $(DOCKERHUB_REPO):local

.PHONY: build
build:
	docker build -t $(DOCKER_IMAGE) .
	docker tag $(DOCKER_IMAGE) $(DOCKER_IMAGE_LATEST)

.PHONY: build-full
build-full:
	docker build -t $(DOCKER_IMAGE) --target production --build-arg PROJECT_NAME=$(PROJECT_NAME) --build-arg BUILD_ID=$(BUILD_ID) -f ./Dockerfile .

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
