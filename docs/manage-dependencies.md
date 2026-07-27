# Manage Dependencies

This project uses [**Poetry** (Python)](https://python-poetry.org/docs/managing-dependencies/) and [**NPM** (Node)](https://docs.npmjs.com/cli/v8/using-npm/developers#specifying-packages).

1. Add/Update dependencies via Docker* e.g.

    **Python (Poetry)**

    ```sh
    docker exec -it core_cms sh -c "cd /code && poetry ..."
    ```

    **Node (NPM)**

    ```sh
    docker run --rm -v "$(pwd):/code" -w /code node:20 npm ...
    ```

2. Update environment using appropriate [command sequence](./command-sequences.md).

> [!important]
> \* **If** you manage dependencies locally, **then** use the same package manager versions as in [`Dockerfile`](../Dockerfile), **so** lock files stay consistent.

> [!tip]
> You can [test a dependency from a local repository clone](../TESTING.md#local-poetry-dependencies-in-docker) without committing or publishing it.
