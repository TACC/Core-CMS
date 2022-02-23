FROM python:3.8.12-buster as python-base

LABEL maintainer="TACC-ACI-WMA <wma_prtl@tacc.utexas.edu>"

ARG DEBIAN_FRONTEND=noninteractive
ARG PROJECT_NAME

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    build-essential python3-dev \
    libldap2-dev libsasl2-dev ldap-utils tox \
    lcov valgrind vim \
    && pip3 install uwsgi

# install node 12.x (only for taccsite_custom)
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs

# load files
RUN mkdir /code
COPY . /code
WORKDIR /code

# install python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# build assets
RUN cd taccsite_custom && npm ci && npm run build --project=$PROJECT_NAME\
    # copy base core cms stylesheets to legacy path
    && mkdir -p ../taccsite_cms/static/site_cms/css/build\
    && cp -r core-cms/static/core-cms/css/build/*\
        ../taccsite_cms/static/site_cms/css/build
