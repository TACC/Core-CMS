# Styles & Scripts

## Table of Contents

- [For **All** Pages](#for-all-pages)
- [For **Multiple** Pages](#for-multiple-pages)
- [For **One** Page](#for-one-page)

### For All Pages

1. Create asset (if not a remote asset):

    | of this type | in this directory |
    | - | - |
    | stylesheet | `taccsite_cms/static/site_cms/css/src/` |
    | script | `taccsite_cms/static/site_cms/js/modules/` |

2. Load asset:

    | of this type | in this file |
    | - | - |
    | stylesheet | `taccsite_cms/static/site_cms/css/src/core-cms.css` |
    | script | `taccsite_cms/templates/assets_core_delayed.html` |

### For Multiple Pages

1. Create asset:

    | of this type | in this directory |
    | - | - |
    | stylesheet | `taccsite_cms/static/site_cms/css/src/` |
    | script | `taccsite_cms/static/site_cms/js/modules/` |

2. Load asset:

    - either **before** content

      ```html
      {% block assets_custom %}
        {{ block.super }}
        <!-- ... -->
      {% endblock assets_custom %}
      ```

      <details><summary>for entire <strong>site</strong></summary>

      ```html
        <link rel="stylesheet" href="{% static '__PROJECT__/css/build/site.css' %}">
        <script src="{% static '__PROJECT__/js/site.js' %}"></script>
      ```

      </details>

      <details><summary>for one <strong>template</strong></summary>

      ```html
        <link rel="stylesheet" href="{% static '__PROJECT__/css/build/template.___.css' %}">
        <script src="{% static '__PROJECT__/js/template.___.js' %}"></script>
      ```

      </details>

      <details><summary>for one <strong>page</strong></summary>

      > **Warning**
      > Undesired. Create re-usable code (see [CMS UI Organization]).

      </details>

    - or **after** content

      ```html
      {% block assets_custom_delayed %}
        {{ block.super }}
        <!-- ... -->
      {% endblock assets_custom_delayed %}
      ```

      <details><summary>for entire <strong>site</strong></summary>

      ```html
        <link rel="stylesheet" href="{% static '__PROJECT__/css/build/site.css' %}">
        <script src="{% static '__PROJECT__/js/site.js' %}"></script>
      ```

      </details>

      <details><summary>for one <strong>template</strong></summary>

      ```html
        <link rel="stylesheet" href="{% static '__PROJECT__/css/build/template.___.css' %}">
        <script src="{% static '__PROJECT__/js/template.___.js' %}"></script>
      ```

      </details>

      <details><summary>for one <strong>page</strong></summary>

      > **Warning**
      > Undesired. Create re-usable code. See [CMS UI Organization].

      </details>

### For One Page

> **Warning**
> Undesired. Create re-usable code. See [CMS UI Organization].

- [For Markup Outside The Template](#for-markup-outside-the-template)
- [For Markup Inside The Template](#for-markup-inside-the-template)

#### For Markup Outside The Template

##### Styles

```html
{% block css %}
  {{ block.super }}
  <style>
  /* ... */
  </style>
{% endblock css %}
```

> **Note**
> Loads **before** all markup.

##### Script

```html
{% block js %}
  {{ block.super }}
  <script type="module">
  /* ... */
  </script>
{% endblock js %}
```

> **Note**
> Loads **after** all markup.


#### For Markup Inside The Template

##### Styles

```html
<style>
/* ... */
</style>
```

##### Script

```html
<script type="module">
/* ... */
</script>
```

<!-- Link Aliases -->

[Core Styles]: https://github.com/TACC/Core-Styles

[CMS UI Organization]: https://confluence.tacc.utexas.edu/x/54AZCg "CMS UI - Organization"
