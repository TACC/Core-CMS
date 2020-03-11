# TACC CMS - Stylesheets - Imports

These styles are intended to be imported by other stylesheets.

## Directories

These directories and files are based on ITCSS (see [CSS Organization][tacc-style-guide]).

    ./
        |_ settings     // global custom values
        |_ tools        // mixins and functions
        |_ generics     // styles which are widespread and stable
        |_ elements     // styles which use tag-based selectors
        |_ objects      // modules which are generic and reusable
        |_ components   // modules which are specific and reusable
        |_ trumps       // overrides via scopes, utilities, hacks

[tacc-css-org]: https://confluence.tacc.utexas.edu/x/DADMBQ

## Rules

1. Stylesheets:
    1. __must__ be in the appropriate directory (see "Directories").
    1. __must__ follow the example styles format (see "Example Styles").
2. Styles for `cms-site-template`:
    1. __must__ be _between_ `BASE STYLES` and `PROJECT STYLES`
    2. __must only__ be styles that should be available to forks.
3. Styles for forks of `cms-site-template`:
    1. __must__ be _beneath_ `PROJECT STYLES`,
    2. __may__ _append_ to _these_ sections of KSS documentation:
        - [description][kss-desc]
        - [modifiers][kss-mods]

[kss-mods]: https://github.com/kss-node/kss/blob/spec/SPEC.md#the-modifiers
[kss-desc]: https://github.com/kss-node/kss/blob/spec/SPEC.md#the-heading-and-description

## Style Guide

[CSS Style Guide](https://confluence.tacc.utexas.edu/x/ZQALBg)

## Example Styles

```css
/*
Styles Name

Description of the purpose and use case of styles. Use the `Markup:` property to link to sample markup.
The documentation format is [KSS Node](https://github.com/kss-node/kss-node/blob/master/README.md).

Markup: x-stylesheet-name.html

Styleguide __StylesSection__.__StylesName__
*/



/* --- BASE STYLES --- */
/* --- Do NOT edit, unless you are working `cms-site-template`! --- */



.some-selector {
  text-transform: none;
}



/* --- PROJECT STYLES --- */
/* --- Styles for repos that are forks `cms-site-template` go here. --- */



.some-selector {
  color: green;
  text-transform: underline; /* override BASE styles */
}
```
