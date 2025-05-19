# TACC CMS - Stylesheets

Stylesheets are built from source code entry point files located in `./src/*`. Stylesheets are built to static asset artifact directory `./build/*`.

Add new stylesheets into these locations to be picked up by the `npm run build` task and the django `collectstatic` steps.

See [repo `README.md` at "Static Files"](/README.md#static-files).

## Development

- (Standard) Style TACC UI patterns in [Core Styles].
- (Exception) Style CMS-specific UI in [Core CMS].
- (Exception) Style project-specific UI in [Core CMS Custom] or its own repo.


<!-- Link Aliases -->

[Core CMS]: https://github.com/TACC/Core-CMS
[Core CMS Custom]: https://github.com/TACC/Core-CMS-Custom
[Core Styles]: https://github.com/TACC/Core-Styles
