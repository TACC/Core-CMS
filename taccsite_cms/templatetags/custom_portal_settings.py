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
    has_index = (len(indexable) > i)
    value = None

    print("len(indexable)",len(indexable))
    print("i",i)
    print("has_index",has_index)

    if has_index:
        value = indexable[i]

    return value


@register.filter
def get_at_index(list, index):
    """
    Gets the list element at the given index.
    """
    has_index = (len(list) > index)
    value = None

    if has_index:
        value = list[index]

    return value
