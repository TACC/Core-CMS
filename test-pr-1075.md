## Testing

### New Path Works

1. `make clean`
2. `make setup`
3. Verify creation of:
    - `taccsite_cms/settings/settings_custom.py`
    - `taccsite_cms/settings/settings_local.py`
    - `taccsite_cms/settings/secrets.py`
4. `make start ARGS=--detach`
5. Open http://localhost:8000/.
6. Confirm site loads with **no** import errors.

### Old Path Still Works (Fallback)

1. Remove or Rename:
  - `taccsite_cms/settings/settings_custom.py`
  - `taccsite_cms/settings/settings_local.py`
  - `taccsite_cms/settings/secrets.py`
2. Create root-level files from examples:
  - `taccsite_cms/settings_custom.py`
  - `taccsite_cms/settings_local.py`
  - `taccsite_cms/secrets.py`
3. `make start ARGS=--detach`
4. Open http://localhost:8000/.
5. Confirm site loads with **no** import errors.
