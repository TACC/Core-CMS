# TACC CMS - Templates

All templates specific to the Core CMS __must__ be placed in this directory (or child directories).

## Page Templates

To make certain templates available as page templates for CMS editors, update `CMS_TEMPLATES` setting.

## Overwrite Apps or Plugins

1. Create sub-directory named the same as the Python module directory of the app/plugin.
2. Create a template of the same name as the app/plugin template to overwrite.
3. Replace or extend the content of the overwritten template.

To learn more, see [How to override Django-CMS templates](https://stackoverflow.com/a/39099777/11817077).

### Examples

#### Overwrite the Blog/News Templates

See [`./djangocms_blog`](./djangocms_blog).

#### Overwrite CMS Admin Toolbar

Create `./cms/toolbar/toolbar.html` with content:

```html
<div id="cms-top">King of the mountain.</div>
```
