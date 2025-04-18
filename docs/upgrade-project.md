# Upgrade Project

- [from v4.N to v4.14](#from-v4n-to-v414)
- [from v4.N to v4.13](#from-v4n-to-v413)
- [from v4.N to v4.12](#from-v4n-to-v412)
- [from v4.N to v4.7](#from-v4n-to-v47)
- [from v3 to v4](#from-v3-to-v4)
- [from v3.N to v3.12](#from-v3n-to-v312)
- [from v2 to v3](#from-v2-to-v3)

Optional:
- [expected cleanup](#expected-cleanup)

## Expected Cleanup

- [Remove Unnecessary Settings](#remove-unnecessary-settings)
- [Simplify Image Paths](#simplify-image-paths)

### Remove Unnecessary Settings

1. In `taccsite_cms/custom_app_settings.py`, remove apps from `STATICFILES_DIRS`, i.e.

    | | change |
    | - | - |
    | from | `STATICFILES_DIRS = ('apps/custom_example', ...)` |
    | to | `STATICFILES_DIRS = (...)` |

    > **Note**
    > Django automatically identifies the `static` directory for each app.

### Simplify Image Paths

1. Remove any subdirectories of your project's static `img` directory, i.e.

    | | root |
    | - | - |
    | from | `taccsite_custom/static/custom_project_dir/img/*/...` |
    | to | `taccsite_custom/static/custom_project_dir/img/...` |

2. Rename **all** references to the previous image paths e.g.
    - `/custom_project_dir/taccsite_cms/settings_custom.py` [^1]
    - [Core Portal Deployments]:`/project_dir/camino/cms.settings_custom.py` [^1]

[^1]: The `cms.settings_custom.py` is committed in [Core Portal Deployments]. A `settings_custom.py` in [Core CMS Custom] is `.gitignore`'d.

## from v4.N to v4.14

- [Rename `PORTAL_ES_ENABLED` Setting](#rename-portal_es_enabled-settings)
- [Upgrade Docker Compose](#upgrade-docker-compose)

### Rename `PORTAL_ES_ENABLED` Setting

| from | to |
| - | - |
| `PORTAL_ES_ENABLED` | `PORTAL_SEARCH_INDEX_IS_AUTOMATIC` |

### Upgrade Docker Compose

Update to _at least_ the latest Docker Compose v2.

The v1 `docker-compose` command has long been deprecated.

## from v4.N to v4.13

- [Upgrade Custom Branding Setting](#upgrade-custom-logo-setting)

### Upgrade Custom Branding Setting

Refactor the `BRANDING` array to a `PORTAL_BRANDING` dict:

```diff
- NSF_BRANDING = [
-     ...
- ]
-
- TACC_BRANDING = [
-     ...
- ]
-
- UTEXAS_BRANDING = [
-     ...
- ]
-
- CUSTOM_BRANDING = [
-     "portal",
-     "custom-project_cms/img/org_logos/custom-project-logo.png",
-     "",
-     "/",
-     "_self",
-     "Custom Project Logo",
-     "anonymous",
-     "True"
- ]
-
- BRANDING = [ NSF_BRANDING, TACC_BRANDING, UTEXAS_BRANDING, CUSTOM_BRANDING ]
+ from taccsite_cms._settings.branding import *
+
+ CUSTOM_BRANDING = {
+     "is_remote": True,
+     "img_file_src": "https://cdn.jsdelivr.net/gh/TACC/Core-CMS-Custom@______/custom-project_assets/custom-project-logo.png",
+     "img_class": "", # additional class names
+     "link_href": "/",
+     "link_target": "_self",
+     "img_alt_text": "Portal Logo",
+     "img_crossorigin": "anonymous",
+ } # To hide logo, set `PORTAL_LOGO = False`
+
+ PORTAL_BRANDING = [ PORTAL_BRANDING_TACC, PORTAL_BRANDING_UTEXAS ]
```

<details><summary>Map of Array Values to Dict Properties</summary>

| | from Array Value | to Dict Property |
| - | - | - |
| 0 | "portal"                  | (unused value) |
| 1 | "site_cms/.../portal.png" | `"img_file_src"` |
| 2 | ""                        | `"img_class"` |
| 3 | "/"                       | `"link_href"` |
| 4 | "_self"                   | `"link_target"` |
| 5 | "Portal Logo"             | `"img_alt_text"` |
| 6 | "anonymous"               | `"img_crossorigin"` |
| 7 | "True"                    | (whether to show logo) |

</details>

## from v4.N to v4.12

- [Rename Certain Settings](#rename-certain-settings)

### Rename Certain Settings

| from | to |
| - | - |
| `INCLUDES_CORE_PORTAL` | `PORTAL_IS_TACC_CORE_PORTAL` |
| `INCLUDES_PORTAL_NAV` | `PORTAL_HAS_LOGIN` |
| `INCLUDES_SEARCH_BAR` | `PORTAL_HAS_SEARCH` |
| `TACC_BLOG_SHOW_CATEGORIES` | `PORTAL_BLOG_SHOW_CATEGORIES` |
| `TACC_BLOG_SHOW_TAGS` | `PORTAL_BLOG_SHOW_TAGS` |
| `TACC_BLOG_CUSTOM_MEDIA_POST_CATEGORY` | `PORTAL_BLOG_CUSTOM_MEDIA_POST_CATEGORY` |
| `TACC_BLOG_SHOW_ABSTRACT_TAG` | `PORTAL_BLOG_SHOW_ABSTRACT_TAG` |
| `TACC_BLOG_CATEGORY_ORDER` | `PORTAL_BLOG_CATEGORY_ORDER` |
| `TACC_SOCIAL_SHARE_PLATFORMS` | `PORTAL_SOCIAL_SHARE_PLATFORMS` |
| `SEARCH_PATH` | `PORTAL_SEARCH_PATH` |
| `SEARCH_QUERY_PARAM_NAME` | `PORTAL_SEARCH_QUERY_PARAM_NAME` |

## from v4.N to v4.7

- [Update Custom Favicon Setting](#update-custom-favicon-setting)
- [Upgrade Custom Logo Setting](#upgrade-custom-logo-setting)

### Update Custom Favicon Setting

1. Refactor `FAVICON` setting as `PORTAL_FAVICON`.
2. Add a key/value pair to the `PORTAL_FAVICON`.

```diff
- FAVICON = {
-     "img_file_src": "site_cms/img/favicons/favicon.ico"
+ PORTAL_FAVICON = {
+     "img_file_src": "site_cms/img/favicons/favicon.ico",
+     "is_remote": False,
}
```

3. Update use of `FAVICON` to use `PORTAL_FAVICON` ([example](https://github.com/TACC/tup-ui/pull/436/files#diff-7fe664832c1616b48f1b567baa26f1641a1de7e681f93546da5224dbd755eed2L13-R14)).

### Upgrade Custom Logo Setting

Refactor the `LOGO` array to a `PORTAL_LOGO` dict:

```diff
- LOGO = [
-     "portal",
-     "site_cms/img/org_logos/portal.png",
-     "",
-     "/",
-     "_self",
-     "Portal Logo",
-     "anonymous",
-     "True"
- ]
+ PORTAL_LOGO = {
+     "is_remote": False,
+     "img_file_src": "site_cms/img/org_logos/portal.png",
+     "img_class": "", # additional class names
+     "link_href": "/",
+     "link_target": "_self",
+     "img_alt_text": "Portal Logo",
+     "img_crossorigin": "anonymous",
+ } # To hide logo, set `PORTAL_LOGO = False`
```

<details><summary>Map of Array Values to Dict Properties</summary>

| | from Array Value | to Dict Property |
| - | - | - |
| 0 | "portal"                  | (unused value) |
| 1 | "site_cms/.../portal.png" | `"img_file_src"` |
| 2 | ""                        | `"img_class"` |
| 3 | "/"                       | `"link_href"` |
| 4 | "_self"                   | `"link_target"` |
| 5 | "Portal Logo"             | `"img_alt_text"` |
| 6 | "anonymous"               | `"img_crossorigin"` |
| 7 | "True"                    | (whether to show logo) |

</details>

## from v3 to v4

1. Use Postgres is v14.9 or greater. [You may assume all TACC sites do.](https://tacc-main.atlassian.net/wiki/spaces/UP/pages/6659089/Postgres+Upgrade+Testing)
2. Update code that uses [features removed in Django 4](https://docs.djangoproject.com/en/4.2/releases/4.0/#features-removed-in-4-0) e.g.
    - `django.conf.urls.url()`
    - `django.utils.encoding.force_text()`
    - `django.utils.translation.ugettext...`
3. Bookmark [backwards incompatible changes in Django 4](https://docs.djangoproject.com/en/4.2/releases/4.0/#backwards-incompatible-changes-in-4-0).
4. Deploy and test.
    | Given a … | Then … |
    | - | - |
    | Deployed Website | Follow [How To Build & Deploy a CMS Website](https://tacc-main.atlassian.net/wiki/x/2AVv). |
    | Local Instance | Follow [Update Project] instructions. (Assume everything changed.) |

## from v3.N to v3.12

1. [Rename Custom Project Directory](#rename-custom-project-directory)
2. [Redirect Deprecated Templates](#redirect-deprecated-templates)
3. [Deploy And Test](#deploy-and-test)
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
    > The name `custom-project-dir` **must** match the old name as it was, including dashes.

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

    > **Important**
    > The `cms.settings_custom.py` is committed in [Core Portal Deployments], **not** [Core CMS Custom] **nor** [Core CMS Resources].

### Deploy And Test

#### For a Deployed Website

Follow [How To Build & Deploy a CMS Website](https://tacc-main.atlassian.net/wiki/x/2AVv).

#### For a Local Instance

Follow [Update Project] instructions. (Assume everything changed.)

### Clean Up After Deploy

1. Change template of every page on the CMS to **not** use deprecated template.
2. Remove its deprecated templates from repository.

## from v2 to v3

**Undocumented.** Contact a primary contributor for assistance.

<!-- Link Aliases -->

[Update Project]: ../README.md#new-minor-or-patch-version-or-branch

[Core CMS Custom]: https://github.com/TACC/Core-CMS-Custom
[Core CMS Resources]: https://github.com/TACC/Core-CMS-Resources
[Core Portal Deployments]: https://github.com/TACC/Core-Portal-Deployments
