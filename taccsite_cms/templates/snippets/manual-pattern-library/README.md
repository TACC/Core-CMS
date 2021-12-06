# TACC CMS - Templates - Snippets - Manual Pattern Library

## Purpose

- Allow any CMS to consistently reproduce UI pattern markup.
- Change a `class` within pattern markup per snippet instance.

## How it Works

1. A snippet is created that uses one of these `.html`* snippets.
2. That snippet instance sets class names its "HTML" field.
3. The classes are applied to element(s) in the `.content.html`.

## Why Two Templates per Pattern

Each pattern has an `.html` and `.content.html` template.

- `.html` has logic only DjangoCMS can read.
- `.content.html` has logic DjangoCMS __and__ [KSS] can read.
- `.content.html` symlinks to `/taccsite_cms/static/css/src/…`.
- [KSS] software auto-builds pattern library using sample markup.

[KSS]: https://warpspire.com/kss/

## Why Manual Pattern Library if [KSS] Auto-Builds?

KSS setup is incomplete. Manual pattern library is a stopgap[^1].

[^1]: The stopgap allows devs to swiftly test new patterns.
