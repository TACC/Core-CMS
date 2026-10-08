# Page export (DOCX)

[Core-CMS-Plugin-Page-Export](https://github.com/TACC/Core-CMS-Plugin-Page-Export) adds **Download…** to the CMS page tree. Export uses the draft **content** placeholder plugin tree (not scraped HTML).

## Install

The plugin is a Poetry dependency (`djangocms-tacc-page-export`) and is listed in `INSTALLED_APPS` as `djangocms_tacc_page_export`. Rebuild the CMS image after changing the plugin (`make build`).

The plugin is installed from Git at tag **`v0.1.0`** (`pyproject.toml` / `poetry.lock`), same pattern as other `djangocms-tacc-*` packages. Rebuild the image after bumping the tag.

## Settings

| Setting | Default | Purpose |
| --- | --- | --- |
| `CMS_PAGE_EXPORT_SHOULD_READ_TACCSITE_PLUGINS` | `True` | Register TACC Site Section/Card readers when those apps are installed |

## Permissions

Only **superusers** and **staff users who can edit a page** can export that page’s draft content (toolbar **Download**, page-tree **Download…**, and the export admin URL). Staff without edit access on a page do not get the actions and are denied on direct URL access.

## Manual test

1. `make start` (or your agent compose stack).
2. Optional fixture page (all supported plugin types):

   ```sh
   docker exec core_cms python manage.py create_test_page_export_plugins --replace
   ```

   Opens at `/test/test-page-export/`.
3. Page tree or toolbar **Download** on that page (or any editable page).
4. Open the `.docx` (or choose scope and download when the page has children).

Plugin support matrix: export repo `docs/plugin-support.md`.
