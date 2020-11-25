# TACC CMS

## Docker Setup

A TACC CMS can be run using Docker and Docker Compose both locally or in production.

## Configuration

### Custom Configuration

Configuration is stored in `default_secrets.py` and may be customized by creating a `secrets.py`.

1. Copy `taccsite_cms/default_secrets.py` as new `taccsite_cms/secrets.py` file.
2. Update the `secrets.py` file.

### Custom Resources per CMS Project

For all CMS projects (besides the standalone Core), the submodule for project-specific resources __must__ be available.

1. `git submodule init` (only necessary once)
    - Add `cms-site-resources` repo as `taccsite_custom/`.
2. `git submodule update` (after `git fetch` / `pull`)
    - Get latest desired submodule commit (thus directory content).
3. Create and update `secrets.py`. See [Custom Configuration](#Optional%20Custom%20Configuration).
    - Setup existing CMS project by manually appending secrets from `taccsite_custom/__PROJECT__/secrets.py`.
    - For new CMS projects, add custom and unique resources and configuration to `taccsite_custom/__PROJECT__/`.
4. Create a `.env` at the root of the project, with the content `CUSTOM_ASSET_DIR=name-of-project` where `name-of-project` matches a directory from `/taccsite_custom`.

### (Optional) Multiple CMS Projects on One Machine

To support multiple instances of the CMS on one machine (i.e. local development), configure unique identification for the database of each.

1. Copy `docker-compose.yml` as new `docker-compose.custom.yml` file, and in the new file:
    - Replace any `taccsite_` string partial with a unique identifier.
    - Replace the first number in `ports` value with a unique port.
2. Create and update `secrets.py`. See [Custom Configuration](Optional%20Custom%20Configuration).
    - Change `_DATABASES`:`default`:`HOST` to equal `docker-compose.custom.yml`'s `postgres`:`hostname`.
3. Run any `docker-compose` with file argument, e.g.:

    ```bash
    docker-compose -f docker-compose.custom.yml …
    ```

## Run the CMS (via Docker)

> __Notice__: The `docker-compose.yml` file included in this repo is set up for running the instance locally.

### Prerequisites

- Have [Docker Compose](https://docs.docker.com/compose/) on the host system.

### Steps

1. [Build][docker-compose-build] the CMS and database images:

    ```bash
    docker-compose build
    ```

2. [Create and run][docker-compose-up] the CMS and database containers:

    ```bash
    docker-compose up
    ```

3. [Start a bash session][docker-exec-bash] into the CMS container:

    > __Notice__: If you are using a `docker-compose.custom.yml`, then replace this command's `taccsite_cms` with that file's `cms`: `hostname`.

    ```bash
    docker exec -it taccsite_cms /bin/bash
    ```

4. [Run migrations][django-cms-migrate] for Django CMS:

    ```bash
    python manage.py migrate
    ```

    _This is like a Django CMS wrapper around [Django migrations][django-cms-migrate]._

5. [Create a superuser][django-cms-su] for Django CMS:

    > __Notice__: A TACC username is required for LDAP access, but any password can be used. The password will be validated against LDAP first, if that fails, it will be validated against the password assigned during the following command's interface. __For production, create a strong password.__

    ```bash
    python manage.py createsuperuser
    ```

    _You may create additional accounts as needed._

The CMS admin site should now be accessible at http://localhost:8000/admin (or at the port defined in a `docker-compose.custom.yml`).


[docker-exec-bash]: https://docs.docker.com/engine/reference/commandline/exec/#run-docker-exec-on-a-running-container

[docker-compose-up]: https://docs.docker.com/compose/reference/up/
[docker-compose-build]: https://docs.docker.com/compose/reference/build/

[django-migrate]: https://docs.djangoproject.com/en/2.2/topics/migrations/

[django-collectstatic]: https://docs.djangoproject.com/en/2.2/ref/contrib/staticfiles/#django-admin-collectstatic

[django-cms-migrate]: http://docs.django-cms.org/en/latest/how_to/install.html#database-tables
[django-cms-su]: http://docs.django-cms.org/en/latest/how_to/install.html#admin-user


Log in with the user that was created via the `createsuperuser` step.

> __Notice__: To log in with a TACC account using LDAP, create the account using the TACC username, then assign staff and/or superuser privileges. The assigned password can be any password and does __not__ need to be sent to the user. The CMS will __not__ attempt to validate with the assigned password unless LDAP authentication fails. __For production, create a strong password.__

> __Warning__: The CMS install will be fresh i.e. the CMS will __not__ be populated with production content.

## Changing Static Files

Whenever static files are changed, the CMS may need to be manually told to serve them (if not [automatically performed, or if cached](https://stackoverflow.com/a/59340216/11817077)).

1. [Start a bash session][docker-exec-bash] into the CMS container:

    > __Notice__: If you are using a `docker-compose.custom.yml`, then replace this command's `taccsite_cms` with that file's `cms`: `hostname`.

    ```bash
    docker exec -it taccsite_cms /bin/bash
    ```

2. [Collect static files][django-collectstatic] for Django:

    ```bash
    python manage.py collectstatic
    ```

## Building Static Files

Certain static files are built __from__ source files __in__ `src` directories __to__ compiled files __in__ `build` directories.

> __Notice__: We configured Django to ignore `src` directories during [`collectstatic`][django-collectstatic], so templates can not directly load source files.

### Quick Start

1. Make changes to relevant `src` files.
2. Build static files from source files via:
    - (manually, for any ready changes) `npm run build`
    - (automatically, on source change) `npm run watch`
3. (Debug) Confirm relevant `build` output changed.
4. "Collect" static files. See [Changing Static Files](#Changing%20Static%20Files).
5. (Debug) Confirm relevant `/static/…/build` output changed.

### How to Build

The files are currently built locally and synced to the CMS Docker container. _[Issue #30](https://gitlab.tacc.utexas.edu/wma-cms/cms-site-template/issues/30) will change this process and this paragraph._

1. [Install][npm-cli-install] the dependencies:

    ```bash
    npm ci
    ```

2. Build static files:

    ```bash
    npm run build
    ```

3. (Optional) [Watch][npm-pkg-watch] files, and re-build when source files change:

    ```bash
    npm run watch
    ```

[npm-cli-install]: https://docs.npmjs.com/cli/install
[npm-pkg-watch]: https://www.npmjs.com/package/npm-watch

## Managing Custom Resources

1. Create/Edit files in a child directory of `/taccsite_custom`.
2. Follow instructions and directory structure of `example-cms`.
3. Reference other projects in `/taccsite_custom`.
4. (As necessary) Build static assets.
5. (For templates) Restart server.
6. [Commit changes.](#Commit%20Changes)
    1. In `/taccsite_custom` submodule repo, commit changes.
    2. In `cms-site-template` parent repo, add `/taccsite_custom` change.
    3. In `cms-site-template` parent repo, commit changes.

## Reference

- [Formatting & Linting](https://confluence.tacc.utexas.edu/x/HoBGCw)
- [DjangoCMS Stand Alone Site](https://confluence.tacc.utexas.edu/x/G4G-Ag)
