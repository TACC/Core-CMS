# Develop a Custom Project

| You can do these actions | via this resource | (status) |
| - | - | - |
| **customize** static assets | [Core CMS Custom] | active |
| **customize** templates, static assets, settings | [Core CMS Resources](#via-core-cms-resources) | deprecated |
| **customize** templates, static assets, custom apps, URLs, middleware | [Core CMS Template] | active |
| **create** or **customize** an app | [Develop a Custom App/Plugin](./develop-custom-app.md) | active |

## via [Core CMS Resources]

> [!DANGER]
> Deprecated solution.

> [!TIP]
> Use [Core CMS Custom] or [Core CMS Template] instead.

### Update Project

To update `/taccsite_custom` to have **pinned** content from [Core CMS Resources]:

1. `git submodule update`

To update `/taccsite_custom` to have **new** content from [Core CMS Resources]:

1. `cd taccsite_custom`
2. Checkout desired [Core CMS Resources] branch.
3. `git pull`
4. `cd ../`

To make CMS on local machine register changes to files in `/taccsite_custom`:

| types of files changed | action to take |
| - | - |
| `static/css` | [build css] |
| `static/` | [collect static files] |
| `templates/` | [restart server] |

### Build CSS

To compile CSS static files:

- **from** source files **in** `src` directories
- **to** compiled files **in** `build` directories

```sh
npm run build:css --project="custom_project_dir"
docker exec -it core_cms sh -c "python manage.py collectstatic --no-input"

```

This process allows use of future-proof CSS via [Core Styles].

### Commit Changes

To commit changes to a custom project:

1. `cd taccsite_custom`
2. Checkout or create a [Core CMS Resources] branch.
3. Commit changes.
4. `cd ../`
5. Add `/taccsite_custom` change.
6. Commit changes to a [Core CMS] branch.

> [!NOTE]
> For a more thorough walkthrough, read [How to Change Submodule Branch Commit](https://github.com/TACC/Core-CMS/wiki/How-to-Change-Submodule-Branch-Commit).

<!-- Link Aliases -->

[Core CMS]: https://github.com/TACC/Core-CMS
[Core Styles]: https://github.com/TACC/Core-Styles
[Core CMS Custom]: https://github.com/TACC/Core-CMS-Custom
[Core CMS Resources]: https://github.com/TACC/Core-CMS-Resources
[Core CMS Template]: https://github.com/TACC/Core-CMS-Template

[restart server]: https://github.com/TACC/Core-CMS/wiki/How-to-Restart-the-CMS-Server
[collect static files]: ./develop-project.md#collect-static-files
[build css]: [#build-css]
