"""Template tags for header logo (e.g. building plugin_logo from Picture plugin)."""
from django import template

register = template.Library()


@register.simple_tag
def header_logo_from_picture(instance, picture_link):
    """
    Custom Template Tag `header_logo_from_picture`

    Use: Build plugin_logo from djangocms_picture instance for header_logo.

    Load custom tag into template:
        {% load header_logo_from_picture %}

    Template inline usage:
        {% header_logo_from_picture instance picture_link as plugin_logo %}
        {% include "header_logo.html" with plugin_logo=plugin_logo %}
    """
    picture = getattr(instance, 'picture', None)
    attrs = getattr(instance, 'attributes', None) or {}

    default_alt_text = getattr(picture, 'default_alt_text', None) if picture else None

    alt = attrs.get('alt') or default_alt_text or ''
    img_src = getattr(instance, 'img_src', None) or ''
    link_target = getattr(instance, 'link_target', None)

    return {
        'is_remote': False,
        'img_file_src': img_src,
        'img_class': '',
        'link_href': picture_link or '/',
        'link_target': link_target or '',
        'img_alt_text': alt,
        'img_crossorigin': 'anonymous',
    }
