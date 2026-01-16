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
  - [Develop a Custom App/Plugin](#develop-a-custom-appplugin)
- [Test Project](#test-project)
- [Debug Project](#debug-project)
- [Build & Deploy Project](#build--deploy-project)
- [Contributing](#contributing)
- [Resources](#resources)

## Related Repositories

- [Camino], a Docker container-based deployment scheme
- [Core Portal], the base Portal code for TACC WMA CMS Websites
- [Core Styles], the shared UI pattern code for TACC WMA CMS Websites
- [Core CMS Template], a template for creating new TACC WMA CMS projects
- [Core CMS Custom], the new solution for extensions of the [Core CMS] project
- [Core Portal Deployments], private repository that facilitates deployments of [Core Portal] images via [Camino] and Jenkins

## Project Architecture

| directory | contents |
| - | - |
| `apps` | additional Django applications |
| `bin` | scripts e.g. build CSS |
| `taccsite_cms` | customize & configure [Django CMS] |

## Prerequisites

* [Docker]
  * Docker Engine ≥ v20
  * [Docker Compose]

> **Important**
> We recommend you install the Docker Desktop application. Alternatively, you may install both Docker Engine and Docker Compose.

## Getting Started

How to set up a new local CMS instance.

> **Important**
> To develop a new or existing **custom** CMS website for a TACC client, do **not** clone this repository. Instead, read [Develop a Custom Project]. To develop on the Core CMS (upon which our other CMS are built) continute reading.

### Quick Setup

0. Enter CMS project:
    ```sh
    cd cms
    ```
1. (optional) To remove previous setup **entirely**:
    ```sh
    make clean
    ```
2. Run the setup script:
    ```sh
    make setup
    ```
    You will be prompted for information.
3. [Add Content](#add-content).

### Manual Setup

> [!NOTE]
> If [Quick Start](#quick-start) process fails, report the error to your team, and follow these steps for now.

1. Configure [Django] Application:

    Create a `taccsite_cms/*.py` for every `*.example.py`, e.g.

    ```sh
    cp taccsite_cms/settings_custom.example.py taccsite_cms/settings_custom.py
    cp taccsite_cms/secrets.example.py taccsite_cms/secrets.py
    cp taccsite_cms/settings_local.example.py taccsite_cms/settings_local.py
    ```

2. Start [Docker] Containers:

    ```sh
    make start
    ```

    > **Note**
    > This will make the terminal window busy. To run commands after this, **either** open a new terminal window **or** run `make start ARGS="--detach"` instead.

3. Prepare [Django] Application:

    ```sh
    docker exec -it core_cms /bin/bash
    # This opens a command prompt within the container
    ```

    (Run these commands within the container.)

    ```sh
    python manage.py migrate
    python manage.py createsuperuser
    # To use default "Username" and skip "Email address", press Enter at both prompts.
    # At "Password" prompts, you may use an easy-to-remember password.
    python manage.py collectstatic --no-input

    ```

4. [Add Content](#add-content).

#### Add Content

1. Open http://localhost:8000/.
2. Login with the credentials you defined in step 2.
3. Create one CMS page.\
    (With "New page" highlighted, click "Next" button.)
    - This page will automatically be your local homepage.

> **Important**
> A local machine CMS will be empty. It will **not** have content from staging **nor** production. If you need that, follow and adapt instructions to [replicate a CMS database](https://tacc-main.atlassian.net/wiki/x/GwBJAg). This requires high-level server access or somone to give you a copy of the content.

> **Note**
> A local machine CMS does **not** include **nor** integrate with an instance of [Core Portal]. To attempt to do that, follow [How to Use a Custom Docker Compose File](https://github.com/TACC/Core-CMS/wiki/How-to-Use-a-Custom-Docker-Compose-File) and [Locally Develop CMS Portal Docs](https://github.com/TACC/Core-CMS/wiki/Locally-Develop-CMS---Portal---Docs). **Help welcome.**

## Update Project

To update an existing CMS instance.

### New Major Version (or v3.12)

Read [Upgrade Project] for developer instructions.

### New Minor or Patch Version (or Branch)

```sh
make stop
make build
make start
```

<details><summary>Advanced</summary>

To only update as necessary, or update since uncommon changes:

| | If this changed | Run this command |
| - | - | - |
| 0 | Dockerfile | `make stop`, `make build`, `make start` |
| 1 | Python models | `docker exec -it core_cms sh -c "python manage.py migrate"` |
| 2 | Node dependencies | `npm ci` |
| 3 | CSS stylesheets | `npm run build:css` |
| 4 | Assets e.g.<br><sub>images, stylesheets, JavaScript</sub> | `docker exec -it core_cms sh -c "python manage.py collectstatic --no-input"` |

</details>

## Develop Project

Read [Django CMS User Guide] for CMS user instructions.

Read [Develop Project] for developer instructions.

### Develop a Custom Project

To develop a new or existing custom CMS website for a client, read [Develop a Custom Project].

### Develop a Custom App/Plugin

To develop a new or existing Django CMS app or plugin for a client, read [Develop a Custom App/Plugin].

## Test Project

Read [Testing] for miscellaneous workflows.

## Debug Project

Read [Debug Project] for miscellaneous tips.

## Build & Deploy Project

Follow "Core-CMS" section of [How To Build & Deploy][Build & Deploy Project].

## Contributing

To contribute, first read [How to Contribute][Contributing].

## Resources

### Commands

| command | reference |
| - | - |
| `docker exec -it core_cms /bin/bash` | [docker](https://docs.docker.com/engine/reference/commandline/exec/#run-docker-exec-on-a-running-container)
| `python manage.py migrate` | [django cms](https://docs.django-cms.org/en/release-3.8.x/how_to/install.html#database-tables), [django](https://docs.djangoproject.com/en/3.2/topics/migrations/)
| `python manage.py collectstatic` | [django](https://docs.djangoproject.com/en/3.2/howto/static-files/)
| `python manage.py createsuperuser` | [django cms](https://docs.django-cms.org/en/release-3.8.x/how_to/install.html#admin-user), [django](https://docs.djangoproject.com/en/3.2/ref/django-admin/#createsuperuser)

<!-- Link Aliases -->

[Camino]: https://github.com/TACC/Camino
[Core CMS]: https://github.com/TACC/Core-CMS
[Core Styles]: https://github.com/TACC/Core-Styles
[Core CMS Template]: https://github.com/TACC/Core-CMS-Template
[Core CMS Custom]: https://github.com/TACC/Core-CMS-Custom
[Core Portal]: https://github.com/TACC/Core-Portal
[Core Portal Deployments]: https://github.com/TACC/Core-Portal-Deployments

[Git Submodules]: https://git-scm.com/book/en/v2/Git-Tools-Submodules

[Docker]: https://docs.docker.com/get-docker/
[Docker Compose]: https://docs.docker.com/compose/install/

[Django]: https://www.djangoproject.com/
[Django CMS]: https://www.django-cms.org/
[Django CMS User Guide]: https://tacc-main.atlassian.net/wiki/x/phdv

[Build & Deploy Project]: https://tacc-main.atlassian.net/wiki/x/2AVv

[Develop a Custom Project]: ./docs/develop-custom-project.md
[Develop a Custom App/Plugin]: ./docs/develop-custom-app.md
[Develop Project]: ./docs/develop-project.md
[Upgrade Project]: ./docs/upgrade-project.md
[Debug Project]: ./docs/debug-project.md
[Testing]: ./TESTING.md
[Contributing]: ./CONTRIBUTING.md
