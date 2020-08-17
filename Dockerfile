FROM python:3.6-buster

ENV PYTHONUNBUFFERED 1

# install undescribed requirements
RUN apt-get update && \
    apt-get install -y build-essential python3-dev \
    libldap2-dev libsasl2-dev ldap-utils tox \
    lcov valgrind vim && pip3 install uwsgi

# install node 12.x
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs

# prepare code
RUN mkdir /code
COPY . /code
WORKDIR /code

# install python packages
RUN pip3 install -r requirements.txt

# build assets
RUN npm ci && npm run build
