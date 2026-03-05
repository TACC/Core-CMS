"""Template tags for header logo (e.g. building plugin_logo from Picture plugin)."""
from django import template

from cms.models import StaticPlaceholder

register = template.Library()


def _get_header_content_parsed(request, placeholder_name):
    """
    Return (logo_plugin, logo_link, remaining_plugins).
    If placeholder has just 1 Picture w/ template "header_logo", treat as logo.
    Otherwise, remaining_plugins are shown at bottom of header.
    """
    site = getattr(request, 'site', None)
    placeholder = StaticPlaceholder.objects.filter(
        code=placeholder_name,
        site=site
    ).first()
    no_content = (None, None, [])

    if not placeholder:
        return no_content

    placeholder_instance = placeholder.public

    if not placeholder_instance:
        return no_content

    plugin_list = placeholder_instance.get_plugins_list(language=request.LANGUAGE_CODE)
    no_logo_content = (None, None, list(plugin_list))

    if len(plugin_list) == 1:
        first_plugin = plugin_list[0]
        instance, plugin_type = first_plugin.get_plugin_instance()
        is_picture_pluign = getattr(plugin_type, '__name__', '') == 'PicturePlugin'
        uses_logo_template = getattr(instance, 'template', None) == 'header_logo'

        if instance and is_picture_pluign:
            if uses_logo_template:
                link = getattr(instance, 'get_link', lambda: None)()
                logo_content = (instance, link or '#', [])

                return logo_content

    return no_logo_content


@register.simple_tag(takes_context=True)
def get_header_content_parsed(context, placeholder_name):
    """
    Parse static placeholder for header: single "Header logo" Picture = logo; else all plugins = remaining.
    Returns object with .logo_plugin, .logo_link, .remaining_plugins.
    """
    request = context.get('request')
    content_default = type('HeaderContent', (), {
        'logo_plugin': None,
        'logo_link': None,
        'remaining_plugins': []
    })()

    if not request:
        return content_default

    logo_plugin, logo_link, remaining_plugins = _get_header_content_parsed(
        request,
        placeholder_name
    )
    content_parsed = type('HeaderContent', (), {
        'logo_plugin': logo_plugin,
        'logo_link': logo_link,
        'remaining_plugins': remaining_plugins
    })()

    return content_parsed


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
