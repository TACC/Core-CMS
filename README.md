# TACC CMS

## Docker Setup

TACC CMS can be run using Docker and Docker-Compose both locally or in production.

## Configuration

Create a secrets file at taccsite_cms/secrets.py

Set the secret settings like below:

```python
_SECRET_KEY = 'Change Me'
_DEBUG = True
_ALLOWED_HOSTS = ['*']
_SITE_ID = 1
_CMS_TEMPLATES =  (
    ## Customize this
    ('base.html', 'Base'),
    ('cms_menu.html', 'CMS Menu'),
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right')
)

_DATABASE_ENGINE = 'django.db.backends.postgresql'
_DATABASE_NAME = 'taccsite'
_DATABASE_USERNAME = 'taccsite'
_DATABASE_PASSWORD = 'taccsite'
_DATABASE_HOST = 'taccsite_postgres'
_DATABASE_PORT = 5432
```

## Running the CMS with Docker

Use [Docker Compose](https://docs.docker.com/compose/)!

The docker-compose.yml file included in this repo is setup for running the composition locally.

First, build the CMS docker image:

```bash
docker-compose build
```
Create and run a docker container from the image.

```bash
docker-compose up
```
Exec into the container and run migrations then create a superuser account.

```bash
docker exec -it taccsite_cms /bin/bash
python3 manage.py migrate
```

Create a superuser account, TACC username is required for LDAP, but any password can be used, the pw will be validated against LDAP first, if that fails, it will be validated against the assigned password below.

```bash
python3 manage.py createsuperuser
```
Create additional accounts as needed

Access CMS admin site at at http://localhost:8000/admin

To log in with a TACC account using LDAP, create the account using the TACC username and assign staff and/or superuser privileges. The assigned password can be any password and doesn't need to be sent to the user. The CMS will not attempt to validate with the assigned password unless LDAP auth fails, creating a strong password is recommended for production.

## Building Static Resources

These static resources are built from source files:

- CSS Stylesheets

### Setup

1. Install the dependencies:

    ```bash
    npm install
    ```

2. Build the static dependencies:

    ```bash
    npm run build
    ```

3. (Optional) If you want the build to occur when you change source files, then run:

    ```bash
    npm run watch
    ```

### Usage

1. Make changes to source files in `/src`.
2. Compile changes to source via:
    - (manually, for any ready changes) `npm run build`
    - (automatically, on source change) `npm run watch`
3. Notice that build output is in `/build`.
    - Docker loads that output as if it were in `/taccsite_cms/static/site_cms`.
