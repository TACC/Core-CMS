# TACC CMS - Stylesheets - Source

AUTHOR STYLESHEETS HERE!

- Author styles as stylesheet partials in `./_imports/`.
- Import stylesheet partials into entry point files here at `./`.
- Built stylesheets are compiled to `../build/`.

See project `README.md` at ["Static Files"](/README.md#static-files) and [CMS UI Organization].

_This directory exists in `static/` __only__ because it is customary, using Django, for CSS to be authored in this directory._

## Rules

1. Files __must__ import styles from [Core Styles].[^1]
1. Files __must__ be [named with appropriate format](#naming-format).
1. Files __must__ be [documented in appropriate format](#documentation-format).

[^1]: The `_migrations` directory is a short-term exception.

## Naming Format

| Format | Description |
| :- | :- |
| `site(.*).css` | styles that apply to the entire website i.e. global styles
| `template.*.css` | styles that apply only to certain templates
| `page.*.css` | styles that apply only to certain pages
| `app.*.css` | styles that apply only to certain apps (a.k.a. plugins)
| `migrate.*.css` | styles that apply to websites that have been migrated[^2]

[^2]: When sensible, use the migration folder name, i.e. `migrate.v1_v2.css`.

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


<!-- Link Aliases -->

[Core Styles]: https://github.com/TACC/tup-ui/tree/main/libs/core-styles
[CMS UI Organization]: https://confluence.tacc.utexas.edu/x/54AZCg
