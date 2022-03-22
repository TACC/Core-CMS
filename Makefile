DOCKERHUB_REPO := taccwma/$(shell cat ./docker_repo.var)
PROJECT_NAME := $(shell cat ./docker_repo.var)
DOCKER_TAG ?= $(shell git rev-parse --short HEAD)
BUILD_ID := $(shell git describe --always)
DOCKER_IMAGE := $(DOCKERHUB_REPO):$(DOCKER_TAG)
DOCKER_IMAGE_LATEST := $(DOCKERHUB_REPO):latest

.PHONY: build
build:
	docker-compose -f ./docker-compose.yml build

.PHONY: build-full
build-full:
	docker build -t $(DOCKER_IMAGE) --build-arg PROJECT_NAME=$(PROJECT_NAME) \
		--build-arg BUILD_ID=$(BUILD_ID) --target production -f ./Dockerfile .

.PHONY: publish
publish:
	docker push $(DOCKER_IMAGE)

.PHONY: publish-latest
publish-latest:
	docker tag $(DOCKER_IMAGE) $(DOCKER_IMAGE_LATEST)
	docker push $(DOCKER_IMAGE_LATEST)

.PHONY: start
start:
	docker-compose -f docker-compose.yml up

.PHONY: stop
stop:
	docker-compose -f docker-compose.yml down

.PHONY: stop-verbose
stop-v:
	docker-compose -f docker-compose.yml down -v
