# Custom Project

| You can customize these features | via this repository | (status) |
| - | - | - |
| templates, static assets, settings, custom apps, URLs, middleware | [Core-CMS-Custom](#via-core-cms-custom) | active |
| templates, static assets, settings | [Core-CMS-Resources](#via-core-cms-resources) | deprecated |

## via [Core CMS Custom]

Work on the project **only** via [Core CMS Custom].

> **Note**
> You should **not** need to clone **nor** edit this [Core CMS] repository.

## via [Core CMS Resources]

### Update Project

To update `/taccsite_custom` to have specific content from [Core CMS Resources]:

- Read [How to Change Submodule Branch Commit](https://github.com/TACC/Core-CMS/wiki/How-to-Change-Submodule-Branch-Commit).

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
docker exec -it core_cms /bin/bash
# That opens a command prompt within the container.
    npm run build:css --project="core-cms"
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

<!-- Link Aliases -->

[Core CMS]: https://github.com/TACC/Core-CMS
[Core CMS Resources]: https://github.com/TACC/Core-CMS-Resources
[Core CMS Custom]: https://github.com/TACC/Core-CMS-Custom

[restart server]: https://github.com/TACC/Core-CMS/wiki/How-to-Restart-the-CMS-Server
[collect static files]: ./develop-project.md#collect-static-files
[build css]: [#build-css]
