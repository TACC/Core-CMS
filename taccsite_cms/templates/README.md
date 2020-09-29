# TACC CMS - Templates

All templates specific to the Core CMS __must__ be placed in this directory (or child directories).

## Page Templates

To make certain templates available as page templates for CMS editors, update `_CMS_TEMPLATES` secret.

## Overwrite Plugins

To overwrite the templates of any other app (e.g. the `django` CMS, the `djangocms_blog` plugin), add them here _within_ a namespaced directory that has the same structure and file names of the app code. See [How to override Django-CMS templates](https://stackoverflow.com/a/39099777/11817077).

### Examples

#### Overwrite the Blog/News Templates

See [`./djangocms_blog`](./djangocms_blog).

#### Overwrite CMS Admin Toolbar

Create `./cms/toolbar/toolbar.html` with content:

```html
<div id="cms-top">King of the mountain.</div>
```
