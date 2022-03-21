FROM python:3.8.12-buster as python-base

LABEL maintainer="TACC-ACI-WMA <wma_prtl@tacc.utexas.edu>"

ARG DEBIAN_FRONTEND=noninteractive
ARG PROJECT_NAME
ARG BUILD_ID

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    build-essential python3-dev \
    libldap2-dev libsasl2-dev ldap-utils tox \
    lcov valgrind vim \
    && pip3 install uwsgi

# install node 16.x
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs

# load files
RUN mkdir /code
COPY . /code
WORKDIR /code

# install python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# build assets
RUN npm ci
RUN npm run build --project=$PROJECT_NAME --build-id=$BUILD_ID
