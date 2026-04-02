"""Template tags for header logo (e.g. building plugin_logo from Picture plugin)."""
from django import template

from cms.models import StaticPlaceholder

register = template.Library()


def _get_header_content_parsed(request, placeholder_name):
    """
    Parse content of static placeholder `placeholder_name`:

    * (if present) single "Header logo" Picture as logo
    * (if present) link for logo
    * (if present) remaining plugins

    Return (logo_plugin, logo_link, remaining_plugins).
    """
    logo_plugin = None
    logo_link = None
    remaining_plugins = []

    site = getattr(request, 'site', None)
    placeholder = StaticPlaceholder.objects.filter(
        code=placeholder_name,
        site=site
    ).first()

    # Return NO content (if placeholder does not exist)
    if not placeholder:
        return (logo_plugin, logo_link, remaining_plugins)

    placeholder_instance = placeholder.public
    # Return NO content (if placeholder is not public)
    if not placeholder_instance:
        return (logo_plugin, logo_link, remaining_plugins)

    plugin_list = placeholder_instance.get_plugins_list(language=request.LANGUAGE_CODE)
    remaining_plugins = list(plugin_list)

    if len(plugin_list) == 1:
        first_plugin = plugin_list[0]
        instance, plugin_type = first_plugin.get_plugin_instance()
        is_picture_plugin = type(plugin_type).__name__ == 'PicturePlugin'
        uses_logo_template = getattr(instance, 'template', None) == 'header_logo'

        if instance and is_picture_plugin:
            if uses_logo_template:
                link = getattr(instance, 'get_link', lambda: None)()
                logo_plugin = instance
                logo_link = link or '#'
                remaining_plugins = []

    # Return ALL content (that is available from placeholder)
    return (logo_plugin, logo_link, remaining_plugins)


@register.simple_tag(takes_context=True)
def get_header_content_parsed(context, placeholder_name):
    """
    Parse content of static placeholder `placeholder_name`:

    * (if present) single "Header logo" Picture as logo
    * (if present) link for logo
    * (if present) remaining plugins

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
        {% load header_content_tags %}

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
