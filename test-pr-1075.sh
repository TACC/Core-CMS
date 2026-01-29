#!/usr/bin/env bash
# Run test.md scenarios and print output so you can see and copy it.
# Run from repo root: bash run-test.sh   (or chmod +x run-test.sh && ./run-test.sh)

set -e
cd "$(dirname "$0")"

echo "=============================================="
echo "Test 1: New path works"
echo "=============================================="

echo ""
echo "--- 1. Stop containers (if running) ---"
make stop || true

echo ""
echo "--- 2. make setup (interactive: you may need to create superuser) ---"
make setup

echo ""
echo "--- 3. Verify creation of settings/ files ---"
for f in taccsite_cms/settings/settings_custom.py taccsite_cms/settings/settings_local.py taccsite_cms/settings/secrets.py; do
  if [ -f "$f" ]; then echo "  OK $f"; else echo "  MISSING $f"; exit 1; fi
done

echo ""
echo "--- 4. Wait and curl http://localhost:8000/ ---"
sleep 5
curl -s -o /dev/null -w "  HTTP %{http_code}\n" http://localhost:8000/ || true

echo ""
echo "--- 5. Container logs (last 30 lines, look for import errors) ---"
docker compose -f docker-compose.dev.yml logs --tail=30 cms 2>&1 || true

echo ""
echo "=============================================="
echo "Test 2: Old path still works (fallback)"
echo "=============================================="

echo ""
echo "--- 1. Stop containers ---"
make stop

echo ""
echo "--- 2. Remove/rename settings/*.py ---"
for f in taccsite_cms/settings/settings_custom.py taccsite_cms/settings/settings_local.py taccsite_cms/settings/secrets.py; do
  [ -f "$f" ] && mv "$f" "$f.bak" && echo "  Renamed $f"
done

echo ""
echo "--- 3. Create root-level files from examples ---"
cp taccsite_cms/settings/settings_custom.example.py taccsite_cms/settings_custom.py
cp taccsite_cms/settings/settings_local.example.py taccsite_cms/settings_local.py
cp taccsite_cms/settings/secrets.example.py taccsite_cms/secrets.py
echo "  Created taccsite_cms/settings_custom.py, settings_local.py, secrets.py"

echo ""
echo "--- 4. Rebuild and start containers (to pick up root-level files) ---"
make build
make start ARGS=--detach

echo ""
echo "--- 5. Wait and curl http://localhost:8000/ ---"
sleep 5
curl -s -o /dev/null -w "  HTTP %{http_code}\n" http://localhost:8000/ || true

echo ""
echo "--- 6. Container logs (last 30 lines, look for import errors) ---"
docker compose -f docker-compose.dev.yml logs --tail=30 cms 2>&1 || true

echo ""
echo "--- Restore: put settings/*.py back, remove root-level copies ---"
for f in settings_custom settings_local secrets; do
  [ -f "taccsite_cms/settings/${f}.py.bak" ] && mv "taccsite_cms/settings/${f}.py.bak" "taccsite_cms/settings/${f}.py"
done
rm -f taccsite_cms/settings_custom.py taccsite_cms/settings_local.py taccsite_cms/secrets.py
echo "  Done."

echo ""
echo "=============================================="
echo "Tests complete. Review output above."
echo "=============================================="
