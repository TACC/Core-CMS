# TACC Core CMS

https://cep.tacc.utexas.edu/

The base CMS code for TACC WMA Workspace Portals & Websites

## Table of Contents

- [Related Repositories](#related-repositories)
- [Project Architecture](#project-architecture)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Update Project](#update-project)
- [Develop Project](#develop-project)
  - [Develop a Custom Project](#develop-a-custom-project)
- [Debug Project](#debug-project)
- [Build & Deploy Project](#build--deploy-project)
- [Contributing](#contributing)
- [Resources](#resources)

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

## Prerequisites

* [Docker]
  * [Docker Engine] ≥ v20
  * [Docker Compose]

> **Important**
> We recommend you install the Docker Desktop application. Alternatively, you may install both Docker Engine and Docker Compose.

## Getting Started

> **Important**
> To develop a new or existing custom CMS website for a TACC client, do **not** clone this repository. Instead, read [Develop a Custom Project]. To develop on the Core CMS (upon which our other CMS are built) continute reading.

Set up a new local CMS instance.

0. [Clone this Repository.](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
1. Enter the Repository Clone:

    ```sh
    cd Core-CMS
    ```

2. Add Core CMS Settings:

    Create a `taccsite_cms/settings_local.py` with content from `settings_local.example.py`, e.g.

    ```sh
    cp taccsite_cms/settings_local.example.py taccsite_cms/settings_local.py
    ```

3. Build & Start the Docker Containers:

    ```sh
    make start
    ```

4. Enter the CMS Docker Container:

    (This opens a command prompt within the container.)

    ```sh
    docker exec -it core_cms /bin/bash
    ```

5. Run the Django Application:

    (Run these commands within the container.)

    ```sh
    python manage.py migrate
    python manage.py createsuperuser
    # To use default "Username" and skip "Email address", press Enter at both prompts.
    # At "Password" prompts, you may use an easy-to-remember password.
    python manage.py collectstatic --no-input

    ```

6. Open Django CMS:
    1. Open http://localhost:8000/.
    2. Login with the credentials you defined in step 2.
    3. Create one CMS page.\
        (With "New page" highlighted, click "Next" button.)
        - This page will automatically be your local homepage.

> **Important**
> A local machine CMS will be empty. It will **not** have content from staging **nor** production. If you need that, follow and adapt instructions to [copy a database](https://confluence.tacc.utexas.edu/x/W4DZDg).

> **Note**
> A local machine CMS does **not** include **nor** integrate with an instance of [Core Portal]. To attempt to do that, follow [How to Use a Custom Docker Compose File](https://github.com/TACC/Core-CMS/wiki/How-to-Use-a-Custom-Docker-Compose-File) and [Locally Develop CMS Portal Docs](https://github.com/TACC/Core-CMS/wiki/Locally-Develop-CMS---Portal---Docs). **Help welcome.**

## Update Project

To update an existing CMS instance.

### New Major Version (or v3.12)

Read [Upgrade Project] for developer instructions.

### New Minor or Patch Version (or Branch)

- If CMS `Dockerfile` changed, rebuild Docker Containers:

    ```sh
    make stop
    make build
    make start
    ```

- If anything else changed, update the Django application:

    ```sh
    docker exec -it core_cms /bin/bash
    # This opens a command prompt within the container.
    ```

  Run relevant commands within the container:

  - If **styles** changed:

      ```sh
      npm ci
      npm run build:css --project="core-cms"
      python manage.py collectstatic --no-input
      ```

  - If **assets** changed:

      ```sh
      python manage.py collectstatic --no-input
      ```

  - If **models** changed:

      ```sh
      python manage.py migrate
      ```

## Develop Project

Read [Django CMS User Guide] for CMS user instructions.

Read [Develop Project] for developer instructions.

### Develop a Custom CMS Project

To develop a new or existing custom CMS website for a client, read [Project Customization].

## Debug Project

Read [Debug Project] for miscellaneous tips.

## Build & Deploy Project

Follow "Core-CMS" section of [How To Build & Deploy][Build & Deploy Project].

## Contributing

To contribute, first read [How to Contirbute][Contributing].

## Resources

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

[TACC UI Patterns]: https://tacc.utexas.edu/static/ui/
[Build & Deploy Project]: https://confluence.tacc.utexas.edu/x/Lo99E
[Django CMS User Guide]: https://confluence.tacc.utexas.edu/x/FgDqCw

[Develop a Custom Project]: ./docs/develop-custom-project.md
[Develop Project]: ./docs/develop-project.md
[Upgrade Project]: ./docs/upgrade-project.md
[Debug Project]: ./docs/debug-project.md
[Contributing]: ./docs/contributing.md
