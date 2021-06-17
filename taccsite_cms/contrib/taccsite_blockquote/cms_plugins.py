# SEE: https://github.com/django-cms/djangocms-bootstrap4/blob/2.0.0/djangocms_bootstrap4/contrib/bootstrap4_content/cms_plugins.py#L41

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from taccsite_cms.contrib.helpers import concat_classnames

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

    cache = False
    text_enabled = False

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
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return context
