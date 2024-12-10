"""
To edit layout (Containers, Rows, Columns)
"""

from django.contrib.auth.models import Group

from .util import (
    let_view_and_change_page_structure,
    let_view_and_change_grid
)

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name='Grid Editor (Basic)'
    )

    let_view_and_change_page_structure(group)
    let_view_and_change_grid(group)
