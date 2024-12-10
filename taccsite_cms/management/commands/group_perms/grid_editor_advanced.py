"""
To edit, move, add, and delete layout elements (Containers, Rows, Columns)
"""

from django.contrib.auth.models import Group

from ..util import (
    let_view_and_change_page_structure,
    let_view_and_change_grid,
    let_add_and_delete_grid
)

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name='Grid Editor (Advanced)'
    )

    let_view_and_change_page_structure(group)
    let_view_and_change_grid(group)
    let_add_and_delete_grid(group)
