# TACC CMS - Stylesheets - Imports

AUTHOR ACTUAL STYLES HERE!

These styles are only to be imported by other stylesheets.

## Rules

1. Files __must__ be [located in appropriate directory](#directories).
1. Files __must__ be [documented in appropriate format](#documentation-format).
1. Files __must__ follow the [style guide](#style-guide).

1. Styles __should__ be [structural](#structure-vs-skin) and __may__ be a [skin](#structure-vs-skin).

## Directories

These directories are based on [ITCSS][tacc-itcss].

[tacc-itcss]: https://confluence.tacc.utexas.edu/x/IAA9Cw

## Documentation Format

```css
/*
Styles Name

Description of the purpose and use case of styles. Use the `Markup:` property to link to sample markup. The documentation format is [KSS Node](https://github.com/kss-node/kss-node/blob/master/README.md).

Markup: x-stylesheet-name.html

Styleguide __StylesSection__.__StylesName__
*/

.some-selector {
  text-transform: none;
}
```

## Style Guide

See [TACC: CSS Style Guide](https://confluence.tacc.utexas.edu/x/ZQALBg).

## Structure vs. Skin

- Most Core styles will be _only __or__ mostly_ for [structure][tacc-oocss].
- Some core styles may be [skin][tacc-oocss].

[tacc-oocss]: https://confluence.tacc.utexas.edu/x/VwALBg
