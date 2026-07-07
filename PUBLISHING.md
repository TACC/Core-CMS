# How to Publish

0. Read [Versioning](#versioning).
1. [Create release and tag on GitHub.](https://github.com/TACC/Core-CMS/releases/new)
2. [Build & Deploy](README.md#build--deploy-project) off of the new release tag.

## Versioning

1. Always pre-release `vX.Y.Z-rc1` before a production release `vX.Y.Z`.
2. Does your team need to verify pre-release changes in pre-production?
    - If **yes**, then create the next pre-release e.g. `vX.Y.Z-rc2`, `-rc3`.
    - If **not**, then let them be part of production **release `vX.Y.Z`**.
3. Can your team fix all the pre-release bugs before production release?
    - If **yes**, then — when they are fixed — **release `vX.Y.Z`**.
    - If **not**, then remove the buggy code.
4. If `vX.Y.Z` has still nto been released, then repeat step 2.
