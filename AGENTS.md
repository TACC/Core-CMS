# AGENTS.md

## Cursor Cloud specific instructions

This is a **Docker-based Django CMS** project. All application code runs inside Docker containers.

### Services

| Service | Container | Port |
| --- | --- | --- |
| Django CMS (app) | `core_cms` | `localhost:8000` |
| PostgreSQL 14.9 | `core_cms_postgres` | `5432` (internal) |
| Elasticsearch 7.17 | `core_cms_elasticsearch` | `localhost:9201` |

### Makefile commands

Use the `Makefile` instead of raw `docker compose` commands:

| Command | Purpose |
| --- | --- |
| `make setup` | One-command full setup (see caveat below) |
| `make build` | Build Docker images |
| `make start` | Start containers (`ARGS="--detach"` for background) |
| `make stop` | Stop containers |
| `make clean` | Stop containers, remove volumes and images |

### First-time setup

```sh
DJANGO_SUPERUSER_PASSWORD=yourpass make setup
```

`make setup` (i.e. `bin/setup-cms.sh`) handles: settings file creation, Docker build, container startup, readiness polling, migrations, superuser creation, CSS build, and `collectstatic`. Non-interactive shells must set `DJANGO_SUPERUSER_PASSWORD`; a TTY prompts interactively.

### Key gotchas

- **Settings files** are gitignored. Created from `*.example.py` by `bin/setup-cms.sh` or manually.
- The `secrets.py` Elasticsearch host should be `core_cms_elasticsearch` (the Docker hostname), not `elasticsearch`.
- Docker commands may need `sudo` depending on the environment.
- **Elasticsearch cgroups v2:** ES 7.17.0 crashes on kernels with cgroups v2 (`CgroupV2Subsystem` NPE). Use ES 7.17.9+ in `docker-compose.dev.yml`.
- **uwsgi PEP 517 build failure:** Poetry 1.4.0 fails to build uwsgi in the Docker image. The Dockerfile needs `ENV PIP_NO_BUILD_ISOLATION=1` before `poetry install --no-dev`.
- **Postgres secret files:** `docker-compose.dev.yml` mounts `./conf/postgres/*.secret` files. These are not required for development and can be ignored.

### Lint, test, build

- **Lint:** `docker exec core_cms flake8 taccsite_cms/ --max-line-length=120` (pre-existing warnings expected)
- **Tests:** `docker exec core_cms python manage.py test taccsite_cms.contrib.taccsite_sample --no-input`
- **CSS build:** `docker run --rm -v "$(pwd):/code" -w /code node:18 sh -c "npm ci && npm run build"`
- **Collect static:** `docker exec core_cms python manage.py collectstatic --no-input`

See `README.md` for full setup instructions.
