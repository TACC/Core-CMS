# TACC CMS - Templates - Snippets - Manual Pattern Library

## Notice

This is a stopgap for swiflty testing modifers on UI patterns.

Automatic pattern library (e.g. [KSS], [etc.]) would be better.

## Purpose

- Allow consistent testing of a UI pattern on any CMS.
- Change a `class` of a UI pattern per snippet instance.

## How it Works

1. A snippet is created that uses one of these `.html`* snippets.
2. That snippet instance sets class names its "HTML" field.
3. The classes are applied to element(s) in the `.content.html`.

## Why Two Templates per Pattern

Each pattern has an `.html` and `.content.html` template.

- `.html` has logic only DjangoCMS can read.
- `.content.html` has logic DjangoCMS __and__ [KSS] can read.
- `.content.html` symlinks to `/taccsite_cms/static/css/src/…`.

[KSS]: https://warpspire.com/kss/
[etc.]: https://confluence.tacc.utexas.edu/x/FADMBQ
