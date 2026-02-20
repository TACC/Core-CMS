"""
To edit, move, add, and delete images, videos, thumbnail sizes, and folders
"""

from django.contrib.auth.models import Group

from ..util import (
    let_view_page_and_structure,
    let_view_and_change_media_plugins,
    let_add_and_delete_media_plugins,
    let_view_and_change_adv_media_plugins,
    let_add_and_delete_adv_media_plugins,
    let_view_thumbnail_option,
    let_view_and_change_folder,
    let_add_and_delete_folder,
    let_view_and_change_image_file,
)

GROUP_NAME = 'Media Editor (Advanced)'

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name=GROUP_NAME
    )

    let_view_page_and_structure(group)
    let_view_and_change_media_plugins(group)
    let_add_and_delete_media_plugins(group)
    let_view_and_change_adv_media_plugins(group)
    let_add_and_delete_adv_media_plugins(group)
    let_view_thumbnail_option(group)
    let_view_and_change_folder(group)
    let_view_and_change_image_file(group)
