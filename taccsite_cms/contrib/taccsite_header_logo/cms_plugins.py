from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from djangocms_picture.cms_plugins import PicturePlugin
from djangocms_picture.models import Picture


@plugin_pool.register_plugin
class HeaderLogoPlugin(PicturePlugin):
    """
    Header > "Header logo" plugin

    Same fields as Picture; fixed navbar markup (no template dropdown).
    """
    model = Picture
    module = _('TACC Header')
    name = _('Header logo')
    render_template = 'taccsite_header_logo/header_logo_plugin.html'
    cache = False

    fieldsets = [
        (None, {
            'fields': (
                'picture',
                'external_picture',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'use_responsive_image',
                ('width', 'height'),
                'alignment',
                'caption_text',
                'attributes',
            )
        }),
        (_('Link settings'), {
            'classes': ('collapse',),
            'fields': (
                ('link_url', 'link_page'),
                'link_target',
                'link_attributes',
            )
        }),
        (_('Cropping settings'), {
            'classes': ('collapse',),
            'fields': (
                ('use_automatic_scaling', 'use_no_cropping'),
                ('use_crop', 'use_upscale'),
                'thumbnail_options',
            )
        })
    ]

    def get_render_template(self, context, instance, placeholder):
        return self.render_template
