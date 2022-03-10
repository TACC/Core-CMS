from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from djangocms_link.cms_plugins import LinkPlugin

from taccsite_cms.contrib.helpers import (
    concat_classnames,
    get_model_field_name
)
from taccsite_cms.contrib.constants import TEXT_FOR_NESTED_PLUGIN_CONTENT_SWAP

from .models import TaccsiteCallout



# Plugin

@plugin_pool.register_plugin
class TaccsiteCalloutPlugin(LinkPlugin):
    """
    Components > "Callout" Plugin
    https://confluence.tacc.utexas.edu/x/EiIFDg
    """
    module = 'TACC Site'
    model = TaccsiteCallout
    name = _('Callout')
    render_template = 'callout.html'
    def get_render_template(self, context, instance, placeholder):
        return self.render_template

    cache = True
    text_enabled = False
    allow_children = True
    # GH-91: Enable this limitation
    # parent_classes = [
    #     'SectionPlugin'
    # ]
    child_classes = [
        'PicturePlugin'
    ]
    max_children = 1

    fieldsets = [
        (None, {
            'fields': (
                'title', 'description',
            ),
        }),
        (_('Link'), {
            'fields': (
                ('external_link', 'internal_link'),
                ('anchor', 'target'),
            )
        }),
        (_('Image'), {
            'classes': ('collapse',),
            'description': TEXT_FOR_NESTED_PLUGIN_CONTENT_SWAP.format(
                element='an image',
                plugin_name='Image'
            ) + '\
            <br />\
            If image disappears while editing, then reload the page to reload the image.',
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
        has_child_plugin = {}

        # To identify child plugins
        for plugin_instance in instance.child_plugin_instances:
            if (type(plugin_instance).__name__ == 'Picture'):
                has_child_plugin['image'] = True
                context.update({ 'image_plugin': plugin_instance })

        classes = concat_classnames([
            'c-callout',
            'c-callout--has-figure' if has_child_plugin.get('image') else '',
            'c-callout--is-link' if instance.get_link() else '',
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        context.update({
            'link_url': instance.get_link(),
            'link_target': instance.target
        })
        return context
