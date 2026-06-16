from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from djangocms_picture.cms_plugins import PicturePlugin
from djangocms_picture.models import Picture

from .forms import HeaderLogoForm

HEADER_LOGO_ELEMENT_ID = 'header-logo'


@plugin_pool.register_plugin
class HeaderLogoPlugin(PicturePlugin):
    """
    Header > "Header logo" plugin

    Full Picture plugin; default id="header-logo" when not set in Attributes.
    """
    model = Picture
    form = HeaderLogoForm
    module = _('TACC Header')
    name = _('Header logo')

    def render(self, context, instance, placeholder):
        if not instance.attributes:
            instance.attributes = {}
        if 'id' not in instance.attributes:
            instance.attributes['id'] = HEADER_LOGO_ELEMENT_ID
        return super().render(context, instance, placeholder)
