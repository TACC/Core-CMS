FROM python:3.6-buster
ENV PYTHONUNBUFFERED 1
# Install OS Packages
RUN apt-get update && \
    apt-get install -y build-essential python3-dev \
    libldap2-dev libsasl2-dev ldap-utils tox \
    lcov valgrind vim && \
    pip3 install uwsgi && \
    # Node
    # GL-30: Also, run `npm ci` and `npm run build`
    curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get install -y nodejs
# Prepare Directories
RUN mkdir /code
COPY . /code
WORKDIR /code
# Install App Requirements
RUN pip3 install -r requirements.txt
