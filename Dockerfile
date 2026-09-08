# PYTHON BASE IMAGE
FROM python:3.11-bookworm AS python-base
LABEL maintainer="TACC-ACI-WMA <wma_prtl@tacc.utexas.edu>"
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    build-essential python3-dev \
    libldap2-dev libsasl2-dev ldap-utils tox \
    lcov valgrind vim \
    && pip3 install uwsgi

ENV PYTHONUNBUFFERED 1

# https://python-poetry.org/docs/configuration/#using-environment-variables
ENV POETRY_VERSION=2.3.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

ENV PATH="$PATH:$POETRY_HOME/bin"

RUN pip3 install --upgrade pip setuptools wheel
# Install into its own venv, not via the official installer or into the project's
# environment: the installer creates its venv with symlinks=False, which on bookworm
# resolves to Debian's libpython3.11 (pulled in by python3-dev/tox/valgrind above)
# instead of this image's own build, breaking the ssl module. Installing into the same
# environment as the project (POETRY_VIRTUALENVS_CREATE=false) also risks project deps
# downgrading a shared library Poetry itself needs.
RUN python3 -m venv "$POETRY_HOME" \
    && "$POETRY_HOME/bin/pip" install poetry=="$POETRY_VERSION"
RUN mkdir /code
# copy project requirement files here to ensure they will be cached.
COPY pyproject.toml poetry.lock /code/
WORKDIR /code
# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --only main --no-root



# POETRY DEPENDENCIES
FROM python-base AS development
COPY . /code/
# quicker install because poetry runtime deps are already installed
RUN poetry install --no-root



# NODE DEPENDENCIES & BUILD & OUTPUT
FROM node:20 AS node_build

# Install dependencies
COPY package.json package-lock.json /code/
WORKDIR /code
RUN npm ci

# Build assets
COPY . /code/
ARG BUILD_ID
RUN npm run build --build-id="$BUILD_ID"



# FINAL LAYER
FROM python-base AS production

# Support CMS logs
RUN mkdir -p /var/log/cms

# Populate with code from Node layer
# - (new) /node_modules
# - (unchanged) /package.json and /package-lock.json
# - (populated) /css/build and /taccsite_ui/dist
COPY --from=node_build /code/ /code
