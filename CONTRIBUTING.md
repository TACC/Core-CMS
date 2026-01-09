# How to Contribute

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

1. Update version:
  - `poetry version N.N.N`
2. Review. Commit. Push.
3. Create release and tag on GitHub.
4. [Build & Deploy](../README.md#build--deploy-project) `main` branch.[^1]

[^1]: So that new CMS image is tagged `latest` and `vN.N.N`.

<!-- Link Aliases -->

[development site]: https://dev.cep.tacc.utexas.edu
[production site]: https://prod.cep.tacc.utexas.edu
