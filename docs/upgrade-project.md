# Upgrade Project

## Table of Contents

- [from v3 to v4](#from-v3-to-v4)
- [from v3.N to v3.12](#from-v3n-to-v312)
- [from v2 to v3](#from-v2-to-v3)

## from v3 to v4

1. Upgrade your CMS database to Postgres v14.9.
2. Update code that uses [features removed in Django 4](https://docs.djangoproject.com/en/4.2/releases/4.0/#features-removed-in-4-0) e.g.
    - `django.conf.urls.url()`
    - `django.utils.encoding.force_text()`
    - `django.utils.translation.ugettext...`
3. Bookmark [backwards incompatible changes in Django 4](https://docs.djangoproject.com/en/4.2/releases/4.0/#backwards-incompatible-changes-in-4-0).
4. [Update Project] (Assume everything changed.)

## from v3.N to v3.12

1. [Rename Custom Project Directory](#rename-custom-project-directory)
2. [Redirect Deprecated Templates](#redirect-deprecated-templates)
3. [Update Project For Deploy](#update-project-for-deploy)
4. [Clean Up After Deploy](#clean-up-after-deploy)

### Rename Custom Project Directory

**If** your custom project directory name has dashes, e.g.

`taccsite_custom/custom-project-dir`

**Then**:

1. Rename all `custom-project-dir` directories to `custom_project_dir`.
2. Update all `custom-project-dir` references to `custom_project_dir`.

> **Important**
> A custom project directory name is a Django application. A Django application name must be "a valid Python identifier".

### Redirect Deprecated Templates

**If** your custom project directory has any `templates/*.html` e.g.

- `taccsite_custom/custom_project_dir/templates/standard.html`
- `taccsite_custom/custom_project_dir/templates/fullwidth.html`
- `taccsite_custom/custom_project_dir/templates/home.html`

**Then**:

1. Copy the templates to become deprecated templates:
    - from `custom_project_dir/templates`
    - to `custom-project-dir/templates`

    > **Warning**
    > The name `custom_project_dir` **must** match the old name as it was, including dashes.

2. Edit the deprecated templates to extend the new templates e.g.

    ```django
    {% extends "custom_project_dir/templates/standard.html" %}
    ```

3. Update `settings_custom.py` to support deprecated templates:

    ```diff
        ('custom_project_dir/templates/standard.html', 'Standard'),
        ('custom_project_dir/templates/fullwidth.html', 'Full Width'),
    +   ('custom-project-dir/templates/standard.html', 'DEPRECATED Standard'),
    +   ('custom-project-dir/templates/fullwidth.html', 'DEPRECATED Full Width'),
    ```

### Update Project For Deploy

Follow [Update Project] instrcutions. (Assume everything changed.)

### Clean Up After Deploy

1. Change template of every page on project to **not** use deprecated template.
2. Remove its deprecated templates from repository.

## from v2 to v3

**Undocumented.** Contact a primary contributor for assistance.

<!-- Link Aliases -->

[Update Project]: ../README.md#new-minor-or-patch-version-or-branch
