# TACC Core CMS

The base CMS code for TACC WMA Workspace Portals & Websites


## Related Repositories

- [Camino], a Docker container-based deployment scheme
- [Core Portal], the base Portal code for TACC WMA CMS Websites
- [Core Styles], the shared UI pattern code for TACC WMA CMS Websites
- [Core CMS Resources], the custom CMS code for TACC WMA CMS Websites
- [Core Portal Deployments], private repository that facilitates deployments of [Core Portal] images via [Camino] and Jenkins


## Local Development Setup

### Prequisites for Running the CMS

* Docker 20.10.7
* Docker Compose 1.29.2
* Python 3.6.8
* Nodejs 16.x (LTS)

The Core CMS can be run using [Docker][1] and [Docker Compose][2]. You will
need both Docker and Docker Compose pre-installed on the system you wish to run the CMS
on.

If you are on a Mac or a Windows machine, the recommended method is to install
[Docker Desktop](https://www.docker.com/products/docker-desktop), which will install both Docker and Docker Compose as well as Docker
Machine, which is required to run Docker on Mac/Windows hosts.


### Code Configuration

After you clone the repository locally, there are several configuration steps required to prepare the project.

#### Required

1. Initialize / Update submodules:
    1. `git submodule init`\
        <sub>Adds [Core CMS Resources] repo as submodule at `taccsite_custom/`. Only necessary once per parent repo clone.</sub>
    2. `git submodule update`\
        <sub>Downloads code from pinned commit of [Core CMS Resources] repo to `taccsite_custom/`.</sub>

#### Optional

Settings may be customized piecemeal by adding, in any of these files, only the settings to change:

| \* | File | Usage |
| - | - | - |
| 1 | `secrets.py` | Sensitive setting we would never commit to GitHub, like DB creds and secret values |
| 2 | `settings_custom.py` | Settings specific to one CMS project (you can symlink to an existing file)† |
| 3 | `settings_local.py` | Settings specific to a local development environment, not intended for others |

<sub>\* This is a "Precedence" column. [A file with a higher precedence value overrides one of a lower value.](https://github.com/TACC/Core-CMS/blob/929dc4b/taccsite_cms/settings.py#L458-L478)</sub>\
<sub>† See [If You Want to Test Custom Resources per CMS Project](#if-you-want-to-test-custom-resources-per-cms-project).</sub>

##### If You Run this CMS Independent of [Core Portal]

Add `INCLUDES_CORE_PORTAL = False` to `taccsite_cms/settings_local.py` (to avoid [Not Found: `core/markup/nav/`](https://github.com/TACC/Core-CMS/wiki/Not-Found%3A--core-markup-nav)).

##### If You Want to Use This With Local [Core Portal] Instance

Follow [How to Use a Custom Docker Compose File](https://github.com/TACC/Core-CMS/wiki/How-to-Use-a-Custom-Docker-Compose-File).

##### If You Want to Test Custom Resources per CMS Project

All CMS projects (besides the stand-alone CMS core), store project-specific resources in the `taccsite_custom` submodule.

1. Create a `taccsite_cms/settings_custom.py` symlink to `taccsite_custom/name-of-project/settings_custom.py`
*†
2. Build project-specific static files. _See [Static Files](/README.md#static-files)._

<sub>\* Where `name-of-project` matches a directory from `/taccsite_custom`.</sub>\
<sub>† Example (from project root): `ln -s ../taccsite_custom/name-of-project/settings_custom.py taccsite_cms/settings_custom.py`\*</sub>


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

    > __Notice__: To log in with a TACC account using LDAP, create the account using the TACC username, then (as an admin or superuser) assign staff and/or superuser privileges. The assigned password can be any password and does __not__ need to be sent to the user. The CMS will __not__ attempt to validate with the assigned password unless LDAP authentication fails. __For production, create a strong password.__

6. [Collect static files][django-static] for Django:

    ```bash
    python manage.py collectstatic
    ```

    _[If `DEBUG` is set to `True`, then this is automated via `python manage.py runserver`.][django-static-serve-dev]_

7. Login to the admin web interface.

    The CMS admin site should now be accessible at http://localhost:8000/admin .*

    _You may log in as the superuser created via the `createsuperuser` command in an earlier step._

    <sub>\* Or at the port defined in a `docker-compose.custom.yml`.</sub>

8. Create the first page of your local CMS.

    > __Warning__: The CMS install will be fresh i.e. the CMS will __not__ be populated with production content.

    You may create pages as needed to test CMS development.

    _In the future, you will be able to clone content from other CMS instances._


[docker-exec-bash]: https://docs.docker.com/engine/reference/commandline/exec/#run-docker-exec-on-a-running-container

[docker-compose-up]: https://docs.docker.com/compose/reference/up/
[docker-compose-build]: https://docs.docker.com/compose/reference/build/

[django-migrate]: https://docs.djangoproject.com/en/3.1/topics/migrations/
[django-static]: https://docs.djangoproject.com/en/3.1/howto/static-files/
[django-static-serve-dev]: https://docs.djangoproject.com/en/2.2/howto/static-files/#serving-static-files-during-development

[django-cms-migrate]: http://docs.django-cms.org/en/latest/how_to/install.html#database-tables
[django-cms-su]: http://docs.django-cms.org/en/latest/how_to/install.html#admin-user


### Static Files

If you changes files in any `static/` directory, you may need to follow some of these steps.

> __Notice__: We configured Django to [ignore `src` directories][ignore-src-dirs] during [`collectstatic`][django-static], so templates can __not__ directly load source files.

[ignore-src-dirs]: https://github.com/TACC/Core-CMS/blob/7b62db1/taccsite_cms/django/contrib/staticfiles_custom/apps.py

#### Quick Start

0. _(assumed)_ Install missing or out-of-date Node dependencies.\*
1. _(optional)_ Make changes to `/taccsite_custom/name-of-project/static/name-of-project/css/src` files. †‡
2. Build static files from source files.\
    Via shell:
    1. `npm run build`\
        or\
        `npm run build --project=name-of-project` †\
        or\
        `npm run build (...) --build-id=optional-identifier` §
3. _(to debug)_ Review respective files' content in\
    `/taccsite_custom/name-of-project/static/name-of-project/css/build`. †
4. "Collect" static files. _See [How to Collect Static Files](#how-to-collect-static-files)._
5. _(to debug)_ Confirm respective output changed in:\
    `/taccsite_cms/static/site_cms/css/build`\
    and/or\
    `/taccsite_custom/static/name-of-project/css/build` †

<sub>\* The recommended command to install expected dependencies is `npm ci`.</sub>\
<sub>† Where `name-of-project` matches a directory from `/taccsite_custom`.</sub>\
<sub>‡ To commit such changes, see [Changing Custom Resources](#changing-custom-resources).</sub>\
<sub>§ A build ID can tag files (e.g. preserved comment in stylesheet).</sub>

#### How to Build Static Files

Certain static files are built __from__ source files __in__ `src` directories __to__ compiled files __in__ `build` directories.

1. Build static resources: \*

    ```bash
    npm run build
    ```

    or †

    ```bash
    npm run build --project=name-of-project
    ```

<sub>\* You should run these commands in the container __from `/code/`__. _See [Running Commands in Container](#running-commands-in-container)._</sub>\
<sub>† Where `name-of-project` matches a directory from `/taccsite_custom`.</sub>

#### How to Collect Static Files

Whenever static files are changed, the CMS must be manually told to serve them.\*

<!-- TODO: [Automatically perform `collectstatic`](https://stackoverflow.com/q/59339571/11817077) -->

1. [Collect static files][django-static] for Django: \*

    ```bash
    python manage.py collectstatic --no-input
    ```

<sub>\* You should run these commands in the container __from `/code/`__. _See [Running Commands in Container](#running-commands-in-container)._</sub>

### Changing Custom Resources

If you need to get the latest files into `/taccsite_custom` from [Core CMS Resources]:

1. [How to Change Submodule Branch Commit](https://github.com/TACC/Core-CMS/wiki/How-to-Change-Submodule-Branch-Commit)

If you need to change files within `/taccsite_custom`:

1. Follow instructions and directory structure of `example-cms`.
2. Create/Edit files in a child directory of `/taccsite_custom`.
4. Reference other projects in `/taccsite_custom`.
5. _(to test static file changes)_ Build static files.\*
6. _(to test template changes)_ Restart server.
7. Commit changes:
    1. In `/taccsite_custom` submodule repo, commit changes (__not__ to `main` branch).
    2. In this parent repo, add `/taccsite_custom` change.
    3. In this parent repo, commit changes (__not__ to `main` branch).

<sub>To learn more, see [Static Files](#static-files).</sub>

### Customizing Text in Admin UI

1. Create file `/taccsite_cms/locale/en/LC_MESSAGES/django.po`.
2. Add to the file only the strings to translate and the appropriate comments for that string.
3. Build the `.mo` file: \*

    ```bash
    django-admin compilemessages
    ```

4. Restart the CMS server.[^3]†

<sub>\* You should run this command in the container __from `/code/`__. _See [Running Commands in Container](#running-commands-in-container)._</sub>\
<sub>† See [Restarting the CMS Server](#restarting-the-cms-server).</sub>

### UI Pattern Demo

This demo shows [Core Styles] with `site.css` from either [Core CMS] or a [Core CMS Resources] project.

1. Build UI patterns demo: \*

    ```bash
    npm run build:css-demo --project=name-of-project
    ```

2. Serve the demo:

    ```bash
    npm run start:css-demo
    ```

<sub>\* Where `name-of-project` is "core-cms" or matches a directory from `/taccsite_custom`. __A project name is required.__</sub>


## Running Commands in Container

__If using `docker-compose.yml` then__ run certain commands via shell within container (because files are __not__ re-synced with local machine).

__If using `docker-compose.dev.yml` or `docker-compose.custom.yml` then__ run certain commands __either__ on local machine __or__ via shell within container (because files are re-synced with local machine).

To [enter shell within container][docker-exec-bash]: \*

```bash
docker exec -it core_cms /bin/bash
```

<sub>\* __If using `docker-compose.custom.yml`, then__ change  `core_cms` to its `cms:` `container_name`.</sub>

## Restarting the CMS Server

See [How to Restart the CMS Server](https://github.com/TACC/Core-CMS/wiki/How-to-Restart-the-CMS-Server).

## Setting up Search Index

See [How to Build Search Index](https://github.com/TACC/Core-CMS/wiki/How-to-Build-Search-Index).


## Linting and Formatting Conventions

Not standardized. See [(internal) Formatting & Linting](https://confluence.tacc.utexas.edu/x/HoBGCw).


## Testing

Server-side CMS plugin testing is run through Python. Start docker container first by `docker exec -it core_cms bash`, Then run `python manage.py test path.to-dir.with.tests`\* from the project root folder to run backend tests and display a report at the bottom of the output.

<sub>\* To run tests without console logging, run `python manage.py test path.to-dir.with.tests --nomigrations`.</sub>

<!-- TODO: Make command recursively find all tests -->
<!-- SEE: https://docs.djangoproject.com/en/2.2/topics/testing/overview/#running-tests -->

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

#### Testing Core Styles Changes Locally

See [Locally Develop CMS and Styles](https://github.com/TACC/Core-CMS/wiki/Locally-Develop-CMS-and-Styles).

### Best Practices

Sign your commits ([see this link](https://help.github.com/en/github/authenticating-to-github/managing-commit-signature-verification) for help)

### Release Workflow

Only appointed team members may release versions.

1. Create new branch for version bump.
1. Update `CHANGELOG.md`.
1. Update version via `npm version N.N.N` (run from `.../core-styles/`).
1. Commit, push, PR, review, merge.
1. Tag version i.e.
    1. `git tag -a vN.N.N -m "vN.N.N"`
    2. `git push origin vN.N.N`
1. Author a release via GitHub (choose the tag from previous step).

### Resources

* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)
* [Tapis Project (Formerly Agave)](https://tacc-cloud.readthedocs.io/projects/agave/en/latest/)


<!-- Link Aliases -->

[Core Portal Deployments]: https://github.com/TACC/Core-Portal-Deployments
[Camino]: https://github.com/TACC/Camino
[Core CMS]: https://github.com/TACC/Core-CMS
[Core Styles]: https://github.com/TACC/tup-ui/tree/main/libs/core-styles
[Core CMS Resources]: https://github.com/TACC/Core-CMS-Resources
[Core Portal]: https://github.com/TACC/Core-Portal
[1]: https://docs.docker.com/get-docker/
[2]: https://docs.docker.com/compose/install/
