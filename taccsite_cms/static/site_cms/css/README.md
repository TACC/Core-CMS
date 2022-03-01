# TACC CMS - Stylesheets

Stylesheets are built from source code entry point files located in `./src/*`. Stylesheets are built to static asset artifact directory `./build/*`.

Add new stylesheets into these locations to be picked up by the `npm run build` task and the django `collectstatic` steps.

See [repo `README.md` at "Static Files"](/README.md#static-files).

## Development

- (Standard) Develop Core UI patterns in [Core Styles].
- (Exception) Develop project-specific UI patterns in [Core CMS Resources].


<!-- Link Aliases -->

[Core CMS Resources]: https://github.com/TACC/Core-CMS-Resources
[Core Styles]: https://github.com/tacc-wbomar/Core-Styles
