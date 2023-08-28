# Contributing

## Linting and Formatting

Not standardized. Read [(internal) Formatting & Linting](https://confluence.tacc.utexas.edu/x/HoBGCw).

## Best Practices

- [Sign your commits.](https://help.github.com/en/github/authenticating-to-github/managing-commit-signature-verification)
- [Learn Markdown.](https://bitbucket.org/tutorials/markdowndemo)

## Development Workflow

We use a modifed version of [GitFlow](https://datasift.github.io/gitflow/IntroducingGitFlow.html).

- "feature branches" have a specific prefix:
  - `feat/` for features and updates
  - `fix/` for bugfixes and hotfixes
  - `refactor/` for large internal changes
  - `style/` for code style changes (white-space, formatting, etc.)
  - `chore/` for no-op changes
  - `docs/` for documentation
  - `perf/` for performance improvements
  - `test/` for test case updates
  - or other "types" from [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#summary)
- "develop" branch is usually `main`,\
    <sup>but can exist as a long-lived multi-feature branch prefixed with `dev/`</sup>
- "release branches" (as needed) are prefixed with `release/`
- "hotfix branches" are prefixed `fix/`
- "master branch" is always `main`

Our [development site] is always up-to-date with `main` branch.

> **Note**
> The [development site] is only accessible behind the TACC Network.

Our [production site] is built from a specific commit.

## Release Workflow

Only appointed team members may release versions.

1. Create new branch for version bump.
1. Update `CHANGELOG.md`.
1. Update version via:\
  `npm version N.N.N`
1. Commit, push, PR, review, merge.
1. Create release and tag on GitHub.
1. Annotate Github's tag:\
  `bin/annotate-tag.sh vN.N.N`\
  (where `N.N.N` is the version tag)
1. Overwrite remote tag with annotated one:\
  `git push --tags --force`

<!-- Link Aliases -->

[development site]: https://dev.cep.tacc.utexas.edu
[production site]: https://prod.cep.tacc.utexas.edu
