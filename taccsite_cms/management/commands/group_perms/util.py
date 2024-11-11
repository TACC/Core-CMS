from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

def add_perm(group, app_label, model_name, perm_name):
    """
    Add specific permission to a given group

    This can often be done with just the permission name e.g. —
    `group.permissions.add( Permission.objects.get( name='…' ) )`
    — but providing app and model ensure no conflict.
    """
    model = model_name.lower().replace(' ', '')
    content_type = ContentType.objects.get(
        app_label=app_label,
        model=model
    )

    group.permissions.add(
        Permission.objects.get(
            name=perm_name,
            content_type=content_type
        )
    )
