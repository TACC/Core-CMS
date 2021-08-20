from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from taccsite_cms.contrib.constants import TEXT_FOR_NESTED_PLUGIN_CONTENT_SWAP

from .models import TaccsiteCallout

@plugin_pool.register_plugin
class TaccsiteCalloutPlugin(CMSPluginBase):
    """
    Components > "Callout" Plugin
    https://confluence.tacc.utexas.edu/x/EiIFDg
    """
    module = 'TACC Site'
    model = TaccsiteCallout
    name = _('Callout')
    render_template = 'callout.html'

    cache = True
    text_enabled = False
    allow_children = True
    # GH-91: Enable this limitation
    # parent_classes = [
    #     'SectionPlugin'
    # ]
    child_classes = [
        'PicturePlugin',
        'Bootstrap4PicturePlugin'
    ]
    max_children = 1

    fieldsets = [
        (None, {
            'fields': (
                'title', 'description',
            ),
        }),
        (_('Figure'), {
            'classes': ('collapse',),
            'description': TEXT_FOR_NESTED_PLUGIN_CONTENT_SWAP.format(
                element='an image',
                plugin_name='Image'
            ),
            'fields': (),
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
        has_children = len(instance.child_plugin_instances)

        classes = concat_classnames([
            'c-callout',
            'c-callout--has-children' if has_children else '',
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return context
