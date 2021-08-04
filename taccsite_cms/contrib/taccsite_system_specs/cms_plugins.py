from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from taccsite_cms.contrib.helpers import concat_classnames
from taccsite_cms.contrib.taccsite_offset.cms_plugins import get_direction_classname

from .constants import DEFAULT_OTHER_TITLE

from .models import TaccsiteSystemSpecs

@plugin_pool.register_plugin
class TaccsiteSystemSpecsPlugin(CMSPluginBase):
    """
    Components > "System Specs" Plugin
    """
    module = 'TACC Site'
    model = TaccsiteSystemSpecs
    name = _('System Specs')
    render_template = 'system_specs.html'

    cache = True
    text_enabled = False
    allow_children = False

    fieldsets = [
        (_('System Specifications'), {
            'fields': (
                'system_desc',
                'system_processor_count',
                'system_processor_type',
                'system_node_ram',
                'system_network',
                'system_performance',
                'system_memory',
            )
        }),
        (_('Subsystems / Resources'), {
            'fields': (
                'other_title',
                'other_desc',
            )
        }),
        (_('Footer link'), {
            'classes': ('collapse',),
            'description': 'The "See All" link at the bottom of the list. "Display name" is the text.',
            'fields': (
                'name',
                ('external_link', 'internal_link'),
                ('anchor', 'target'),
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
            's-data_list',
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        context.update({
            'default_other_title': DEFAULT_OTHER_TITLE,
            'has_other': instance.other_title or instance.other_desc
        })
        return context
