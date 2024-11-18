from django.contrib.auth.models import Group

from .util import (
    let_view_and_change_page_structure,
    let_view_and_change_media_plugins,
    let_add_and_delete_media_plugins,
    let_view_and_change_adv_media_plugins,
    let_add_and_delete_adv_media_plugins,
    let_view_thumbnail_option,
    let_view_and_change_folder,
    let_view_and_change_image_file,
)

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name='Media Editor (Advanced)'
    )

    let_view_and_change_page_structure(group)
    let_view_and_change_media_plugins(group)
    let_add_and_delete_media_plugins(group)
    let_view_and_change_adv_media_plugins(group)
    let_add_and_delete_adv_media_plugins(group)
    let_view_thumbnail_option(group)
    let_view_and_change_folder(group)
    let_view_and_change_image_file(group)
