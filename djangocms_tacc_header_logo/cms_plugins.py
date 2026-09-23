from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from djangocms_picture.cms_plugins import PicturePlugin
from djangocms_picture.models import Picture

from .forms import TaccsiteHeaderLogoForm

HEADER_LOGO_ID = 'header-logo'
HEADER_LOGO_CLASS = 'navbar-brand'


@plugin_pool.register_plugin
class TaccsiteHeaderLogoPlugin(PicturePlugin):
    """
    Components > "Header logo" Plugin
    """
    model = Picture
    form = TaccsiteHeaderLogoForm
    module = 'TACC Site'
    name = _('Header logo')

    def render(self, context, instance, placeholder):
        if not instance.attributes:
            instance.attributes = {}

        existing_class = instance.attributes.get('class', '')
        instance.attributes['class'] = f'{HEADER_LOGO_CLASS} {existing_class}'.strip()
        instance.attributes['id'] = HEADER_LOGO_ID

        return super().render(context, instance, placeholder)
