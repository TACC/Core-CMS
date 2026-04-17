# AGENTS.md

- [Architecture](#architecture)
- [Pull Requests](#pull-requests)

## Architecture

This is a **Docker-based Django CMS** project. All application code runs inside Docker containers.

### Services

| Service | Container | Port |
| --- | --- | --- |
| Django CMS (app) | `core_cms` | `localhost:8000` |
| PostgreSQL 14.9 | `core_cms_postgres` | `5432` (internal) |
| Elasticsearch 7.17 | `core_cms_elasticsearch` | `localhost:9201` |

### Make

Use the `Makefile` instead of raw `docker compose` commands:

| Command | Purpose |
| --- | --- |
| `make setup` | One-command full setup (see caveat below) |
| `make build` | Build Docker images |
| `make start` | Start containers (`ARGS="--detach"` for background) |
| `make stop` | Stop containers |
| `make clean` | Stop containers, remove volumes and images |

### Setup

```sh
DJANGO_SUPERUSER_PASSWORD=yourpass make setup
```

`make setup` (i.e. `bin/setup-cms.sh`) handles: settings file creation, Docker build, container startup, readiness polling, migrations, superuser creation, CSS build, and `collectstatic`. Non-interactive shells (e.g. agent runs) must set `DJANGO_SUPERUSER_PASSWORD`; a TTY prompts interactively.

_Note: Stale containers errors (e.g. `core_cms_elasticsearch already in use`) come from old Compose state. Ask human whether to remove stale `core_cms*` containers/projects; once resolved, rerun `make setup`._

### Dependencies

- When updating dependencies, use `npm` commands (e.g. `uninstall`/`install`); do not hand-edit lockfile entries.
- When installing `@tacc/core-styles`, use a published version from the registry, or a `git+https://github.com/...` spec so install does not require SSH.

### Gotchas

#### Settings & Secrets

- **Settings files** are gitignored. Created from `*.example.py` by `bin/setup-cms.sh` or manually.
- **Postgres secret files:** `docker-compose.dev.yml` mounts `./conf/postgres/*.secret` files. These are not required for development and can be ignored.

#### Elasticsearch

- **`secrets.py` Elasticsearch host:** Should be `core_cms_elasticsearch` (the Docker hostname), not `elasticsearch`.
- Docker commands may need `sudo` depending on the environment.
- **Elasticsearch cgroups v2:** ES 7.17.0 crashes on kernels with cgroups v2 (`CgroupV2Subsystem` NPE). Use ES 7.17.9+ in `docker-compose.dev.yml`.

### Lint, Test, Build

- **Lint:** `docker exec core_cms flake8 taccsite_cms/ --max-line-length=120` (pre-existing warnings expected)
- **Tests:** `docker exec core_cms python manage.py test taccsite_cms.contrib.taccsite_sample --no-input`
- **CSS build:** `docker run --rm -v "$(pwd):/code" -w /code node:18 sh -c "npm ci && npm run build"`
- **Collect static:** `docker exec core_cms python manage.py collectstatic --no-input`

See `README.md` for full setup instructions.

## Pull Requests

Write skimmable, template-aligned PRs; reviewers can see the code diff for details.
