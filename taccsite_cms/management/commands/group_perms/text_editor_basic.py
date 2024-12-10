"""
To edit and move textual elements blocks, folders, and files
"""

from django.contrib.auth.models import Group

from ..util import (
    let_view_and_change_page_structure,
    let_view_and_change_text,
    let_view_and_change_folder,
    let_view_and_change_file,
)

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name='Text Editor (Basic)'
    )

    let_view_and_change_page_structure(group)
    let_view_and_change_text(group)
    let_view_and_change_folder(group)
    let_view_and_change_file(group)
