from django import template
from urllib.parse import urlparse
from django.utils.html import format_html
from django.contrib import auth as auth

register = template.Library()

# NOTE: This file, in Core CMS, is an example.
# REQUIRES: Registering simple_tag "limit_visibility_in_menu" that returns True.
# EXAMPLE USAGE: https://github.com/TACC/Core-CMS-Custom/pull/45

# INSTRUCTIONS
# (only for a Core-CMS-Custom app)
#
# 1. Clone this file into the app's matching directory.
# 2. The CMS should add Page IDs and User Groups as needed.
# 3. The example functions and example logic may be built upon or replaced.

# FAQ: Example Functions
#
# def has_certain_groups(user):
#     for group in user.groups.all():
#         if group.name in ['SOME_GROUP', 'ANOTHER_GROUP', 'YET_ANOTHER']:
#             return True
#     return False
#
# def is_specific_group(user):
#     return user.groups.filter(name='SOME_GROUP').exists()

@register.simple_tag(takes_context=True)
def limit_visibility_in_menu(context, menu_item):
    """
    Custom Template Tag `limit_visibility_in_menu`

    Use: Return (boolean) whether given menu item is visible by current user.

    Load custom tag into template:
        {% load limit_visibility_in_menu %}

    Template inline usage:
        {# (renders `True` or `False`) #}
        {% limit_visibility_in_menu menu_item %}

        {# (renders "A" or "B") #}
        {% limit_visibility_in_menu menu_item as can_view %}
        {% if can_view %} A {% else %} B {% endif %}

    Example:
        ../templates/cms_menu.html
    """
    request = context['request']
    user = request.user
    has_page_id = ('reverse_id' in menu_item.attr)
    page_id = menu_item.attr['reverse_id'] if has_page_id else ''

    # FAQ: Example Logic
    #
    # if (
    #     user.is_superuser or
    #     page_id == 'certain_groups_only_page' and has_certain_groups(user) or
    #     page_id == 'some_group_only_page' and is_specific_group(user) or
    #     not bool(page_id)
    # ):
    #     return True
    # else:
    #     return False

    return True
