"""Template tags for header logo (e.g. building plugin_logo from Picture plugin)."""
from django import template

register = template.Library()


@register.simple_tag
def header_logo_from_picture(instance, picture_link):
    """
    Build a plugin_logo dict from a djangocms_picture instance for use in header_logo.html.

    Usage: {% header_logo_from_picture instance picture_link as plugin_logo %}
    Then:  {% include "header_logo.html" with plugin_logo=plugin_logo %}
    """
    attributes = getattr(instance, 'attributes', None) or {}
    picture = getattr(instance, 'picture', None)
    alt = attributes.get('alt') or (getattr(picture, 'default_alt_text', None) if picture else None) or ''
    img_src = getattr(instance, 'img_src', None) or ''
    return {
        'link_href': picture_link or '#',
        'link_target': getattr(instance, 'link_target', None) or '',
        'img_class': '',
        'img_file_src': img_src,
        'is_remote': True,
        'img_crossorigin': '',
        'img_alt_text': alt,
    }
