# TACC CMS - Locale String Overrides

## Purpose

Overwrite text in the  DjangoCMS admin UI.

## Use Cases

- Use language that matches the vocabulary of our CMS editors.
- Use language that non-technical CMS editors can understand more easily.

## Example

To change the text of the "Publish page changes" button and the description of the "CONTAINER TYPE" field on a Bootstrap Contaienr plugin instance.

1. Create file `/taccsite_cms/locale/en/LC_MESSAGES/django.po`.
2. Add this content to the file:

    ```po
    #: django-cms
    #: cms/cms_toolbars.py:400
    msgid "Publish page changes"
    msgstr "Dragon approves changes"

    #: djangocms-bootstrap
    #: contrib/bootstrap4_grid/models.py:42
    msgid ""
    "Defines if the grid should use fixed width (<code>.container</code>) or "
    "fluid width (<code>.container-fluid</code>)."
    msgstr ""
    "Defines a grid of water magic with fluid and frozen containers. "
    "No animals will be harmed by the creation of this grid."
    ```

3. Enter shell of Docker: `docker exec -it core_cms /bin/bash`.[^1]
4. Build the `.mo` file: `django-admin compilemessages`[^2]
5. Restart the CMS server.[^3]

[^1]: If you are running [CMS and Portal integrated local environment](https://github.com/TACC/Core-CMS/wiki/Locally-Develop-CMS---Portal---Docs), you may need to use `docker exec -it sad_cms /bin/bash` instead.
[^2]: If this is your first time to run such a command, you may need to first install `gettext`: `apt-get install gettext`
[^3]: Locally, restart the `cms` Docker service __or__ run `touch taccsite_cms/settings.py`.
