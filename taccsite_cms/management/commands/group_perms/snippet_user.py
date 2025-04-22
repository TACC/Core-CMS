"""
To edit, move, add and delete Snippet plugins
(not snippets themselves, but "Snippet" blocks which point to a snippet)
"""

from django.contrib.auth.models import Group

from ..util import (
    let_view_page_and_structure,
    let_view_and_change_snippet_plugin,
    let_add_and_delete_snippet_plugin,
)

GROUP_NAME = 'Snippet User'

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name=GROUP_NAME
    )

    let_view_page_and_structure(group)
    let_view_and_change_snippet_plugin(group)
    let_add_and_delete_snippet_plugin(group)
