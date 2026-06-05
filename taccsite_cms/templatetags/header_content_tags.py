"""Template tags for header logo (HeaderLogoPlugin → header_logo markup)."""
from django import template

register = template.Library()


@register.simple_tag
def header_logo_from_picture(instance, picture_link):
    """
    Build plugin_logo dict from djangocms_picture Picture instance for header markup.
    """
    picture = getattr(instance, 'picture', None)
    attrs = getattr(instance, 'attributes', None) or {}

    default_alt_text = getattr(picture, 'default_alt_text', None) if picture else None

    alt = attrs.get('alt') or default_alt_text or ''
    img_src = getattr(instance, 'img_src', None) or ''
    link_target = getattr(instance, 'link_target', None)
    is_remote = img_src.startswith('http://') or img_src.startswith('https://')

    return {
        'is_remote': is_remote,
        'img_file_src': img_src,
        'img_class': '',
        'link_href': picture_link or '/',
        'link_target': link_target or '',
        'img_alt_text': alt,
        'img_crossorigin': 'anonymous',
    }
