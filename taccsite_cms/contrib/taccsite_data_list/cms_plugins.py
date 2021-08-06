from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from taccsite_cms.contrib.helpers import concat_classnames
from taccsite_cms.contrib.taccsite_offset.cms_plugins import get_direction_classname

from taccsite_cms.contrib.helpers import AbstractMaxChildrenPlugin

from .models import TaccsiteDataList, TaccsiteDataListItem
from .constants import ORIENTATION_DICT, TYPE_STYLE_DICT, DENSITY_DICT



# Helpers

def get_classname(dict, value):
    """Get layout class based on value."""
    return dict.get(value, {}).get('classname')



# Plugins

@plugin_pool.register_plugin
class TaccsiteDataListPlugin(CMSPluginBase, AbstractMaxChildrenPlugin):
    """
    Components > "Data List" Plugin
    https://confluence.tacc.utexas.edu/x/EiIFDg
    """
    module = 'TACC Site'
    model = TaccsiteDataList
    name = _('Data List')
    render_template = 'data_list.html'

    cache = True
    text_enabled = True
    allow_children = True
    child_classes = [
        'TaccsiteDataListItemPlugin'
    ]

    fieldsets = [
        (_('Required configuration'), {
            'fields': (
                'type_style',
                'orientation',
                'density',
            )
        }),
        (_('Optional configuration'), {
            'fields': (
                'truncate_values',
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
            'c-data-list',
            get_classname(ORIENTATION_DICT, instance.orientation),
            get_classname(TYPE_STYLE_DICT, instance.type_style),
            get_classname(DENSITY_DICT, instance.density),
            'c-data-list--should-truncate-values'
                if instance.truncate_values else '',
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return context

@plugin_pool.register_plugin
class TaccsiteDataListItemPlugin(CMSPluginBase):
    """
    Components > "Data List Item" Plugin
    https://confluence.tacc.utexas.edu/x/EiIFDg
    """
    module = 'TACC Site'
    model = TaccsiteDataListItem
    name = _('Data List Item')
    render_template = 'data_list_item.html'

    cache = True
    text_enabled = False
    allow_children = True
    child_classes = [
        'LinkPlugin'
    ]
    max_children = 1 # Only a label until we know what value will need

    fieldsets = [
        (None, {
            'fields': (
                ('key', 'value'),
                ('use_plugin_as_key'),
            )
        })
    ]

    # Render

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        request = context['request']

        parent_plugin_instance = instance.parent.get_plugin_instance()[0]

        context.update({
            'parent_plugin_instance': parent_plugin_instance
        })

        return context
