# How to Publish

0. Read [Versioning](#versioning).
1. [Create release and tag on GitHub.](https://github.com/TACC/Core-CMS/releases/new)
2. [Build & Deploy](README.md#build--deploy-project) off of the new release tag.

## Build & Push

### GitHub Actions

Push to `main` or run **Build** (`workflow_dispatch`). Image tags: `<short-sha>`, sanitized `<branch>`, and `latest`.

The workflow mirrors [Core-CMS-Template](https://github.com/TACC/Core-CMS-Template/blob/main/.github/workflows/build.yml) and local `make build-full` (`production` target, `BUILD_ID` build-arg).

Repo secrets: `DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN` (same as [other Core-CMS-Template projects](https://github.com/topics/tacc-core-cms-template)).

### Local

```sh
make build-full
make publish          # optional: make publish-latest
```

## Versioning

1. Always pre-release `vX.Y.Z-rc1` before a production release `vX.Y.Z`.
2. Does your team need to verify changes in pre-production?
    - If **yes**, then create the next pre-release e.g. `vX.Y.Z-rc2`, `-rc3`.
    - If **not**, then let the changes be part of production **release `vX.Y.Z`**.
3. Can your team fix all the pre-release bugs before production release?
    - If **yes**, then — when they are fixed — **release `vX.Y.Z`**.
    - If **not**, then remove the buggy code.
4. If `vX.Y.Z` has _still **not**_ been released, then repeat step 2.
