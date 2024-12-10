# Programmatically Add Groups & Permissions

## Groups & Permissions

**News Writer (Basic)**: To edit/add Blog articles.

**News Writer (Advanced)**: As much as "News Writer (Basic)" **plus** edit/add/delete Blockquotes **plus** add/delete news Categories and Tags.

**Text Editor (Basic)**: To edit textual elements blocks, folders, and files.

**Text Editor (Advanced)**: As much as "Text Editor (Basic)" **plus** add/delete textual elements, folders and files.

**Media Editor (Basic)**: To edit images, videos, thumbnail sizes, and folders.

**Media Editor (Advanced)**: As much as "Media Editor (Basic)" **plus** add/delete images, videos, thumbnail sizes, and folders.

**Grid Editor (Basic)**: To edit layout (Containers, Rows, Columns).

**Grid Editor (Advanced)**: As much as "Grid Editor (Basic)" **plus** add/delete layout (Containers, Rows, Columns).

## Usage

### Set Permissions

1. Login to the CMS admin.
2. Open a shell into the CMS container e.g.
    `docker exec -it core_cms /bin/bash`
3. In the shell, run the group/permission command e.g.
    `python manage.py set_group_perms news_writer_advanced`
4. Open the CMS admin interface e.g.
    [https://localhost:8000/admin/auth/group](https://localhost:8000/admin/auth/group)
5. In the CMS admin, verify group permissions are as you intend.

### Debug a Command

1. Open a shell into the CMS container e.g. `docker exec -it core_cms /bin/bash`.
2. In the shell, open a Python shell i.e. `python`.
3. In the Python shell, run the following commands.

```py
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taccsite_cms.settings")
django.setup()
# any additional debugging code or scripts you want to execute
```

## Develepment

### Create a New Group

1. Duplicate an existing group.
2. Rename the file and group name.
3. Adjust permissions usign existing sets.

### Create a New Permission Set

### via Existing Set in this Code

1. Duplicate an existing `let_*` function in [`util.py`](./util.py).
2. Rename the function. Rewrite its descritpion.
3. Assign the permission set to a relevant group.

### via Existing Group in CMS Admin

#### 1. Get Permissions from HTML

You may **either** download an appropriate `.html` from [Django CMS - Developer Guide - User Permissions / Groups / Roles](https://tacc-main.atlassian.net/wiki/x/egtv) **or**:

1. Using the CMS admin interface, build out the permissions for a group.
2. Using the browser Developer Tools, copy the `<option>`s from the `<select>` that has the permissions you chose.
3. Save those `<options>` to a new blank file.

#### 2. Convert Permissions to Python

Use regex to convert the `<option>`s from HTML to Python Django CMS instructions.

- Find:\
  <sub>(minified HTML)</sub>

  ```regexp
  <option value=".+?" title="([\s\w]+) \| ([\s\w]+) \| ([\s\w]+)">[\s\w]+ \| [\s\w]+ \| [\s\w]+</option>
  ```

  <sub>(unminified HTML)</sub>

  ```regexp
  [\n\s]*<option[\n\s]*value=".+"[\n\s]*title="([\s\w]+) \| ([\s\w]+) \| ([\s\w]+)"[\n\s]*>\n*[\s]*[\s\w]+ \| [\s\w]+ \| [\s\w]+</option>
  ```

- Replace:

    ```text

        add_perm(group, '$1', '$2', '$3')
    ```

## Reference

- [Programmatically create a django group with permissions](https://stackoverflow.com/q/22250352/11817077)
- [Writing custom django-admin commands](https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/)
