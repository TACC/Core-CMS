# SEE: https://github.com/django-cms/djangocms-bootstrap4/blob/2.0.0/djangocms_bootstrap4/contrib/bootstrap4_content/cms_plugins.py#L41

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_text

from taccsite_cms.contrib.helpers import concat_classes

from .models import TaccsiteBlockquote

from .defaults import user_name as default_name

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
                ('quote_text', 'quote_origin'),
                'quote_alignment',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse'),
            'fields': (
                'attributes',
            )
        }),
    ]

    # Helpers

    def get_alignment_class(self, instance, option_value):
        """Get alignment class based on alignment option."""

        switcher = {
            'right': 'c-offset-content--right',
            'left': 'c-offset-content--left',
        }

        return switcher.get(option_value, '')

    # Render

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        request = context['request']

        classes = ' '.join([
            's-blockquote',
            self.get_alignment_class(instance, instance.quote_alignment),
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return context
