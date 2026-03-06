## Command Sequences

To only update environment as necessary, or update since uncommon changes:

| | If this changed | Run this command |
| - | - | - |
| 0 | Dockerfile,<br>Python dependencies | `make stop`, `make build`, `make start` |
| 1 | Python models | `docker exec -it core_cms sh -c "python manage.py migrate"` |
| 2 | Node dependencies* | `npm ci` |
| 3 | CSS stylesheets* | `npm run build:css` |
| 4 | Assets e.g.<br><sub>images, stylesheets, JavaScript</sub> | `docker exec -it core_cms sh -c "python manage.py collectstatic --no-input"` |

> [!tip]
> \* If you do not want to use Node locally, then run `docker run --rm -v "$(pwd):/code" -w /code node:18 sh -c "npm ci && npm run build"`
