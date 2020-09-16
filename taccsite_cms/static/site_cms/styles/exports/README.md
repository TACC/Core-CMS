# TACC CMS - Stylesheets - Exports

These entry points are parsed and processed by the `npm run build` step.

## Types of Stylesheets

- `site(.*).css`:    styles that apply to the entire website i.e. global styles
- `page-type.*.css`: styles that apply only to certain types of pages
- `*/*`:             styles that have not yet been organized

## Rules

1. Stylesheets:
    1. __must__ have an appropriate name or directory (see "Types of Stylesheets")
    1. __should__ follow the example styles format (see "Example Styles")
2. Styles for `cms-site-template`:
    1. __must__ be _between_ `BASE STYLES` and `PROJECT STYLES`
    2. __must only__ be styles that should be available to forks
3. Styles for forks of `cms-site-template`:
    1. __must__ be _beneath_ `PROJECT STYLES`

## Example Styles

```css
/* DO NOT ADD STYLES HERE; ONLY IMPORT OTHER STYLESHEETS */

/* --- BASE STYLES --- */
/* --- Do NOT edit, unless you are working on `cms-site-template`! --- */
@import url("_imports/…/__SOME_FILE_A__.css");
@import url("_imports/…/__SOME_FILE_B__.css");

/* --- PROJECT STYLES --- */
/* --- Styles for repos that fork `cms-site-template` go here. --- */
/* … */
```
