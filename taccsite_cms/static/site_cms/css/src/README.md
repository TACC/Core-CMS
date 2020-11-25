# TACC CMS - Stylesheets

AUTHOR STYLESHEETS HERE!

- Author styles as stylesheet partials in `./_imports/`.
- Import stylesheet partials into entry point files here at `./`.
- Built stylesheets are compiled to `../build/`.

See project `README.md` at ["Static Files"](/README.md#static-files).

_This directory exists in `static/` __only__ because it is customary, using Django, for CSS to be authored in this directory._

## Rules

1. Files __must__ import styles from [`./_imports/`](./_imports).
1. Files __must__ be [named with appropriate format](#Naming%20Format).
1. Files __must__ be [documented in appropriate format](#Documentation%20Format).

## Naming Format

| Format | Description |
| :- | :- |
| `site(.*).css` | styles that apply to the entire website i.e. global styles
| `template.*.css` | styles that apply only to certain templates
| `page.*.css` | styles that apply only to certain pages

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
