# Debug Project

## Start with a Brand New CMS

The `make stop` retains volumes (e.g. database) and images (layers of previous builds).

To start with no volumes, run:
```bash
make stop ARGS="--volumes"
```

To start with no volumes and no images, run:
```bash
make clean
```

## Verify Images Are Collected

1. Review content of `/taccsite_cms/static/site_cms/img`.
2. Verify that content is also _in the container_ at `/static/site_cms/img`.

## Verify CSS Build Output

1. Review content of `/taccsite_cms/static/site_cms/css/build`.
2. Verify that content is also _in the container_ at `/static/site_cms/css/build`.

> **Note**
> You will never see `/static/…/css/src`, because [this app ignores `src/`][ignore-src-dirs] when [collecting static files](#collect-static-files). This is done so templates can **not** load load source files.

[ignore-src-dirs]: https://github.com/TACC/Core-CMS/blob/7b62db1/taccsite_cms/django/contrib/staticfiles_custom/apps.py

## Restart CMS Server

See [How to Restart the CMS Server](https://github.com/TACC/Core-CMS/wiki/How-to-Restart-the-CMS-Server).

## Run Another Local CMS

`docker-compose.dev.yml` fixes container names (`core_cms`, `core_cms_postgres`, …) and port **8000**. To add a second CMS, create a **gitignored** `docker-compose.local-1.yml` and merge it:

```bash
docker compose -f docker-compose.dev.yml -f docker-compose.local-1.yml …
```

### Same Database

**Use case:** Run a second dev server (for example on port **8001**) against the **same** Postgres and Elasticsearch as your usual `make start` stack.

> [!WARNING]
> Both CMS processes share one database. Migrations, test-page commands, and content edits from either server affect the same data. Do not use this for two migration experiments at once.

1. Start the primary stack from this repo (`make start`).
2. In `docker-compose.local-1.yml`:
   - Add a second app service (do not add Postgres or Elasticsearch).
   - Give it a new `container_name` (not `core_cms`).
   - Map host port **8001** to container port **8000**.
   - Mount the other checkout at `/code`.
   - Attach the service to the `core_cms_net` network.
3. Start only that service:

   ```bash
   docker compose -f docker-compose.dev.yml -f docker-compose.local-1.yml up -d <that-service>
   ```

4. Run management commands against the new container, for example `docker exec <that-container> python manage.py migrate`.
5. Open **http://127.0.0.1:8001/**.

### Isolated Database

**Use case:** A separate Postgres volume so you can run migrations or experiments without touching the database behind **http://127.0.0.1:8000/**.

1. In `docker-compose.local-1.yml`, override **CMS**, **Postgres**, and **Elasticsearch** from `docker-compose.dev.yml`:
   - Give each service a **new** `container_name` (none may match `core_cms`, `core_cms_postgres`, or `core_cms_elasticsearch`).
   - Give Postgres a **new** named volume (do not reuse `core_cms_postgres_data`).
   - Use host ports that do not conflict with the primary stack (for example app **8001**, Elasticsearch **9202**).
2. In `taccsite_cms/settings/secrets.py` for the checkout you mount into this stack:
   - Set `DATABASES['default']['HOST']` to the sandbox Postgres `container_name`.
   - Set `ES_HOSTS` to the sandbox Elasticsearch hostname (for example `http://<sandbox-es-container_name>:9200`).
3. Start the sandbox stack:

   ```bash
   docker compose -f docker-compose.dev.yml -f docker-compose.local-1.yml up -d
   ```

4. Initialize the sandbox database (migrate, superuser, `collectstatic`, CSS build as needed—the same steps as [Getting Started](../README.md#getting-started), but use `docker exec` on the **sandbox** CMS container name).
5. Open the sandbox app URL (for example **http://127.0.0.1:8001/**).

## Build Search Index

See [How to Build Search Index](https://github.com/TACC/Core-CMS/wiki/How-to-Build-Search-Index).
