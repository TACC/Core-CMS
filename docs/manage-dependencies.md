# Manage Dependencies

This project uses [**uv** (Python)](https://docs.astral.sh/uv/getting-started/installation/) and [**pnpm** (Node)](https://pnpm.io/installation).

1. Add/Update dependencies via Docker* e.g.

    **Python (uv)**

    ```sh
    docker exec -it core_cms sh -c "cd /opt/pysetup && uv ..."
    ```

    **Node (pnpm)**

    ```sh
    docker run --rm -v "$(pwd):/code" -w /code ghcr.io/pnpm/pnpm:12 pnpm ...
    ```

2. Update environment using appropriate [command sequence](./command-sequences.md).

> [!important]
> \* **If** you manage dependencies locally, **then** use the same package manager versions as in [`Dockerfile`](../Dockerfile), **so** lock files stay consistent.

> [!tip]
> You can [test a dependency from a local repository clone](../TESTING.md#local-uv-dependencies-in-docker) without committing or publishing it.
