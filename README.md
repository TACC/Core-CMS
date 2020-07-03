# TACC CMS

## Docker Setup

TACC CMS can be run using Docker and Docker-Compose both locally or in production.

## Configuration

### To Support Indepenent Isolated Instance

Skip configuration; you may use the default configuration.

### To Support Instance Alongside Other CMS Project Instances

1. Create new `taccsite_cms/secrets.py`:
    1. In [UT Stache](https://stache.utexas.edu), open the __"SAD CMS 0N: […]"__ entry for this project.
    2. Copy the value of the __"Secret"__ field.
    3. Create `taccsite_cms/secrets.py` with that copied value.
2. Edit `taccsite_cms/settings.py` to load new `taccsite_cms/secrets.py`:
    - Comment out `import taccsite_cms.secrets_example …` line.
    - Uncomment `import taccsite_cms.secrets …` line.
3. Edit `docker-compose.yml` to use "Database Settings" from new secrets.

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

Certain static resources are built

- __from__ `/taccsite_cms/static/site_cms` source code entry point files, and populated
- __to__ `/taccsite_cms/static/build` in a matching folder as build artifacts.

Resources:

- `…/styles` (CSS stylesheets)

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

1. Make changes to source files.
2. Compile changes to source via:
    - (manually, for any ready changes) `npm run build`
    - (automatically, on source change) `npm run watch`
3. Confirm that the build output has changed.

Remember:

- Templates must load files, that were built, from `…/build`
- Templates must load files, that need __no__ build step, from `…/site_cms`
