# How to Test

- [CMS Changes](https://github.com/TACC/Core-CMS/wiki/Test-CMS-Changes)
- [Major Changes to CSS](https://github.com/TACC/Core-CMS/wiki/How-to-Test-Major-Changes-to-CSS)
- [CSS Build Output](https://github.com/TACC/Core-CMS/wiki/Test-CSS-Build-Output)
- [Core Styles Version Change](https://github.com/TACC/Core-CMS/wiki/How-to-Test-Core-Styles-Version-Change)
- [Local Poetry Dependencies in Docker](#local-poetry-dependencies-in-docker)

## Local Poetry Dependencies in Docker

When developing a Poetry-managed Python dependency that exists in another repository, you can test changes locally in the CMS Docker environment without needing to commit and push to the remote repository first.

### Prerequisites

- The dependency repository must be cloned locally, typically as a sibling directory to this repository.
- The dependency must be specified in `pyproject.toml` as a git dependency (for build compatibility).

### Steps

1. **Ensure the dependency repository is cloned** at the expected path e.g.

   ```bash
   # From the Core-CMS directory
   ls ../Core-CMS-Plugin-Remote-Content
   ```

2. **Add a volume mount** to the `cms` service in `docker-compose.dev.yml` e.g.

   ```yaml
   volumes:
     - .:/code
     - ../Core-CMS-Plugin-Remote-Content:/code/../Core-CMS-Plugin-Remote-Content
   ```

   > [!NOTE]
   > The volume mount path is relative to the container's `/code` directory, which maps to the repository root.

3. **Modify the command** to install the local dependency at runtime e.g.

   ```yaml
   command: >
     sh -c "
       poetry add ../Core-CMS-Plugin-Remote-Content --editable &&
       python3 manage.py runserver 0.0.0.0:8000
     "
   ```

   > [!NOTE]
   > The `--editable` flag installs the package in development mode, so changes are reflected immediately without reinstalling.

4. **Start the development environment**:
   ```bash
   docker-compose -f docker-compose.dev.yml up
   ```

5. **Make changes** to the dependency repository. Python code changes trigger Django's auto-reload automatically.

6. **After testing, revert the changes** to `docker-compose.dev.yml` to restore the normal configuration.

> [!TIP]
> To test multiple local dependencies, add additional volume mounts and `poetry add` commands in the same pattern.

### Troubleshooting

- [Container Fails to Start: "Path does not exist"](#container-fails-to-start-path-does-not-exist)
- [Changes to the Dependency aren't Reflected](#changes-to-the-dependency-arent-reflected)
- [Build Fails with Path Dependency Error](#build-fails-with-path-dependency-error)

### Container Fails to Start: "Path does not exist"

Ensure the dependency repository is cloned at the expected relative path.

### Changes to the Dependency aren't Reflected

Check that the volume mount path is correct and that the dependency was installed with `--editable` flag. You may need to restart the container.

### Build Fails with Path Dependency Error

Ensure `pyproject.toml` uses a git dependency, not a path dependency. Path dependencies are only used at runtime via `poetry add`.
