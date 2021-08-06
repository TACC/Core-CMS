from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from djangocms_link.cms_plugins import LinkPlugin

from taccsite_cms.contrib.helpers import concat_classnames
from taccsite_cms.contrib.taccsite_offset.cms_plugins import get_direction_classname

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
        (_('Subsystems and/or resources - Introduction'), {
            'fields': (
                'other_title',
                'other_desc',
            )
        }),
        (_('Subsystems and/or resources - Data'), {
            'classes': ('collapse',),
            'description': '\
            <dl>\
                <dt>To add data</dt>\
                    <dd>nest a plugin inside this one.</dd>\
                <dt>To edit data</dt>\
                    <dd>edit the existing plugin.*</dd>\
            </dl>\
            <br />\
            * If the existing data is from a plugin not nested within this one, then you should nest it inside this one instead.\
            ',
            'fields': ()
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
            's-system-specs',
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        context.update({
            'default_other_title': DEFAULT_OTHER_TITLE,
            'has_other': instance.other_title or instance.other_desc,
            'link_url': instance.get_link(),
            'link_text': instance.name,
            'link_target': instance.target
        })
        return context
