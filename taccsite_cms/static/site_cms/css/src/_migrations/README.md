# TACC CMS - Stylesheets - Migrations

ORGANIZE STYLES HERE!

These folders' styles are only to be imported by other stylesheets.

CMS websites that were migrated from earlier instances may need these styles.

> ⚠ When all old websites are ported and redesigned, this folder may be deleted.

## Rules

1. Folders __must__ include any top-of-file comments from source file.
1. Folders __must__ be [named with appropriate format](#Naming%20Format).
1. Files __should__ [comment on purpose and means of acquisition](#Documentation%20Format).
1. Files __must__ include a top-of-file comments (from source file or by TACC).
1. Files (except this document) __must__ be in a folder.

## Documentation Format

```css
/*
Pre-2020 Django CMS Bootstrap 3.3.7
HOW: https://dev.help.com/some-tool
HOW: Included code that ...
HOW: Included code that ... (because ...) e.g.:
  - ...
HOW: Did NOT incude code that ...
SRC: https://bitbucket.org/taccaci/frontera/src/master/client/css/bootstrap.min.css
*/
```

## Naming Format

| Format | Description |
| :- | :- |
| `A/` | as of old "A"[^1]
| `A_B/` | from old "A" to new "B"[^1]

[^1]: Where "A" and "B" represent a version, or historical state, of the CMS. E.g. `v1_v2/` from Core CMS @ __v1__.N.N (pre-2020) to Core CMS @ __v2__.N.N (2020+).
