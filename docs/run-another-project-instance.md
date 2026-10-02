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

## Agent worktrees (isolated, no Elasticsearch)

**Use case:** Edit one **git worktree** and run a dedicated CMS + Postgres stack (no Elasticsearch, no collision with `make start` on port 8000). Copy [`docker-compose.agent.example.yml`](../docker-compose.agent.example.yml) to a gitignored `docker-compose.agent-<port>.yml` in the **main checkout** (so instance metadata survives deleting a worktree).

A container runs whichever checkout its Compose file points at, not the worktree you have open in the editor. Keep all edits in the **active workspace** only—do **not** copy them into another checkout.

**Agents:** Before you rely on an instance, set `build.context` and the CMS bind mount to the **absolute path of the worktree you are editing**, then recreate the CMS container. If an existing `docker-compose.agent-<port>.yml` still points at another path (including a removed worktree), **update those paths yourself** and run `docker compose -f docker-compose.agent-<port>.yml -p cms<port> up -d --build`. Do not ask the user to repoint or report stale paths unless you are blocked. Renaming the compose file is optional; the port in the filename and `-p cms<port>` only identify the instance—**paths** must match your worktree.

- Set `build.context` **and** the CMS bind mount to the active worktree, as **absolute paths**. (`build: .` builds from the main checkout.)
- Use only that worktree bind mount for `/code`. Do **not** add anonymous volumes on `/code/static` or `/code/taccsite_cms/static` (they hide built CSS from the worktree).
- Recreate the container after path edits: `docker compose -f docker-compose.agent-<port>.yml -p cms<port> up -d --build`.
- Keep the same compose file name and `-p cms<port>` when repointing paths, so the Postgres named volume stays attached.
- In that worktree, `taccsite_cms/settings/settings_custom.py` (from `settings_custom.example.py`) with `PORTAL_SEARCH_INDEX_IS_AUTOMATIC = False` so saving a page does not require Elasticsearch.
- Omit the `elasticsearch` service. Postgres hostname in `secrets.py` can stay `core_cms_postgres` when the compose file adds that **network alias** on the agent Postgres service.
- Before deleting a worktree, repoint that instance’s paths to another checkout (or `docker compose … down` if retiring the instance).
