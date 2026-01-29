#!/usr/bin/env bash
# Debug script to check what's happening with settings imports

set -e
cd "$(dirname "$0")"

echo "=== 1. Check if settings_local.py exists on host ==="
ls -la taccsite_cms/settings/settings_local.py 2>&1 || echo "FILE NOT FOUND ON HOST"

echo ""
echo "=== 2. Create it if missing ==="
if [ ! -f "taccsite_cms/settings/settings_local.py" ]; then
  cp taccsite_cms/settings/settings_local.example.py taccsite_cms/settings/settings_local.py
  echo "Created settings_local.py from example"
else
  echo "settings_local.py already exists"
fi

echo ""
echo "=== 3. Stop containers ==="
make stop || true

echo ""
echo "=== 3b. Test import in a one-off container (to see actual error) ==="
docker compose -f docker-compose.dev.yml run --rm --no-deps cms python3 -c "
import sys
sys.path.insert(0, '/code')
try:
    import taccsite_cms.settings
    print('SUCCESS: Imported taccsite_cms.settings')
    print('DEBUG:', taccsite_cms.settings.DEBUG)
    print('ALLOWED_HOSTS:', taccsite_cms.settings.ALLOWED_HOSTS)
except Exception as e:
    print('FAILED:', type(e).__name__)
    import traceback
    traceback.print_exc()
" 2>&1

echo ""
echo "=== 3c. Start container normally ==="
make start ARGS=--detach

echo ""
echo "=== 3a. Wait for containers to be ready (like setup-cms.sh) ==="
for i in {1..30}; do
  if docker ps | grep -q "core_cms" && docker ps | grep -q "core_cms_postgres" && docker ps | grep -q "core_cms_elasticsearch"; then
    echo "  Containers are running (attempt $i)"
    break
  fi
  if [ $i -eq 30 ]; then
    echo "  ERROR: Containers failed to start after 30 seconds"
    echo ""
    echo "=== Container status ==="
    docker compose -f docker-compose.dev.yml ps
    echo ""
    echo "=== Container logs (cms) ==="
    docker compose -f docker-compose.dev.yml logs --tail=50 cms 2>&1 || true
    exit 1
  fi
  sleep 1
done

echo ""
echo "=== 3b. Check container status ==="
docker compose -f docker-compose.dev.yml ps cms

echo ""
echo "=== 3c. Wait a moment for logs to flush, then check container logs ==="
sleep 2
docker compose -f docker-compose.dev.yml logs --tail=100 cms 2>&1 || true

echo ""
echo "=== 3d. Check if container is still running ==="
if docker ps | grep -q "core_cms"; then
  echo "  Container is still running"
else
  echo "  Container has crashed - checking exit status"
  docker ps -a | grep core_cms
fi

echo ""
echo "=== 4. Check if file exists in container (if still running) ==="
if docker ps | grep -q "core_cms"; then
  docker exec core_cms ls -la /code/taccsite_cms/settings/settings_local.py 2>&1 || echo "FILE NOT FOUND IN CONTAINER"
else
  echo "  Container not running, cannot check file"
fi

echo ""
echo "=== 5. Test import in container (if still running) ==="
if docker ps | grep -q "core_cms"; then
  docker exec core_cms python manage.py shell -c "
import sys
print('Python path:', sys.path[:3])
try:
    from taccsite_cms.settings.settings_local import *
    print('SUCCESS: Imported from taccsite_cms.settings.settings_local')
    print('DEBUG from import:', DEBUG if 'DEBUG' in dir() else 'NOT SET')
    print('ALLOWED_HOSTS from import:', ALLOWED_HOSTS if 'ALLOWED_HOSTS' in dir() else 'NOT SET')
except Exception as e:
    print('FAILED:', type(e).__name__, str(e))
    try:
        from taccsite_cms.settings_local import *
        print('FALLBACK SUCCESS: Imported from taccsite_cms.settings_local')
    except Exception as e2:
        print('FALLBACK FAILED:', type(e2).__name__, str(e2))
" 2>&1 || echo "Cannot exec into container - it has crashed"
else
  echo "  Container not running, cannot test import"
fi

echo ""
echo "=== 6. Check Django settings (what Django actually sees) - if container running ==="
if docker ps | grep -q "core_cms"; then
  docker exec core_cms python manage.py shell -c "
from django.conf import settings
print('Django DEBUG:', settings.DEBUG)
print('Django ALLOWED_HOSTS:', settings.ALLOWED_HOSTS)
import os
env_debug = os.environ.get('DEBUG')
env_hosts = os.environ.get('ALLOWED_HOSTS')
if env_debug:
    print('ENV DEBUG:', env_debug)
if env_hosts:
    print('ENV ALLOWED_HOSTS:', env_hosts)
" 2>&1 || echo "Cannot exec into container - it has crashed"
else
  echo "  Container not running, cannot check Django settings"
  echo ""
  echo "=== 6b. Since container crashed, let's check what might be wrong ==="
  echo "Checking if there's a syntax error in settings files..."
  python3 -m py_compile taccsite_cms/settings.py 2>&1 || echo "Syntax error in settings.py"
  python3 -m py_compile taccsite_cms/settings/settings_local.py 2>&1 || echo "Syntax error in settings_local.py"
fi
