"""
To edit and move layout elements (Containers, Rows, Columns)
"""

from django.contrib.auth.models import Group

from ..util import (
    let_view_page_and_structure,
    let_view_and_change_grid
)

GROUP_NAME = 'Grid Editor (Basic)'

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name=GROUP_NAME
    )

    let_view_page_and_structure(group)
    let_view_and_change_grid(group)
