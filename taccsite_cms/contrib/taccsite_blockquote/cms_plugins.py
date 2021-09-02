from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from taccsite_cms.contrib.helpers import concat_classnames
from taccsite_cms.contrib.taccsite_offset.cms_plugins import get_direction_classname

from .models import TaccsiteBlockquote

@plugin_pool.register_plugin
class TaccsiteBlockquotePlugin(CMSPluginBase):
    """
    Components > "Blockquote" Plugin
    https://confluence.tacc.utexas.edu/x/FIEjCQ
    """
    module = 'TACC Site'
    model = TaccsiteBlockquote
    name = _('Blockquote')
    render_template = 'blockquote.html'

    cache = True
    text_enabled = True
    allow_children = False

    fieldsets = [
        (None, {
            'fields': (
                'text',
                'origin',
                'use_cite',
            )
        }),
        (_('Citation'), {
            'classes': ('collapse',),
            'fields': (
                'cite_person',
                ('cite_text', 'cite_url'),
            )
        }),
        (_('Layout'), {
            'fields': (
                'offset',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'attributes',
            )
        }),
    ]

    # Render

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        request = context['request']

        classes = concat_classnames([
            's-blockquote',
            get_direction_classname(instance.offset),
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return context
