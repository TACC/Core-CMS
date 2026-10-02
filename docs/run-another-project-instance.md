# Run Another Project Instance

The default stack in `docker-compose.dev.yml` uses fixed container names (`core_cms`, `core_cms_postgres`, …) and serves the app on port **8000**. To run another project instance, add a **gitignored** `docker-compose.local-1.yml` and merge it:

```bash
docker compose -f docker-compose.dev.yml -f docker-compose.local-1.yml …
```

## Same Database

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

## Isolated Database

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

## Agent Worktrees

**Use case:** A developer edits one **git worktree** and runs a **dedicated** CMS + Postgres stack—without Elasticsearch and without `make start` collision on port 8000.

> [!IMPORTANT]
> A container serves the checkout its Compose file mounts, not “whatever directory you have open in the editor.” Point **every** bind mount and `build.context` at the **active worktree** using **absolute paths**.

1. Copy the template:

   ```bash
   cp docker-compose.agent.example.yml docker-compose.agent-<label>.yml
   ```

   (`docker-compose.agent-*.yml` is gitignored; keep the file in a checkout you will not delete casually, or copy the label and paths when you switch worktrees.)

2. Edit `docker-compose.agent-<label>.yml` (or export env vars if you use the template as-is):

   - `build.context` and the CMS volume: absolute path to the worktree under test.
   - Unique `AGENT_PORT` / `AGENT_INSTANCE` (container names `core_cms_<instance>`, host port e.g. **8005**).
   - **Do not** add an `elasticsearch` service.

3. In that worktree’s `taccsite_cms/settings/`:

   - Create `secrets.py` from `secrets.example.py` if missing (`HOST` can stay `core_cms_postgres` when the compose file adds that **network alias** on Postgres).
   - Create `settings_custom.py` from `settings_custom.example.py` so `PORTAL_SEARCH_INDEX_IS_AUTOMATIC = False` (page saves do not require Elasticsearch). Site search will not work until you run a stack with ES.

4. Start the stack (example):

   ```bash
   docker compose -f docker-compose.agent-<label>.yml -p cms_<instance> up -d --build
   ```

5. Initialize (use the **sandbox** CMS container name):

   ```bash
   docker exec core_cms_<instance> python manage.py migrate --no-input
   DJANGO_SUPERUSER_PASSWORD=yourpass docker exec -e DJANGO_SUPERUSER_PASSWORD \
     core_cms_<instance> python manage.py createsuperuser --no-input --username admin --email admin@localhost
   docker run --rm -v "<worktree>:/code" -w /code node:20 sh -c "npm ci && npm run build"
   docker exec core_cms_<instance> python manage.py collectstatic --no-input
   ```

6. Open **http://127.0.0.1:<port>/** (for example **http://127.0.0.1:8005/**).

**Repointing:** When you move the instance to another worktree, update paths in the same compose file and run `up -d --build` with the same `-p` project name so the Postgres volume stays attached.

**Before deleting a worktree:** Repoint its compose file to another checkout or `docker compose … down` and archive anything you need from the volume.
