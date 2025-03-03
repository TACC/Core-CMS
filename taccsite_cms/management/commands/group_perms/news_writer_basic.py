"""
To edit and add Blog articles
"""

from django.contrib.auth.models import Group

from ..util import (
    add_perm,
    let_view_page_and_structure,
    let_view_and_change_plugin,
    let_view_and_change_text,
    let_add_and_delete_text,
    let_view_and_change_media_plugins,
    let_add_and_delete_media_plugins,
    let_view_and_change_image_file,
)

GROUP_NAME = 'News Writer (Basic)'

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name=GROUP_NAME
    )

    let_view_page_and_structure(group)
    let_view_and_change_plugin(group)

    let_view_and_change_text(group)
    let_add_and_delete_text(group)

    let_view_and_change_media_plugins(group)
    let_add_and_delete_media_plugins(group)

    let_view_and_change_image_file(group)
    add_perm(group, 'filer', 'image', 'Can add image')

    # Add permissions to view & change & add articles
    add_perm(group, None, None, 'Can view blog article')
    add_perm(group, None, None, 'Can change blog article')
    add_perm(group, None, None, 'Can add blog article')
