from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name='Image Editor (Basic)'
    )

    model_name = 'page'.lower().replace(' ', '')
    content_type = ContentType.objects.get(app_label='cms', model=model_name)
    group.permissions.add( Permission.objects.get(name='Can change page', content_type=content_type) )

    model_name = 'placeholder'.lower().replace(' ', '')
    content_type = ContentType.objects.get(app_label='cms', model=model_name)
    group.permissions.add( Permission.objects.get(name='Can use Structure mode', content_type=content_type) )

    model_name = 'bootstrap4 picture'.lower().replace(' ', '')
    content_type = ContentType.objects.get(app_label='bootstrap4_picture', model=model_name)
    group.permissions.add( Permission.objects.get(name='Can change bootstrap4 picture', content_type=content_type) )

    model_name = 'bootstrap4 picture'.lower().replace(' ', '')
    content_type = ContentType.objects.get(app_label='bootstrap4_picture', model=model_name)
    group.permissions.add( Permission.objects.get(name='Can view bootstrap4 picture', content_type=content_type) )

    model_name = 'picture'.lower().replace(' ', '')
    content_type = ContentType.objects.get(app_label='djangocms_picture', model=model_name)
    group.permissions.add( Permission.objects.get(name='Can change picture', content_type=content_type) )

    model_name = 'picture'.lower().replace(' ', '')
    content_type = ContentType.objects.get(app_label='djangocms_picture', model=model_name)
    group.permissions.add( Permission.objects.get(name='Can view picture', content_type=content_type) )

    model_name = 'file'.lower().replace(' ', '')
    content_type = ContentType.objects.get(app_label='filer', model=model_name)
    group.permissions.add( Permission.objects.get(name='Can view file', content_type=content_type) )

    model_name = 'Folder'.lower().replace(' ', '')
    content_type = ContentType.objects.get(app_label='filer', model=model_name)
    group.permissions.add( Permission.objects.get(name='Can use directory listing', content_type=content_type) )

    model_name = 'Folder'.lower().replace(' ', '')
    content_type = ContentType.objects.get(app_label='filer', model=model_name)
    group.permissions.add( Permission.objects.get(name='Can view Folder', content_type=content_type) )

    model_name = 'image'.lower().replace(' ', '')
    content_type = ContentType.objects.get(app_label='filer', model=model_name)
    group.permissions.add( Permission.objects.get(name='Can view image', content_type=content_type) )

    model_name = 'thumbnail option'.lower().replace(' ', '')
    content_type = ContentType.objects.get(app_label='filer', model=model_name)
    group.permissions.add( Permission.objects.get(name='Can view thumbnail option', content_type=content_type) )
