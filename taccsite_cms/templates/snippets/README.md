# TACC CMS - Templates - Snippets

__All__, and __only__, snippet code specific to Core __must__ be placed in this directory. This allows us to version and source control snippet code. Failure to do so will result in snippet code loss upon data loss from database.

_This directory can alleviate danger #1 of [Why a Snippet Is Dangerous](#why-a-snippet-is-dangerous)._

## Important

1. The Core CMS __must not__ use any snippets __for production__. _They __should only__ be for testing._
2. A CMS project __should not__ use any snippets. _They __may only__ be temporarily._
3. A CMS project snippet __must__ be saved into its respective snippets directory, `/code/taccsite_custom/name-of-project/static`.
4. Any snippet file __must__ be kept up to date with its snippet.[^1]

[^1]: For now, maintain snippet source code via internal team process.

## What a Snippet Is

A snippet is a __dangerous__ feature from the plugin [`djangocms-snippet`](https://github.com/divio/djangocms-snippet) which is installed in the CMS.

It allows an authorized CMS user to create a snippet of front-end web code (e.g. CSS, HTML, JS) in the database for use anywhere on the website.

## Why a Snippet Is Dangerous

1. The code is dependent on the (unsynced) database, because it is not under:
    - source/version control
2. The code is independent of any other code control:
    - security
    - dependency management
    - style guide
    - organization
    - linting

## Why a Snippet Is Allowed

1. Support time-sensitive changes to the CMS.[^2]
2. Support ad-hoc changes by designer who codes.[^2]
3. Support ad-hoc testing of changes to the code.[^3]

[^2] This is permitted with the expectation that the snippet code is soon appropriately integrated into the repository.
[^3] See Core snippets for examples.
