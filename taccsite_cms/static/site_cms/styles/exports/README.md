# TACC CMS - Stylesheets - Exports

These files are minified and processed by the `npm run build` step.

See [project `README.md` at "Building Static Resources"](/README.md#Building%20Static%20Resources).

All stylesheets are built

- __from__ `../site_cms/…/exports/*` source code entry point files, and populated
- __to__ `../site_cms/build/…/*` as matching build artifacts.

Add new stylesheets into this directory, __NEVER__ that directory!
These will be tracked in the repository and serve as files in which to import source code.

## Rules

1. Files __must__ import styles from [`./_imports`](./_imports).
1. Files __must__ be [named with appropriate format](#Naming%20Format).
1. Files __must__ be [documented in appropriate format](#Documentation%20Format).

## Naming Format

| Format | Description |
| :- | :- |
| `site(.*).css` | styles that apply to the entire website i.e. global styles
| `template.*.css` | styles that apply only to certain types of pages

## Documentation Format

```css
/* DO NOT ADD STYLES HERE; ONLY IMPORT OTHER STYLESHEETS */

/* Organize via ITCSS */
/* SEE: https://confluence.tacc.utexas.edu/x/IAA9Cw */

/* SETTINGS */
/* … */

...

/* COMPONENTS */
/* … */

...
```
