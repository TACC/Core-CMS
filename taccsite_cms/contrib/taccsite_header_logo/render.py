from cms.models import StaticPlaceholder
from cms.plugin_rendering import ContentRenderer

from taccsite_cms.contrib.taccsite_header_logo.constants import HEADER_LOGO_PLACEHOLDER_NAME
from taccsite_cms.contrib.taccsite_header_logo.cms_plugins import HeaderLogoPlugin


def render(request, context):
    """
    Render published HeaderLogoPlugin from header-logo (logo-only fragment).
    """
    static_ph = StaticPlaceholder.objects.filter(code=HEADER_LOGO_PLACEHOLDER_NAME).first()
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
