# Programmatically Add Groups & Permissions to CMS

## Get Permissions

You may **either** download an appropriate `.html` from [Django CMS - Developer Guide - User Permissions / Groups / Roles](https://confluence.tacc.utexas.edu/x/jrntDg) **or**:

1. Using the CMS admin interface, build out the permissions for a group.
2. Using the browser Developer Tools, copy the `<option>`s from the `<select>` that ahs the permissions you chose.
3. Save those `<options>` to a new blank file.

## Convert Permissions

Use regex to convert the `<option>`s from HTML to Python Django CMS instructions.

- Find:

  ```regexp
  [\n\s]*<option[\n\s]*value=".+"[\n\s]*title="[\s\w]+ \| [\s\w]+ \| ([\s\w]+)"[\n\s]*>\n[\s]*[\s\w]+ \| [\s\w]+ \| [\s\w]+</option>
  ```

- Replace:

  ```text
  group.permissions.add( Permission.objects.get(name='$1') )\n
  ```

## Program Permissions

1. Create a python script in this directory named after the group e.g. `news_writer_advanced.py`.
2. Add this starter code:

   ```py
   from django.contrib.auth.models import Group, Permission
   from django.core.management import BaseCommand

   def set_group_perms():
       group, was_created = Group.objects.get_or_create(
         name='__GROUP_NAME__'
       )
   ```

3. Change `__GROUP_NAME__` to the name of the group to add permissions for e.g. `News Writer (Advanced)`.
4. Within the `handle` method, add all the commands from the "Convert Permissions" step.

## Set Permissions

1. Open a shell into the CMS container e.g. `docker exec -it core_cms /bin/bash`.
2. In the shell, run the group/permission command e.g. `python manage.py set_group_perms news_writer_advanced`.
3. Open the CMS admin interface e.g. [https://localhost:8000/admin](https://localhost:8000/admin).
4. In the CMS admin, verify group permissions are as you intend.

## Debug Command

1. Open a shell into the CMS container e.g. `docker exec -it core_cms /bin/bash`.
2. In the shell, open a Python shell i.e. `python`.
3. In the Python shell, run these commands:
   1. `import os`
   2. `import django`
   3. `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taccsite_cms.settings")`
   4. `django.setup()`
   5. Any additional debugging code or scripts you want to execute.

## Reference

- [Programmatically create a django group with permissions](https://stackoverflow.com/q/22250352/11817077)
- [Writing custom django-admin commands](https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/)
