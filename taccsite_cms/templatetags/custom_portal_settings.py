from django import template

register = template.Library()

@register.filter
def index(indexable, i):
    """
    Custom Template Tag `index`

    Use: Access Setting List Values by Index Number in Templates.

    Load custom tag into template:
        {% load custom_portal_settings %}

    Example settings.py configuration:
        settings_values = [['a','b','c'], ['d','e','f']]

    Template inline usage:
        {{ settings_values|index:x|index:y }}

    Example:
        <div>{{ settings_values|index:0 }}</div>
            # <div>['a','b','c']</div>
        <div>{{ settings_values|index:0|index:2 }}</div>
            # <div>c</div>

    - Also works with for loops.
    """
    return indexable[i]


@register.filter
def get_at_index(list, index):
    """
    Gets the list element at the given index.
    """
    return list[index]
