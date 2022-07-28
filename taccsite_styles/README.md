# TACC CMS - Styles (CSS Source Files)

Styles are compiled:

- from source code at `/taccsite_styles/`
- to static files at `/taccsite_cms/static/site_cms/css/build/`

The `npm run build` step will compile the source code.

The Django `collectstatic` step will read the static files.

See [repo `README.md` at "Static Files"](/README.md#static-files).

## Development

| scope of styles | codebase |
| - | - |
| for CMS & Portal | [Core Styles] |
| CMS-specific     | [Core CMS] |
| project-specific | [Core CMS Resources] |


<!-- Link Aliases -->

[Core CMS]: https://github.com/TACC/Core-CMS
[Core CMS Resources]: https://github.com/TACC/Core-CMS-Resources
[Core Styles]: https://github.com/TACC/tup-ui/tree/main/libs/core-styles
