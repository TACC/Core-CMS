# TACC CORE-CMS

## Docker Setup

The TACC CORE-CMS can be run using Docker and Docker Compose, both locally and in production.

## Configuration

### Required

1. Create a `.env` with this content\* at the root of the project:

    ```bash
    CUSTOM_ASSET_DIR=example-cms
    ```

    \* Where `example-cms` is the project to be run. _See [(Optional) Custom Resources per CMS Project](#optional-custom-resources-per-cms-project)._
1. Initialize / Update submodules.
    1. `git submodule init`\
        _(Adds `cms-site-resources` repo as submodule at `taccsite_custom/`. Only necessary once per `CORE-cms` repo clone.)_
    2. `git submodule update`\
        _(Downloads code from pinned commit of `cms-site-resources` repo to `taccsite_custom/`.)_
    3. (as necessary) Change the pinned commit of submodule.\
        _(Downloads code from different commit of `cms-site-resources` repo to `taccsite_custom/`.)_

        ```bash
        # Navigate into submodule (from root of this repo)
        cd taccsite_custom
        # Checkout different commit of submodule repo
        git checkout master_or_other_branch_or_commit
        # Update commit of submodule repo (as necessary)
        git pull # (or git fetch […], etc.)
        ```

    4. (as necessary) Save/Commit the pinned commit of submodule.\
        _(Updates the pinned commit of `cms-site-resources` repo at `taccsite_custom/`.)_

        ```bash
        # Navigate back to this repo (from root of submodule repo)
        cd ../
        # Commit this repo's pointer to a different commit of submodule repo
        git add taccsite_custom
        git commit -m "[…] Update submodule to get […]"
        ```

<!-- IDEA: For brevity, consider moving steps 3 and 4 to a different section or document -->

### For Isolated Instance Like Production

Skip further configuration; you may use the default configuration.

### For Isolated Containerized Local Development

1. Run any `docker-compose` command with `docker-compose.dev.yml` configuration, ex:

    ```bash
    docker-compose -f docker-compose.dev.yml …
    ```

### (Optional) Custom Configuration

Configuration is stored in `default_secrets.py` and may be customized by creating a `secrets.py`.

1. Copy `taccsite_cms/default_secrets.py` as new `taccsite_cms/secrets.py` file.
2. Update the `secrets.py` file.

### (Optional) Custom Resources per CMS Project

All CMS projects (besides the stand-alone CMS core), store project-specific resources in the `taccsite_custom` submodule.

1. (For Production) Copy `docker-compose.yml` as new `docker-compose.custom.yml` file, and in the new file:
    - To `cms`:`volumes` list, add an entry `/code/taccsite_custom/name-of-project/static`.*
2. Create and update `secrets.py`. _See [Custom Configuration](#optional-custom-configuration)._
    - Setup existing CMS project by manually appending secrets from `taccsite_custom/name-of-project/secrets.py`.*
    - For new CMS projects, add custom and unique resources and configuration to `taccsite_custom/name-of-project/`.*
3. Update the `.env` at the root of the project, with the content `CUSTOM_ASSET_DIR=name-of-project`.*
4. Re-build static assets, so that project-specific assets are built. _See ["Static Files"](/README.md#static-files)._

\* Where `name-of-project` matches a directory from `/taccsite_custom`.

### (Optional) Multiple CMS Projects on One Machine

To support multiple instances of the CMS on one machine (i.e. local development), configure unique identification for the database of each.

1. Copy `docker-compose.dev.yml` as new `docker-compose.custom.yml` file, and in the new file:
    - Replace any `core_cms` string partial with a unique identifier.
    - Replace the first number in `ports` value with a unique port.
2. Create and update `secrets.py`. _See [Custom Configuration](#optional-custom-configuration)._
    - Change `_DATABASES`:`default`:`HOST` to equal `docker-compose.custom.yml`'s `postgres`:`hostname`.
3. Run any `docker-compose` command with `docker-compose.custom.yml` configuration, ex:

    ```bash
    docker-compose -f docker-compose.custom.yml …
    ```

### (Optional) Migrate Website from Older Version

Some websites need static resources to supplement their migration.

1. __If__ you did not [create your project by cloning `example-cms`](#custom-resources), __then__:
    1. Copy `templates/fullwidth.html` from `taccsite_custom/example-cms/` to `taccsite_custom/name-of-project/`.
    2. Copy `static/.../css/src/migrate.v1_v2.css` from `taccsite_custom/example-cms/` to `taccsite_custom/name-of-project/`.
2. Update `taccsite_custom/name-of-project/templates/fullwidth.html` to load migration assets e.g.:
    - Change

    ```html
      <!-- To style old CMS content on new CMS -->
      <!-- <link rel="stylesheet" href="{% static 'example-cms/css/build/migrate.v1_v2.css' %}"> -->
    ```

    - To

    ```html
      <!-- To style old CMS content on new CMS -->
      <link rel="stylesheet" href="{% static 'name-of-project/css/build/migrate.v1_v2.css' %}">
    ```

## Run the CMS

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

    > __Notice__: If you are using a `docker-compose.custom.yml`, then replace this command's `core_cms` with that file's `cms`: `container_name`.

    ```bash
    docker exec -it core_cms /bin/bash
    ```

4. [Run migrations][django-cms-migrate] for Django CMS:

    ```bash
    python manage.py migrate
    ```

    _This is like a Django CMS wrapper around [Django migrations][django-migrate]._

5. [Create a superuser][django-cms-su] for Django CMS:

    > __Notice__: A TACC username is required for LDAP access, but any password can be used. The password will be validated against LDAP first, if that fails, it will be validated against the password assigned during the following command's interface. __For production, create a strong password.__

    ```bash
    python manage.py createsuperuser
    ```

    _You may create additional accounts as needed._

    The CMS admin site should now be accessible at http://localhost:8000/admin (or at the port defined in a `docker-compose.custom.yml`).

    Log in with the user that was created via the `createsuperuser` step.

    > __Notice__: To log in with a TACC account using LDAP, create the account using the TACC username, then assign staff and/or superuser privileges. The assigned password can be any password and does __not__ need to be sent to the user. The CMS will __not__ attempt to validate with the assigned password unless LDAP authentication fails. __For production, create a strong password.__

    > __Warning__: The CMS install will be fresh i.e. the CMS will __not__ be populated with production content.

6. [Collect static files][django-static] for Django:

    ```bash
    python manage.py collectstatic
    ```

    _[If `DEBUG` is set to `True`, then this is automated via `python manage.py runserver`.][django-static-serve-dev]_


[docker-exec-bash]: https://docs.docker.com/engine/reference/commandline/exec/#run-docker-exec-on-a-running-container

[docker-compose-up]: https://docs.docker.com/compose/reference/up/
[docker-compose-build]: https://docs.docker.com/compose/reference/build/

[django-migrate]: https://docs.djangoproject.com/en/3.1/topics/migrations/
[django-static]: https://docs.djangoproject.com/en/3.1/howto/static-files/
[django-static-serve-dev]: https://docs.djangoproject.com/en/3.1/howto/static-files/#serving-static-files-during-development

[django-cms-migrate]: http://docs.django-cms.org/en/latest/how_to/install.html#database-tables
[django-cms-su]: http://docs.django-cms.org/en/latest/how_to/install.html#admin-user

https://docs.djangoproject.com/en/3.1/howto/static-files/#serving-static-files-during-development


## Static Files

Certain static files are built __from__ source files __in__ `src` directories __to__ compiled files __in__ `build` directories.

> __Notice__: We configured Django to ignore `src` directories during [`collectstatic`][django-static], so templates can not directly load source files.

### Quick Start

1. (Optional) Make changes to `src` files.
2. Build static files from source files via:
    - (manually, for any ready changes) `npm run build`
    - (automatically, on source change) `npm run watch`
3. (Debug) Confirm relevant `build` output changed.
4. "Collect" static files. _See [How to Collect Static Files](#how-to-collect-static-files)._
5. (Debug) Confirm relevant `/static/…/build` output changed.

### How to Build Static Files

1. (only if using `docker-compose.yml`) [Start a bash session][docker-exec-bash] into the CMS container:

    > __Notice__: If you are using a `docker-compose.custom.yml`, then replace this command's `taccsite_cms` with that file's `cms`: `hostname`.

    ```bash
    docker exec -it core_cms /bin/bash
    ```

    _It is __not__ necessary to run the next commands in the Docker container, but it does completely __isolate development__ and __mimic production__._

2. Build static resources:

    ```bash
    npm run build
    ```

3. (Optional) [Watch][npm-pkg-watch] files, and re-build when source files change:

    ```bash
    npm run watch
    ```

> __Using `docker-compose.yml`__: Resources are automatically built once in the container. To re-build, you must run the commands in this section _in the container_.

> __Using `docker-compose.dev.yml`__: Resources are automatically built once in the container __but__ _container resources are overwritten by local resources_. To re-build, you may run the commands in this section _either_ locally _or_ in the container.


[npm-cli-install]: https://docs.npmjs.com/cli/install
[npm-pkg-watch]: https://www.npmjs.com/package/npm-watch

### How to Collect Static Files

Whenever static files are changed, the CMS may need to be manually told to serve them (if not [automatically performed, or if cached](https://stackoverflow.com/a/59340216/11817077)).

1. [Start a bash session][docker-exec-bash] into the CMS container:

    > __Notice__: If you are using a `docker-compose.custom.yml`, then replace this command's `taccsite_cms` with that file's `cms`: `hostname`.

    ```bash
    docker exec -it core_cms /bin/bash
    ```

2. [Collect static files][django-static] for Django:

    ```bash
    python manage.py collectstatic
    ```

## Custom Resources

1. Create/Edit files in a child directory of `/taccsite_custom`.
2. Follow instructions and directory structure of `example-cms`.
3. Reference other projects in `/taccsite_custom`.
4. (As necessary) Build static assets.
5. (For templates) Restart server.
6. Commit changes:
    1. In `/taccsite_custom` submodule repo, commit changes (__not__ to `master`).
    2. In this parent repo, add `/taccsite_custom` change.
    3. In this parent repo, commit changes (__not__ to `main`).

## How to Run Tests

### Test TACC CMS Plugins

Testing is run through Django. From within `core_cms` container, run `python manage.py test PATH_TO_DIR_WITH_TESTS` from the repository root directory. Example:

```bash
docker exec -it core_cms /bin/bash
python manage.py test taccsite_cms.contrib.taccsite_sample
```

> __Notice__: To test without migrations—which is _much_ faster—add the flag `--nomigrations` (or `-n`). Example:
> 
> ```bash
> docker exec -it core_cms /bin/bash
> python manage.py test taccsite_cms.contrib.taccsite_sample --nomigrations
> ```

<!-- TODO: Make `python manage.py test` recursively find all the tests -->
<!-- SEE: https://docs.djangoproject.com/en/2.2/topics/testing/overview/#running-tests -->

### Test PostCSS Plugin Configs

Testing is manual review of build output. From within `core_cms` container, run `npm run build` from the repository root directory, then review `taccsite_cms/static/site_cms/css/build/_test.css`.

## Reference

- [Formatting & Linting](https://confluence.tacc.utexas.edu/x/HoBGCw)
- [DjangoCMS Stand Alone Site](https://confluence.tacc.utexas.edu/x/G4G-Ag)
