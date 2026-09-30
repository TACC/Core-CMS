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

## Run another local CMS

`docker-compose.dev.yml` fixes container names (`core_cms`, `core_cms_postgres`, …) and port **8000**. A second stack needs a **gitignored** `docker-compose.agent.yml` merged with `-f docker-compose.dev.yml -f docker-compose.agent.yml`.

### Same database (preview another checkout)

Use when you only need a **second dev server** (e.g. **8001**) against the **existing** Postgres/Elasticsearch. **Warning:** both apps share one DB—`migrate`, test pages, and content edits affect both; not safe for parallel migration experiments.

1. Leave the primary stack running (`make start`).
2. In `docker-compose.agent.yml`, add a **second app service** (new `container_name`, host port **8001**, volume mount to the other checkout, same `core_cms_net` network). Do not start a second Postgres service.
3. `docker compose -f docker-compose.dev.yml -f docker-compose.agent.yml up -d <that-service>`
4. Use `docker exec <that-container> …` and open **http://127.0.0.1:8001/**.

If the app cannot reach Postgres, both stacks may be on different Compose networks (common when Postgres was started from another checkout). Prefer one `make start` from this repo, or attach containers to the same network manually.

### Isolated database (separate migration sandboxes)

Use when you need a **fresh Postgres volume** (e.g. two migration branches at once). Override **Postgres, Elasticsearch, and CMS** in `docker-compose.agent.yml`: new `container_name` for each, new named volumes, and non-conflicting host ports (e.g. app **8001**, ES **9202**). Run `make setup` (or migrate + superuser) against that stack only.

Point `taccsite_cms/settings/secrets.py` at the sandbox DB/ES hostnames (matching your override `container_name` values). The primary stack on **8000** can stay up only if every overridden name and port differs.

## Build Search Index

See [How to Build Search Index](https://github.com/TACC/Core-CMS/wiki/How-to-Build-Search-Index).
