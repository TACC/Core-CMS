# TACC CMS - Static Files

All static files specific to the Core CMS __must__ be placed here _within_ `site_cms`. Those assets will be served by Django and may be built by Node.

See project `README.md` at ["Changing Static Files"](/README.md#Changing%20Static%20Files) and ["Building Static Files"](/README.md#Building%20Static%20Files).

## Clarification

The `taccsite_cms` directory isloates all Core resources, while the `site_cms` directory [namespaces the static files and templates][djangocms-custom-resources].

[djangocms-custom-resources]: https://docs.djangoproject.com/en/2.2/intro/tutorial06/#customize-your-app-s-look-and-feel
