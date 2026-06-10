"""Header logo markup"""
from cms.models import StaticPlaceholder
from cms.plugin_rendering import ContentRenderer
from django import template
from django.utils.safestring import mark_safe

from taccsite_cms.contrib.taccsite_header_logo.cms_plugins import HeaderLogoPlugin

register = template.Library()


def render_header_logo_plugin_html(request, context):
    """
    Render published HeaderLogoPlugin from header-content (logo-only fragment).
    """
    static_ph = StaticPlaceholder.objects.filter(code='header-content').first()
    if not static_ph:
        return ''

    placeholder = static_ph.public
    placeholder.is_static = True

    renderer = ContentRenderer(request)
    language = renderer.request_language

    for plugin in renderer.get_plugins_to_render(placeholder, language, template=None):
        if plugin.plugin_type == HeaderLogoPlugin.__name__:
            return renderer.render_plugin(
                plugin,
                context,
                placeholder,
                editable=False,
            )
    return ''


@register.simple_tag(takes_context=True)
def render_header_logo_plugin(context):
    html = render_header_logo_plugin_html(context['request'], context)
    return mark_safe(html) if html else ''


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

    return {
        'img_file_src': img_src,
        'link_href': picture_link or '/',
        'link_target': link_target or '',
        'img_alt_text': alt,
    }
