"""
To edit and move Style plugins
(not CSS, but "Style" block that lets editors add custom markup e.g. for Cards)
"""

from django.contrib.auth.models import Group

from ..util import (
    let_view_page_and_structure,
    let_view_and_change_style_plugin
)

GROUP_NAME = 'Style Editor (Basic)'

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name=GROUP_NAME
    )

    let_view_page_and_structure(group)
    let_view_and_change_style_plugin(group)
