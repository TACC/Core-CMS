from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from djangocms_link.cms_plugins import LinkPlugin

from taccsite_cms.contrib.constants import TEXT_FOR_NESTED_PLUGIN_CONTENT_ADD
from taccsite_cms.contrib.helpers import concat_classnames

from .constants import DEFAULT_OTHER_TITLE

from .models import TaccsiteSystemSpecs

@plugin_pool.register_plugin
class TaccsiteSystemSpecsPlugin(LinkPlugin):
    """
    Components > "System Specs" Plugin
    """
    module = 'TACC Site'
    model = TaccsiteSystemSpecs
    name = _('System Specs')
    render_template = 'system_specs.html'
    def get_render_template(self, context, instance, placeholder):
        return self.render_template

    cache = True
    text_enabled = False
    allow_children = True
    child_classes = [
        'TaccsiteSystemMonitorPlugin',
        'PicturePlugin',
        'TaccsiteDataListPlugin',
    ]

    fieldsets = [
        (_('Specifications'), {
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
        (_('Footer link'), {
            'classes': ('collapse',),
            'description': 'The "See More Detailed Specs" link at the bottom of the list. "Display name" is for alternate link text.',
            'fields': (
                ('external_link', 'internal_link'),
                ('anchor', 'target'),
                'name',
            )
        }),
        (_('Subsystems and/or resources - Introduction'), {
            'fields': (
                'other_title',
                'other_desc',
            )
        }),
        (_('Subsystems and/or resources - Data'), {
            'classes': ('collapse',),
            'description': TEXT_FOR_NESTED_PLUGIN_CONTENT_ADD.format(
                element='data',
                plugin_name='Data List'
            ),
            'fields': ()
        }),
        (_('Image'), {
            'classes': ('collapse',),
            'description': TEXT_FOR_NESTED_PLUGIN_CONTENT_ADD.format(
                element='an image',
                plugin_name='(…) Image'
            ),
            'fields': ()
        }),
        (_('System monitor'), {
            'classes': ('collapse',),
            'description': TEXT_FOR_NESTED_PLUGIN_CONTENT_ADD.format(
                element='a system monitor',
                plugin_name='(…) System Monitor'
            ),
            'fields': ()
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
            's-system-specs',
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        # To identify child plugins
        for plugin_instance in instance.child_plugin_instances:
            if (type(plugin_instance).__name__ == 'TaccsiteSystemMonitor'):
                context.update({ 'sysmon_plugin': plugin_instance })
            if (type(plugin_instance).__name__ == 'Picture'):
                context.update({ 'image_plugin': plugin_instance })
            if (type(plugin_instance).__name__ == 'TaccsiteDataList'):
                context.update({ 'data_plugin': plugin_instance })

        context.update({
            'default_other_title': DEFAULT_OTHER_TITLE,
            'has_other': instance.other_title or instance.other_desc,
            'link_url': instance.get_link(),
            'link_text': instance.name,
            'link_target': instance.target
        })
        return context
