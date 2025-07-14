"""
To view unpublished pages (can see page and structure, but can not edit)
"""

from django.contrib.auth.models import Group

from ..util import (
    let_view_page_and_structure
)

GROUP_NAME = 'Unpublished Page Viewer'

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name=GROUP_NAME
    )

    let_view_page_and_structure(group)
