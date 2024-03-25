# TACC CMS - Stylesheets - Migrations - v3.10 to v3.11

This is a migration:

- from v3.10 with **no** `TACC_CORE_STYLES_VERSION`
- to v3.11 with `TACC_CORE_STYLES_VERSION = `**`2`**

The files are imported from `site_cms/css/build/`.[^1]

Thus, a search for `v3-10_v3-11` will return only this file.

[^1]: That is the only location where CMS can access them. They appear there after `npm run build:css`.
