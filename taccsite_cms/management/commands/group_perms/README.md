# Programmatically Add Groups & Permissions to CMS

## Get Permissions

You may **either** download an appropriate `.html` from [Django CMS - Developer Guide - User Permissions / Groups / Roles](https://confluence.tacc.utexas.edu/x/jrntDg) **or**:

1. Using the CMS admin interface, build out the permissions for a group.
2. Using the browser Developer Tools, copy the `<option>`s from the `<select>` that has the permissions you chose.
3. Save those `<options>` to a new blank file.

## Convert Permissions

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

    model_name = '$2'.lower().replace(' ', '')
    content_type = ContentType.objects.get(app_label='$1', model=model_name)
    group.permissions.add( Permission.objects.get(name='$3', content_type=content_type) )
  ```

## Program Permissions

1. Create a python script in this directory named after the group e.g. `news_writer_advanced.py`.
2. Add this starter code:

    ```py
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    from django.core.management import BaseCommand

    def set_group_perms():
        group, was_created = Group.objects.get_or_create(
          name='__GROUP_NAME__'
        )
    ```

3. Change `__GROUP_NAME__` to the name of the group to add permissions for e.g. `News Writer (Advanced)`.
4. Within the `handle` method, add all the commands from the "Convert Permissions" step.

## Set Permissions

1. Login to the CMS admin.
2. Add a user group named the same as "\_\_GROUP_NAME\_\_". ⚠️
4. Open a shell into the CMS container e.g.
    `docker exec -it core_cms /bin/bash`
4. In the shell, run the group/permission command e.g.
    `python manage.py set_group_perms news_writer_advanced`
5. Open the CMS admin interface e.g.
    [https://localhost:8000/admin](https://localhost:8000/admin)
6. In the CMS admin, verify group permissions are as you intend.

<sub>⚠️ This automatically creates a "User groups (page)" in a way that Django CMS will show it. If you skip this step, you will **not** be able to edit "User groups (page)" permissions (because they will exist, but not be accessible in the CMS admin).</sub>

## Debug Command

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

## Reference

- ["Next Steps" for this feature](https://github.com/TACC/Core-CMS/pull/598#issuecomment-1423258767)
- [Programmatically create a django group with permissions](https://stackoverflow.com/q/22250352/11817077)
- [Writing custom django-admin commands](https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/)
