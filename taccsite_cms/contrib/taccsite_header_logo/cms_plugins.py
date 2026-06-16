from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from djangocms_picture.cms_plugins import PicturePlugin
from djangocms_picture.models import Picture

from .forms import HeaderLogoForm

HEADER_LOGO_LINK_CLASS = 'navbar-brand'


@plugin_pool.register_plugin
class HeaderLogoPlugin(PicturePlugin):
    """
    Header > "Header logo" (Picture) plugin
    """
    model = Picture
    form = HeaderLogoForm
    module = _('TACC Header')
    name = _('Header logo')

    def render(self, context, instance, placeholder):
        if not instance.attributes:
            instance.attributes = {}

        # To add required attributes
        existing_class = instance.attributes.get('class', '')
        instance.attributes['class'] = f'{HEADER_LOGO_LINK_CLASS} {existing_class}'.strip()

        return super().render(context, instance, placeholder)
