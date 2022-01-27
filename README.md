# TACC Core CMS

The base CMS code for TACC WMA Workspace Portals & Websites


## Related Repositories

- [Camino], a Docker container-based deployment scheme
- [Core Portal], the base Portal code for TACC WMA CMS Websites
- [Core Portal Deployments], private repository that facilitates deployments of [Core Portal] images via [Camino] and Jenkins


## Local Development Setup

### Prequisites for Running the CMS

* Docker 20.10.7
* Docker Compose 1.29.2
* Python 3.6.8
* Nodejs 12.x (LTS)

The Core Portal can be run using [Docker][1] and [Docker Compose][2]. You will
need both Docker and Docker Compose pre-installed on the system you wish to run the CMS
on.

If you are on a Mac or a Windows machine, the recommended method is to install
[Docker Desktop](https://www.docker.com/products/docker-desktop), which will install both Docker and Docker Compose as well as Docker
Machine, which is required to run Docker on Mac/Windows hosts.


### Code Configuration

After you clone the repository locally, there are several configuration steps required to prepare the project.

#### Required

1. Create a `.env` file\* at the root of the project with this content:

    ```bash
    CUSTOM_ASSET_DIR=example-cms
    ```

    Where `example-cms` is the project to be run. See [Custom Resources per CMS Project](#custom-resources-per-cms-project).

1. Initialize / Update submodules.
    1. `git submodule init`\
        Adds `cms-site-resources` repo as submodule at `taccsite_custom/`. Only necessary once per `CORE-cms` repo clone.
    2. `git submodule update`\
        Downloads code from pinned commit of `cms-site-resources` repo to `taccsite_custom/`.

\* A ["dotenv" file](https://hexdocs.pm/dotenvy/dotenv-file-format.html) is a file, with or without a name, that has the `.env` extension.

#### Dependent

##### If You Run this CMS Indepednent of [Core-Portal](https://github.com/TACC/Core-Portal/)

Add `INCLUDES_CORE_PORTAL = False` to `taccsite_cms/settings_local.py` (to avoid [Not Found: core/markup/nav](https://github.com/TACC/Core-CMS/wiki/Not-Found%3A--core-markup-nav)).

##### If You Also Have a Local [Core-Portal](https://github.com/TACC/Core-Portal/) Instance

Follow [How to Use a Custom Docker Compose File](https://github.com/TACC/Core-CMS/wiki/How-to-Use-a-Custom-Docker-Compose-File).

#### Optional

##### Custom Configuration

Settings may be customized piecemeal by creating any of these files with just the settings to change:

| \* | File | Usage |
| - | - | - |
| 1 | `secrets.py` | Sensitive setting we would never commit to GitHub, like DB creds and secret values |
| 2 | `settings_custom.py` | Settings specific to one CMS project (you can symlink to an existing file)† |
| 3 | `settings_local.py` | Settings specific to a local development environment, not intended for others |

\* This is a "Precedence" column. A file with a higher precedence value overrides one of a lower value.

† Example (from project root): `ln -s ../taccsite_custom/name-of-project/settings_custom.py taccsite_cms/settings_custom.py`‡

‡ Where `name-of-project` matches a directory from `/taccsite_custom`.

##### Custom Resources per CMS Project

All CMS projects (besides the stand-alone CMS core), store project-specific resources in the `taccsite_custom` submodule.

1. Create a `taccsite_cms/settings_custom.py` symlink to `taccsite_custom/name-of-project/settings_custom.py`.\*†
2. Update the `.env` file so `CUSTOM_ASSET_DIR=name-of-project`.\*
3. Re-build static assets, so that project-specific assets are built. _See ["Static Files"](/README.md#static-files)._

\* Where `name-of-project` matches a directory from `/taccsite_custom`.

† Example (from project root): `ln -s ../taccsite_custom/name-of-project/settings_custom.py taccsite_cms/settings_custom.py`\*


### Running the CMS

1. [Build][docker-compose-build] the CMS and database images:

    ```bash
    docker-compose build
    ```

    Or, if you have a `docker-compose.custom.yml`, then:

    ```bash
    docker-compose -f docker-compose.custom.yml build
    ```

2. [Create and run][docker-compose-up] the CMS and database containers:

    ```bash
    docker-compose up
    ```

    Or, if you have a `docker-compose.custom.yml`, then:

    ```bash
    docker-compose -f docker-compose.custom.yml up
    ```

3. [Start a bash session][docker-exec-bash] into the CMS container:


    > __Notice__: If you have a `docker-compose.custom.yml`, then change  `core_cms` in this command to the `cms`: `container_name` in the `docker-compose.custom.yml`.

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

[django-static-serve-dev]: https://docs.djangoproject.com/en/3.1/howto/static-files/#serving-static-files-during-development


### Static Files

If you changes files in any `static/` directory, you may need to follow some of these steps.

> __Notice__: We configured Django to ignore `src` directories during [`collectstatic`][django-static], so templates can __not__ directly load source files.

#### Quick Start

1. _(optional)_ Make changes to `/taccsite_cms/static/…/src` files.
2. Build static files from source files via:
    - _(manually, for any ready changes)_ `npm run build`
    - _(automatically, on source change)_ `npm run watch`
3. _(to debug)_ Review respective `/taccsite_cms/static/…/build` files' content.
4. "Collect" static files. _See [How to Collect Static Files](#how-to-collect-static-files)._
5. _(to debug)_ Confirm respective `/static/…/build` output changed.

#### How to Build Static Files

Certain static files are built __from__ source files __in__ `src` directories __to__ compiled files __in__ `build` directories.

> __Using `docker-compose.yml`__: Run these commands in bash session within container (because files are __not__ re-synced).

> __Using `docker-compose.dev.yml` or `docker-compose.custom.yml`__: Run these commands on local machine __or__ in bash session within container (because files are re-synced).

- [Start a bash session][docker-exec-bash] into the CMS container:

    > __Notice__: If you have a `docker-compose.custom.yml`, then change  `core_cms` in this command to the `cms`: `container_name` in the `docker-compose.custom.yml`.

    ```bash
    docker exec -it core_cms /bin/bash
    ```

1. Build static resources:

    ```bash
    npm run build
    ```

2. _(optional)_ [Watch][npm-pkg-watch] files, and re-build when source files change:

    ```bash
    npm run watch
    ```

    > __Notice__: This feature is __not__ reliable for _all_ changes on _all_ relevant files.

[npm-cli-install]: https://docs.npmjs.com/cli/install
[npm-pkg-watch]: https://www.npmjs.com/package/npm-watch

#### How to Collect Static Files

Whenever static files are changed, the CMS must be manually told to serve them.\*

<!-- TODO: [Automatically perform `collectstatic`](https://stackoverflow.com/q/59339571/11817077) -->

1. [Start a bash session][docker-exec-bash] into the CMS container:

    > __Notice__: If you have a `docker-compose.custom.yml`, then change  `core_cms` in this command to the `cms`: `container_name` in the `docker-compose.custom.yml`.

    ```bash
    docker exec -it core_cms /bin/bash
    ```

2. [Collect static files][django-static] for Django:

    ```bash
    python manage.py collectstatic
    ```

### Custom Resources

If you need to change files within `/taccsite_custom`:

1. Follow instructions and directory structure of `example-cms`.
2. Create/Edit files in a child directory of `/taccsite_custom`.
3. Reference other projects in `/taccsite_custom`.
4. _(for static asset changes)_ Build static assets.
5. _(for template changes)_ Restart server.
6. Commit changes:
    1. In `/taccsite_custom` submodule repo, commit changes (__not__ to `main`).
    2. In this parent repo, add `/taccsite_custom` change.
    3. In this parent repo, commit changes (__not__ to `main`).

    _For more detailed steps, see [How to Change Submodule Branch Commit](https://github.com/TACC/Core-CMS/wiki/How-to-Change-Submodule-Branch-Commit)._


## Setting up Search Index

See [How to Build Search Index](https://github.com/TACC/Core-CMS/wiki/How-to-Build-Search-Index).

## Linting and Formatting Conventions

Not standardized. See [(internal) Formatting & Linting](https://confluence.tacc.utexas.edu/x/HoBGCw).


## Testing

Server-side CMS plugin testing is run through Python. Start docker container first by `docker exec -it core_cms bash`, Then run `python manage.py test path.to-dir.with.tests`\* from the project root folder to run backend tests and display a report at the bottom of the output.

\* To run tests without console logging, run `python manage.py test path.to-dir.with.tests --nomigrations`.

<!-- TODO: Make command recursively find all tests -->
<!-- SEE: https://docs.djangoproject.com/en/2.2/topics/testing/overview/#running-tests -->

Client-side stylesheet plugin testing is done manually. Run `npm run build` from any folder in this project, then review output in `taccsite_cms/static/site_cms/css/build/_test.css`, to ensure plugins are working correctly.

### Test Coverage

Coverage is sent to codecov on commits to the repo (see Github Actions for branch to see branch coverage). Ideally we only merge positive code coverage changes to `main`.

### Production Deployment

The Core CMS runs in a Docker container as part of a set of services managed with Docker Compose.

CMS images are built by [Jenkins](https://jenkins01.tacc.utexas.edu/view/WMA%20CEP/job/Core_CMS/) and published to the [Docker Hub repo](https://hub.docker.com/repository/docker/taccwma/core-cms).

To update the CMS in production or dev, the corresponding [Core Portal Deployments](https://github.com/TACC/Core-Portal-Deployments) env file should be updated with a tag matching an image previously built and published to the taccwma/core-cms repo.

Deployments are initiated via [Jenkins](https://jenkins01.tacc.utexas.edu/view/WMA%20CEP/job/Core_Portal_Deploy/) and orchestrated, tracked, and directed by [Camino](https://github.com/TACC/Camino) on the target server.


## Deployment Steps

1. Build and publish portal image with [Jenkins](https://jenkins01.tacc.utexas.edu/view/WMA%20CEP/job/Core_CMS/)
2. Update deployment settings, particularly the `CMS_TAG` environment variable in [Core Portal Deployments](https://github.com/TACC/Core-Portal-Deployments) with new tag name
3. Deploy new image with [Jenkins](https://jenkins01.tacc.utexas.edu/view/WMA%20CEP/job/Core_Portal_Deploy/)


## Contributing

### Development Workflow

We use a modifed version of [GitFlow](https://datasift.github.io/gitflow/IntroducingGitFlow.html) as our development workflow. Our [development site](https://dev.cep.tacc.utexas.edu) (accessible behind the TACC Network) is always up-to-date with `main`, while the [production site](https://prod.cep.tacc.utexas.edu) is built to a hashed commit tag.
- Feature branches contain major updates, bug fixes, and hot fixes with respective branch prefixes:
    - `task/` for features and updates
    - `bug/` for bugfixes
    - `fix/` for hotfixes

### Best Practices

Sign your commits ([see this link](https://help.github.com/en/github/authenticating-to-github/managing-commit-signature-verification) for help)

### Resources

* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)
* [Tapis Project (Formerly Agave)](https://tacc-cloud.readthedocs.io/projects/agave/en/latest/)


<!-- Link Aliases -->

[Core Portal Deployments]: https://github.com/TACC/Core-Portal-Deployments
[Camino]: https://github.com/TACC/Camino
[Core CMS]: https://github.com/TACC/Core-CMS
[Core Portal]: https://github.com/TACC/Core-Portal
[1]: https://docs.docker.com/get-docker/
[2]: https://docs.docker.com/compose/install/
