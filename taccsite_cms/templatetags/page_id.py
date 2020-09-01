from django import template

register = template.Library()

@register.simple_tag
def page_id():
    """
    Returns the ID of the current page.

    Load custom tag into template:
        {% load custom_portal_settings %}

    Template inline usage:
        {% page_id %}

    Example:
        <html id="page-{% page_id %}">
    """
    return 'WES-WANTS-PAGE-ID'
