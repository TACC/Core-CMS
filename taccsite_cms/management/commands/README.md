# TACC CMS - Management Commands

- [How to Use](#how-to-use)
- [List Pages Using Each Template](#list-pages-using-each-template)
- [Set Groups & Permissions](#set-groups--permissions)
- [Reference](#reference)

## How to Use

1. Open a shell into the CMS container e.g.
    ```sh
    docker exec -it core_cms /bin/bash
    ```
2. In the shell, run any available command e.g.
    ```sh
    python manage.py filename_of_the_command
    ```

## List Pages Using Each Template

This command lists all pages using each template in the CMS, along with their full URLs.

Usage:
```sh
python manage.py list_page_templates
```

## Set Groups & Permissions

Every file in [`group_perms/`](./group_perms) represents a group. Each group's intended usage is described at the top of its file. Permissions are set via function calls in each file.[^1]

- [Usage](#usage)
- [Development](#development)

### Usage

- [Add a Permissions Group](#add-a-permissions-group)
- [Debug a Command](#debug-a-command)
- [Assign Permissions to a User](#assign-permissions-to-a-user)

#### Add a Permissions Group

1. Run the command e.g.
    ```sh
    python manage.py set_group_perms news_writer_advanced grid_editor_basic
    ```
2. Open the CMS admin interface e.g.
    [https://localhost:8000/admin/auth/group](https://localhost:8000/admin/auth/group)
3. Verify group permissions are as you intend.

> **Note:** If group does not exist, this will **create** it. If group exists, this will **add** permissions to it, but will **not remove** permissions from it.

#### Debug a Command

1. Open a Python shell i.e.
    ```sh
    python
    ```
2. In the Python shell, run the following commands.
    ```py
    import os
    import django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taccsite_cms.settings")
    django.setup()
    ```
3. Then run any additional debugging code or scripts you want to execute.

#### Assign Permissions to a User

Add the User to one or more groups.[^1]

> **Warning:**
> If [`CMS_PERMISSION = True`](https://docs.django-cms.org/en/3.11.8/topics/permissions.html#permission-modes) ([default for Core-CMS](https://github.com/TACC/Core-CMS/blob/v4.21.0/taccsite_cms/settings.py#L164)), then assigning one of these groups to a user is **not enough** to allow them to edit a page. You must also give that user [Global or per-page permissions](https://docs.django-cms.org/en/3.11.8/topics/permissions.html#global-and-per-page-permissions); do so [via a group](https://docs.django-cms.org/en/3.11.8/topics/permissions.html#use-permissions-on-groups-not-on-users).

### Development

- [Create a New Group](#create-a-new-group)
- [Create a New Permission Set](#create-a-new-permission-set)
    - [via Existing Set in this Code](#via-existing-set-in-this-code)
    - [via Existing Group in CMS Admin](#via-existing-group-in-cms-admin)
- [Update all CMS Instances](#update-all-cms-instances)

#### Create a New Group

1. Duplicate an existing group.
2. Rename the file and group name. Rewrite file description.
3. Adjust permissions using existing sets.

#### Create a New Permission Set

##### via Existing Set in this Code

1. Duplicate an existing `let_*` function in [`util.py`](./util.py).
2. Rename the function. Rewrite its description.
3. Assign the permission set to a relevant group.

##### via Existing Group in CMS Admin

###### 1. Get Permissions from HTML

You may **either** download an appropriate `.html` from [Django CMS - Developer Guide - User Permissions / Groups / Roles](https://tacc-main.atlassian.net/wiki/x/egtv) **or**:

1. Using the CMS admin interface, build out the permissions for a group.
2. Using the browser Developer Tools, copy the `<option>`s from the `<select>` that has the permissions you chose.
3. Save those `<options>` to a new blank file.

###### 2. Convert Permissions to Python

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

#### Update all CMS Instances

Add new (reversible) migration file to `taccsite_cms/migrations`.

##### Examples

<details><summary>Add New Permission to Existing Group</summary>

`add_new_perm_to_existing_group.py`
```py
from django.db import migrations

def add_new_perm_in_existing_group(apps, schema_editor):
    group = Group.objects.get(name='Your Group Name')
    add_perm(group, 'the app label', 'the model name', 'The permission name')

def del_new_perm_in_existing_group(apps, schema_editor):
    group = Group.objects.get(name='Your Group Name')
    del_perm(group, 'the app label', 'the model name', 'The permission name')

class Migration(migrations.Migration):

    dependencies = [
        ('taccsite_cms', '0001_add_groups.py'), # most recent migration
    ]

    operations = [
        migrations.RunPython(
            add_new_perm_to_existing_group,
            reverse_code=del_new_perm_in_existing_group
        ),
    ]
```

</details>

<details><summary>Add New Groups</summary>

`add_new_groups.py`:
```py
from django.db import migrations

def add_new_groups(apps, schema_editor):
    from taccsite_cms.management.commands.group_perms.new_group_basic import set_group_perms as add_new_group_basic
    from taccsite_cms.management.commands.group_perms.new_group_advanced import set_group_perms as add_new_group_advanced

    add_new_group_basic()
    add_new_group_advanced()

def del_new_groups(apps, schema_editor):
    from taccsite_cms.management.commands.group_perms.new_group_basic import GROUP_NAME as new_group_basic_group_name
    from taccsite_cms.management.commands.group_perms.new_group_advanced import GROUP_NAME as new_group_advanced_group_name

    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name=new_group_basic_group_name).delete()
    Group.objects.filter(name=new_group_advanced_group_name).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('taccsite_cms', '0002_add_new_perm_to_existing_group.py'), # most recent migration
    ]

    operations = [
        migrations.RunPython(add_new_groups, reverse_code=del_new_groups),
    ]
```
</details>

<details><summary>Delete a Group</summary>

`del_group.py`:
```py
from django.db import migrations

def del_group(apps, schema_editor):
    from taccsite_cms.management.commands.group_perms.media_editor_advanced import GROUP_NAME as media_editor_advanced_group_name

    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name=media_editor_advanced_group_name).delete()

def add_group(apps, schema_editor):
    from taccsite_cms.management.commands.group_perms.media_editor_advanced import set_group_perms as add_media_editor_advanced

    add_media_editor_advanced()

class Migration(migrations.Migration):

    dependencies = [
        ('taccsite_cms', '0003_add_new_groups.py'), # most recent migration
    ]

    operations = [
        migrations.RunPython(del_group, reverse_code=add_group),
    ]
```

</details>

## Reference

- [Programmatically create a django group with permissions](https://stackoverflow.com/q/22250352/11817077)
- [Writing custom django-admin commands](https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/)

[^1]: Groups that end in "(Advanced)" include the permissions of the corresponding "(Basic)" group.
