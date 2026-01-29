#!/usr/bin/env bash
# Test whether taccsite_cms.settings (package re-exporting settings.settings) causes circular import.
# Run from repo root: ./test-circular-import.sh
# Uses local python3 if available; if that fails or you prefer container, run with USE_DOCKER=1
# or start the stack and run: docker exec core_cms python3 -c "import taccsite_cms.settings as s; print('DEBUG', s.DEBUG)"

set -e
cd "$(dirname "$0")"

RUN_IN_DOCKER=
if [[ -n "${USE_DOCKER:-}" ]]; then
  RUN_IN_DOCKER=1
elif ! python3 -c "import django" 2>/dev/null; then
  if docker exec core_cms python3 -c "import django" 2>/dev/null; then
    RUN_IN_DOCKER=1
  fi
fi

ROOT="."
run_py() { TEST_SETTINGS_ROOT="$ROOT" python3 -c "$1"; }
if [[ -n "$RUN_IN_DOCKER" ]]; then
  echo "=== Running tests inside container core_cms ==="
  ROOT="/code"
  run_py() { docker exec -e TEST_SETTINGS_ROOT=/code core_cms python3 -c "$1"; }
fi

FAILED=0

echo "=== Test 1: Import taccsite_cms.settings (as Django does) ==="
run_py "
import sys
import os
sys.path.insert(0, os.environ.get('TEST_SETTINGS_ROOT', '.'))
try:
    import taccsite_cms.settings as s
    print('  Import OK')
    if hasattr(s, 'DEBUG'):
        print('  DEBUG:', s.DEBUG)
    else:
        print('  ERROR: No DEBUG attribute')
        sys.exit(1)
    if hasattr(s, 'ALLOWED_HOSTS'):
        print('  ALLOWED_HOSTS:', s.ALLOWED_HOSTS[:2] if s.ALLOWED_HOSTS else [])
    else:
        print('  ERROR: No ALLOWED_HOSTS attribute')
        sys.exit(1)
except ImportError as e:
    if 'circular' in str(e).lower():
        print('  FAIL: Circular import:', e)
        sys.exit(1)
    raise
except Exception as e:
    print('  FAIL:', type(e).__name__, e)
    sys.exit(1)
" 2>&1 || FAILED=1

echo ""
echo "=== Test 2: Import again (second time; catch stale/cached issues) ==="
run_py "
import sys
import os
sys.path.insert(0, os.environ.get('TEST_SETTINGS_ROOT', '.'))
import importlib
import taccsite_cms.settings
importlib.reload(taccsite_cms.settings)
s = taccsite_cms.settings
print('  Re-import OK')
print('  DEBUG:', getattr(s, 'DEBUG', 'MISSING'))
print('  ALLOWED_HOSTS:', getattr(s, 'ALLOWED_HOSTS', 'MISSING')[:2] if getattr(s, 'ALLOWED_HOSTS', None) else 'MISSING')
" 2>&1 || FAILED=1

echo ""
echo "=== Test 3: Django check ==="
if [[ -n "$RUN_IN_DOCKER" ]]; then
  docker exec core_cms python3 manage.py check 2>&1 || FAILED=1
else
  (python3 manage.py check 2>&1) || { echo "  (Django not in path - run USE_DOCKER=1 ./test-circular-import.sh or start stack and use container)"; FAILED=1; }
fi

echo ""
if [[ $FAILED -ne 0 ]]; then
  echo "=== One or more tests failed (e.g. circular import). ==="
  exit 1
fi
echo "=== Done. No circular import detected. ==="
