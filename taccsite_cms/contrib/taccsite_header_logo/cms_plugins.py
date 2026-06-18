from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from djangocms_picture.cms_plugins import PicturePlugin
from djangocms_picture.models import Picture

from .forms import HeaderLogoForm

HEADER_LOGO_LINK_CLASS = 'navbar-brand'
PORTAL_LOGO_IMG_CLASS = 'portal-logo'


def picture_attributes_hoist_to_parent(instance, picture_link):
    """Match djangocms_picture/default/picture.html attribute placement."""
    default_caption = ''
    if instance.picture:
        default_caption = getattr(instance.picture, 'default_caption', '') or ''
    return bool(
        instance.caption_text
        or default_caption
        or picture_link
        or instance.child_plugin_instances
    )


def apply_header_logo_classes(instance, context, picture_link):
    if not instance.attributes:
        instance.attributes = {}

    existing_class = instance.attributes.get('class', '')
    link_class = f'{HEADER_LOGO_LINK_CLASS} {existing_class}'.strip()

    if picture_attributes_hoist_to_parent(instance, picture_link):
        instance.attributes['class'] = link_class
        context['picture_img_class'] = PORTAL_LOGO_IMG_CLASS
    else:
        instance.attributes['class'] = f'{link_class} {PORTAL_LOGO_IMG_CLASS}'.strip()


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
        apply_header_logo_classes(instance, context, instance.get_link())
        return super().render(context, instance, placeholder)
