from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from taccsite_cms.contrib.helpers import concat_classnames
from taccsite_cms.contrib.taccsite_offset.cms_plugins import get_direction_classname

from .models import TaccsiteDataList
from .constants import ORIENTATION_DICT, TYPE_STYLE_DICT, DENSITY_DICT



# Helpers

def get_classname(dict, value):
    """Get layout class based on value."""
    return dict.get(value, {}).get('classname')



# Plugins

@plugin_pool.register_plugin
class TaccsiteDataListPlugin(CMSPluginBase):
    """
    Components > "Data List" Plugin
    https://confluence.tacc.utexas.edu/x/EiIFDg
    """
    module = 'TACC Site'
    model = TaccsiteDataList
    name = _('Data List')
    render_template = 'data_list.html'

    cache = True
    text_enabled = False
    allow_children = True
    child_classes = [
        'TaccsiteStaticDataListItemPlugin'
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
            'c-data_list',
            get_classname(ORIENTATION_DICT, instance.orientation),
            get_classname(TYPE_STYLE_DICT, instance.type_style),
            get_classname(DENSITY_DICT, instance.density),
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return context
