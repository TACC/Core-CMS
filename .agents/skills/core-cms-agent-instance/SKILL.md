---
name: core-cms-agent-instance
description: >-
  Stand up or repoint a dedicated Core-CMS Docker agent instance on a git
  worktree (port-named directory, compose file, Compose project). Use for
  Core-CMS, Core-CMS-Port, Core-CMS-Template, or other Core-CMS-family repos
  when the user wants another local port (e.g. 8001–8005), a PR branch on that
  instance, or work isolated from the main checkout.
---

# Core-CMS Agent Instance

Worktree and Docker setup for a dedicated local port.

Docker and volume rules: [Core-CMS AGENTS.md — Git Worktrees and Docker](../../../AGENTS.md#git-worktrees-and-docker).

Branch prefixes and workflow: [Core-CMS CONTRIBUTING.md — Development Workflow](https://github.com/TACC/Core-CMS/blob/main/CONTRIBUTING.md#development-workflow). Do not invent prefixes (e.g. `ai/`, `cursor/`) outside those which that doc defines.

## Naming

Keep these aligned:

| Thing | Pattern | Example |
| --- | --- | --- |
| Worktree Directory Basename | `<port>` | `8002` |
| Compose File (Main Checkout Only) | `docker-compose.agent-<port>.yml` in the same directory as `docker-compose.dev.yml` | `docker-compose.agent-8002.yml` |
| Compose Project | `-p cms<port>` | `-p cms8002` |
| CMS Container | `core_cms_<port>` | `core_cms_8002` |
| Postgres Container | `core_cms_postgres_<port>` | `core_cms_postgres_8002` |
| URL | `http://127.0.0.1:<port>/` | `http://127.0.0.1:8002/` |

Use one worktree per instance; its **basename** should match the port. The worktree may live wherever your tooling puts it. **Active code** for that instance lives in that worktree—not in another checkout for the same port.

**Main repo checkout** (not the port worktree) holds `.gitignore`d agent compose files so you can see which worktree each port uses and remove worktrees without losing compose definitions.

## Branch From PR Vs New Task Branch

**Existing PR**

1. From the repo root: `gh pr view <n> --json headRefName,title,url` (or the equivalent for your host).
2. In the **port worktree**: `git fetch origin <headRefName> && git checkout <headRefName>`.

**New work (no PR yet)**

1. Pick a CONTRIBUTING prefix and slug (e.g. `feat/blog-filer-folder-hierarchy`).
2. From the main checkout:  
   `git worktree add <path>/<port> -b <prefix>/<slug> origin/<base>`  
   Stack on another branch by checking out from that head inside the worktree when needed.

Open the **port worktree** as the agent workspace when doing instance work.

## Compose File

- If `docker-compose.agent-<port>.yml` is missing in the **main checkout**, copy [`docker-compose.agent.example.yml`](../../../docker-compose.agent.example.yml) (or an existing `docker-compose.agent-*.yml` next to this repo’s `docker-compose.dev.yml`) and replace **every** absolute path: `build.context`, bind mounts under the active worktree, and `127.0.0.1:<port>:8000`.
- Keep the compose file in the **main checkout** in the same directory as `docker-compose.dev.yml`, even when the worktree path is elsewhere.
- Some client repos bind `settings_custom.py` or other settings from shared deploy repos (for example NAIRR via [Core-Portal-Deployments](https://github.com/TACC/Core-Portal-Deployments)). Read that client’s AGENTS.md and site docs when present; follow those mounts so agent instances match production when instructions exist.

## Start Or Repoint Instance

From the **main checkout** directory that contains this repo’s `docker-compose.dev.yml`:

```bash
docker compose -f docker-compose.agent-<port>.yml -p cms<port> up -d --build
```

Re-run after any compose path change so mounts refresh (stale mounts often show another worktree in `docker inspect`).

## Verify

Required before calling setup done:

1. **Mounts** — Bind mounts match the active worktree (and any external paths your repo documents):

   Compare each bind mount’s **host path** from `docker inspect` to the absolute paths in `docker-compose.agent-<port>.yml`. Paths meant to come from the port worktree must sit under that worktree’s directory, not an old or removed checkout. External paths (for example shared deploy settings) must match what the client repo documents.

   ```bash
   # container path <- host path
   docker inspect core_cms_<port> --format '{{range .Mounts}}{{.Destination}} <- {{.Source}}{{"\n"}}{{end}}'
   ```

2. **HTTP** — after a few seconds: `curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:<port>/` → `200` (or expected redirect).

3. **Branch** — in the worktree: `git branch --show-current` matches the PR head or task branch.

## Retire Or Move

Before deleting a worktree, ask whether to: (A) repoint that port’s compose paths to another checkout, (B) take down the instance (`docker compose -f docker-compose.agent-<port>.yml -p cms<port> down`), or (C) something else.
