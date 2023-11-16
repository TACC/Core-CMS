DOCKERHUB_REPO := taccwma/$(shell cat ./docker_repo.var)
DOCKER_TAG ?= $(shell git rev-parse --short HEAD)
DOCKER_IMAGE := $(DOCKERHUB_REPO):$(DOCKER_TAG)
DOCKER_IMAGE_LATEST := $(DOCKERHUB_REPO):latest

PROJECT_NAME := $(shell cat ./project_name.var)
BUILD_ID := $(shell git describe --always)

.PHONY: build
build:
	docker-compose -f ./docker-compose.yml build

.PHONY: build-full
build-full:
	docker build -t $(DOCKER_IMAGE) \
		--target production \
		--build-arg PROJECT_NAME="$(PROJECT_NAME)" \
		--build-arg BUILD_ID="$(BUILD_ID)" \
		-f ./Dockerfile .

.PHONY: example
example:
	docker-compose -f ./docker-compose.example.yml up

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
