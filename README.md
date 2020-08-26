# TACC CMS

## Docker Setup

A TACC CMS can be run using Docker and Docker Compose both locally or in production.

## Configuration

### To Support Indepenent Isolated Instance

Skip configuration; you may use the default configuration.

### To Support Instance Alongside Other CMS Project Instances

1. Copy `docker-compose.yml` as new `docker-compose.custom.yml` file, and in the new file:
    - Replace any `taccsite_` string partial with a unique identifier.
    - Replace the first number in `ports` value with a unique port.
2. Copy `taccsite_cms/default_secrets.py` as new `taccsite_cms/secrets.py` file, and in the new file:
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

[django-migrate]: https://docs.djangoproject.com/en/3.0/topics/migrations/

[django-cms-migrate]: http://docs.django-cms.org/en/latest/how_to/install.html#database-tables
[django-cms-su]: http://docs.django-cms.org/en/latest/how_to/install.html#admin-user


Log in with the user that was created via the `createsuperuser` step.

> __Notice__: To log in with a TACC account using LDAP, create the account using the TACC username, then assign staff and/or superuser privileges. The assigned password can be any password and does __not__ need to be sent to the user. The CMS will __not__ attempt to validate with the assigned password unless LDAP authentication fails. __For production, create a strong password.__

> __Warning__: The CMS install will be fresh i.e. the CMS will __not__ be populated with production content.

## Building Static Resources

Certain static resources are built

- __from__ `/taccsite_cms/static/site_cms` source code entry point files,

and populated

- __to__ `/taccsite_cms/static/build` in a matching folder as build artifacts.

### Resources

- `…/styles` (CSS stylesheets)

### Setup

1. [Install][npm-cli-install] the dependencies:

    ```bash
    npm install
    ```

2. Build the static dependencies:

    ```bash
    npm run build
    ```

3. (Optional) [Watch][npm-pkg-watch] files, and re-build when source files change:

    ```bash
    npm run watch
    ```


[npm-cli-install]: https://docs.npmjs.com/cli/install
[npm-pkg-watch]: https://www.npmjs.com/package/npm-watch


### Usage

1. Make changes to source files.
2. Compile changes to source via:
    - (manually, for any ready changes) `npm run build`
    - (automatically, on source change) `npm run watch`
3. Confirm that the build output has changed.

> __Remember__:
> Templates can load two kinds of static files.
>
> - Those that _need the build step_ __must__ be loaded from `…/build`.
> - Those that _need __no__ build step_ __must__ be loaded from `…/site_cms`.

## Linting and Formatting Conventions

Markdown docments can be linted via [markdownlint][mdlint]. Known editor plugins:

- [Atom: linter-node-markdownlint](https://atom.io/packages/linter-node-markdownlint)
- [VS Code: vscode-markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)

Client-side and server-side code may be formatted via [EditorConfig][editorconfig]. Known editor plugins:

- [Atom: editorconfig](https://atom.io/packages/editorconfig)
- [VS Code: EditorConfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)


[mdlint]: https://github.com/DavidAnson/markdownlint
[editorconfig]: https://editorconfig.org/


## Reference

- [DjangoCMS Stand Alone Site](https://confluence.tacc.utexas.edu/x/G4G-Ag)
