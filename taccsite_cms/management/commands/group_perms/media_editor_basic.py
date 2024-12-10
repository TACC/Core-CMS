"""
To edit and move images, videos, thumbnail sizes, and folders
"""

from django.contrib.auth.models import Group

from ..util import (
    let_view_and_change_page_structure,
    let_view_and_change_media_plugins,
    let_view_and_change_adv_media_plugins,
    let_view_thumbnail_option,
    let_view_folder,
    let_view_and_change_image_file,
)

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name='Media Editor (Basic)'
    )

    let_view_and_change_page_structure(group)
    let_view_and_change_media_plugins(group)
    let_view_and_change_adv_media_plugins(group)
    let_view_folder(group)
    let_view_and_change_image_file(group)
    let_view_thumbnail_option(group)
