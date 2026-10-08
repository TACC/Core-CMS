# Page export (DOCX)

[Core-CMS-Plugin-Page-Export](https://github.com/TACC/Core-CMS-Plugin-Page-Export) adds **Download as DOCX…** to the CMS page tree. Export uses the draft **content** placeholder plugin tree (not scraped HTML).

## Install

The plugin is a Poetry dependency (`djangocms-tacc-page-export`) and is listed in `INSTALLED_APPS` as `djangocms_tacc_page_export`. Rebuild the CMS image after changing the plugin (`make build`).

Local monorepo layout: `pyproject.toml` points at `../Core-CMS-Plugin-Page-Export`.

## Settings

| Setting | Default | Purpose |
| --- | --- | --- |
| `CMS_PAGE_EXPORT_PAGE_QUALIFIER` | `None` (all pages) | Callable or dotted path; menu shown only when it returns true |
| `CMS_PAGE_EXPORT_SHOULD_READ_TACCSITE_PLUGINS` | `True` | Register TACC Site Section/Card readers when those apps are installed |

## Manual test

1. `make start` (or your agent compose stack).
2. Page tree → any page → **Download as DOCX…**
3. Confirm; open the `.docx` or `.zip`.

Plugin support matrix: export repo `docs/plugin-support.md`.
