# PYTHON BASE IMAGE
FROM python:3.8-buster as python-base
LABEL maintainer="TACC-ACI-WMA <wma_prtl@tacc.utexas.edu>"
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    build-essential python3-dev \
    libldap2-dev libsasl2-dev ldap-utils tox \
    lcov valgrind vim \
    && pip3 install uwsgi

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:$PATH"

# https://python-poetry.org/docs/configuration/#using-environment-variables
ENV POETRY_VERSION=1.4.0 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

RUN pip3 install --upgrade pip setuptools wheel
# Install Poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN mkdir /code
# copy project requirement files here to ensure they will be cached.
COPY pyproject.toml poetry.lock /code/
WORKDIR /code
# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --no-dev



# POETRY DEPENDENCIES
FROM python-base as development
COPY . /code/
# quicker install because poetry runtime deps are already installed
RUN poetry install



# NODE DEPENDENCIES & BUILD & OUTPUT
FROM node:18 as node_build

# Install dependencies
COPY package.json package-lock.json /code/
WORKDIR /code
RUN npm ci

# Build assets
COPY . /code/
ARG PROJECT_NAME
ARG BUILD_ID
RUN npm run build --project=$PROJECT_NAME --build-id=$BUILD_ID



# FINAL LAYER
FROM python-base as production

# Support CMS logs
RUN mkdir -p /var/log/cms

# Populate with code from Node layer
# - (new) /node_modules
# - (unchanged) /package.json and /package-lock.json
# - (populated) /css/build and /taccsite_ui/dist
COPY --from=node_build /code/ /code
