# TACC CMS - Static Files

All static files _specific to_ the Core CMS __must__ be placed here _within_ `site_cms`.
All static files _shared with_ the Core CMS __must__ be placed here _within_ `site_shared`.

These assets will be served by Django and may be built by Node.

See project `README.md` at ["Static Files"](/README.md#static-files).

## Clarification

The `taccsite_cms` directory isolates all Core resources, while the `site_cms` and `site_shared` directories [namespaces the static files and templates][djangocms-custom-resources].

[djangocms-custom-resources]: https://docs.djangoproject.com/en/2.2/intro/tutorial06/#customize-your-app-s-look-and-feel
