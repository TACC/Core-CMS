# TACC Core CMS

https://cep.tacc.utexas.edu/

The base CMS code for TACC WMA Workspace Portals & Websites

## Table of Contents

- [Related Repositories](#related-repositories)
- [Project Architecture](#project-architecture)
- [Project Customization]
- [Prerequisites](#prerequisites)
- [Start Project](#start-project)
- [Update Project](#update-project)
- [Develop Project]
- [Debug Project]
- [Build & Deploy Project] (at "Core-CMS" section)

## Related Repositories

- [Camino], a Docker container-based deployment scheme
- [Core Portal], the base Portal code for TACC WMA CMS Websites
- [Core Styles], the shared UI pattern code for TACC WMA CMS Websites
- [Core CMS Resources], the old solution for extensions of the [Core CMS] project
- [Core CMS Custom], the new solution for extensions of the [Core CMS] project
- [Core Portal Deployments], private repository that facilitates deployments of [Core Portal] images via [Camino] and Jenkins

## Project Architecture

| directory | contents |
| - | - |
| `apps` | additional Django applications |
| `bin` | scripts e.g. build CSS |
| `taccsite_cms` | settings for [Core CMS] |
| `taccsite_custom` | [Git submodule][Git Submodules] of [Core CMS Resources] |
| `taccsite_ui` | files to build [TACC UI Patterns] |

## Project Customization

Read [Project Customization] to learn how to:

- create a new TACC CMS website
- work on an existing TACC CMS website

## Prerequisites

- [Docker] ≥ v20
- [Docker Compose] ≥ v1
- [Python] ≥ v3.8

A CMS project is run using [Docker] and [Docker Compose]. Both must be pre-installed on the system on which you will run the CMS.

[^2]: On a Mac or a Windows machine, we recommended you install
[Docker Desktop](https://www.docker.com/products/docker-desktop), which will install both Docker and Docker Compose as well as Docker Machine, which is required to run Docker on Mac/Windows hosts.

## Start Project

Set up a new local CMS instance.

0. Core CMS:

    Create a `taccsite_cms/settings_local.py` with content from `settings_local.example.py`, e.g.

    ```sh
    cp taccsite_cms/settings_local.example.py taccsite_cms/settings_local.py
    ```

1. Docker Containers:

    ```sh
    make start
    ```

    ```sh
    docker exec -it core_cms /bin/bash
    # This opens a command prompt within the container.
    ```

2. Django Application:

    (Run these commands within the container.)

    ```sh
    python manage.py migrate
    python manage.py createsuperuser
    # To use default "Username" and skip "Email address", press Enter at both prompts.
    # At "Password" prompts, you may use an insecure easy-to-remember password.
    npm ci
    npm run build:css --project="core-cms"
    python manage.py collectstatic --no-input
    ```

3. Django CMS:
    1. Open http://0.0.0.0:8000/.
    2. Login with the credentials you defined in step 2.
    3. Create one CMS page.\
        (With "New page" highlighted, click "Next" button.)
        - This page will automatically be your local homepage.

> **Note**
> A local machine CMS will be empty. It will **not** have content from staging nor production. To have that, follow and adapt instructions to [copy a database](https://confluence.tacc.utexas.edu/x/W4DZDg).

> **Note**
> A local machine CMS does **not** include **nor** integrate with an instance of [Core Portal]. To attempt to do that, follow [How to Use a Custom Docker Compose File](https://github.com/TACC/Core-CMS/wiki/How-to-Use-a-Custom-Docker-Compose-File) and [Locally Develop CMS Portal Docs](https://github.com/TACC/Core-CMS/wiki/Locally-Develop-CMS---Portal---Docs). **Help welcome.**

## Update Project

Update an existing local CMS instance.

1. If CMS `Dockerfile` changed, rebuild Docker Containers:

    ```sh
    make stop
    make build
    make start
    ```

2. If static assets or database models changed, update the Django Application:

    ```sh
    docker exec -it core_cms /bin/bash
    ```

    (Run these commands within the container.)

    ```sh
    python manage.py migrate
    python manage.py collectstatic --no-input
    ```

## Develop Project

Read [Develop Project] for developer instructions.

## Debug Project

Read [Debug Project] for miscellaneous tips.

## Build & Deploy Project

Follow "Core-CMS-Resources" section of [How To Build & Deploy][Build & Deploy Project].

## Release Project

Only appointed team members may release versions.

1. Create new branch for version bump.
1. Update `CHANGELOG.md`.
1. Update version via:\
   `npm version N.N.N`
1. Commit, push, PR, review, merge.
1. Create release and tag on GitHub.
1. Replace Github's unannotated tag with an annotated one:\
   `git pull`
   `git checkout vN.N.N`
   `git tag -d vN.N.N`
   `git tag -a vN.N.N -m "feat: vN.N.N"`
   `git push --tags --force`

## Contributing



## Resources

- [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)
- [Tapis Project (Formerly Agave)](https://tacc-cloud.readthedocs.io/projects/agave/en/latest/)

### Commands

| command | reference |
| - | - |
| `docker exec core_cms /bin/bash` | [docker](https://docs.docker.com/engine/reference/commandline/exec/#run-docker-exec-on-a-running-container)
| `python manage.py migrate` | [django cms](https://docs.django-cms.org/en/release-3.8.x/how_to/install.html#database-tables), [django](https://docs.djangoproject.com/en/3.2/topics/migrations/)
| `python manage.py collectstatic` | [django](https://docs.djangoproject.com/en/3.2/howto/static-files/)
| `python manage.py createsuper` | [django cms](https://docs.django-cms.org/en/release-3.8.x/how_to/install.html#admin-user), [django](https://docs.djangoproject.com/en/3.2/ref/django-admin/#createsuperuser)

<!-- Link Aliases -->

[Camino]: https://github.com/TACC/Camino
[Core CMS]: https://github.com/TACC/Core-CMS
[Core Styles]: https://github.com/TACC/Core-Styles
[Core CMS Resources]: https://github.com/TACC/Core-CMS-Resources
[Core CMS Custom]: https://github.com/TACC/Core-CMS-Custom
[Core Portal]: https://github.com/TACC/Core-Portal
[Core Portal Deployments]: https://github.com/TACC/Core-Portal-Deployments

[Git Submodules]: https://git-scm.com/book/en/v2/Git-Tools-Submodules

[Docker]: https://docs.docker.com/get-docker/
[Docker Compose]: https://docs.docker.com/compose/install/
[Python]: https://www.python.org/downloads/

[TACC UI Patterns]: https://tacc.utexas.edu/static/ui/
[Build & Deploy Project]: https://confluence.tacc.utexas.edu/x/Lo99E

[Project Customization]: ./docs/project-customization.md
[Develop Project]: ./docs/develop-project.md
[Debug Project]: ./docs/debug-project.md
