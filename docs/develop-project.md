# Develop Project

Read [Django CMS User Guide] for CMS user instructions.

## Table of Contents

- [Build Static Files](#build-static-files)
- [Collect Static Files](#collect-static-files)
- [Customize Admin UI Text](#customize-admin-ui-text)
- [Demo UI Patterns](#demo-ui-patterns)
- [Develop with Core Styles Simultaneously](#develop-with-core-styles-simultaneously)

## Build Static Files

All CSS static files are built:

- **from** source files **in** `src` directories
- **to** compiled files **in** `build` directories

This allows use of future-proof CSS via [Core-Styles].

```sh
docker exec -it core_cms /bin/bash
# That opens a command prompt within the container.
    npm run build:css --project="core-cms"
```

## Collect Static Files

Whenever files in a `static/` directory are changed, the CMS must be manually told to serve them:

```sh
docker exec -it core_cms /bin/bash
# That opens a command prompt within the container.
    python manage.py collectstatic --no-input
```

> **Note**
> [Building static files](#build-static-files) **is** a changes to files in a `static/` directory.

> **Note**
> We may be able to [automatically perform `collectstatic`](https://stackoverflow.com/q/59339571/11817077). **Help wanted.**

## Customize Admin UI Text

1. Create file:\
    `/taccsite_cms/locale/en/LC_MESSAGES/django.po`
2. Add to the file only:
    - the strings to translate
    - appropriate comments for that string\
        (reference the existing entries)
3. Build the `.mo` file:

    ```sh
    docker exec -it core_cms /bin/bash
    # That opens a command prompt within the container.
        cd /code
        apt-get install gettext
        django-admin compilemessages
    ```

4. [Restart the CMS server.][restart server]

## Demo UI Patterns

A demo of any documented CSS modules from [Core Styles] and [Core CMS].

1. Build and serve:

    ```sh
    docker exec -it core_cms /bin/bash
    # That opens a command prompt within the container.
        npm run build:ui-demo
        python manage.py collectstatic --no-input
    ```

2. Open http://localhost:8000/static/ui/index.html.

## Develop with [Core Styles] Simultaneously

See [Locally Develop CMS and Styles](https://github.com/TACC/Core-CMS/wiki/Locally-Develop-CMS-and-Styles).

<!-- Link Aliases -->

[Core Styles]: https://github.com/TACC/Core-Styles

[restart server]: https://github.com/TACC/Core-CMS/wiki/How-to-Restart-the-CMS-Server

[Django CMS User Guide]: https://confluence.tacc.utexas.edu/x/FgDqCw
