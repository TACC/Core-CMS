from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import gettext_lazy as _

from taccsite_cms.contrib.helpers import concat_classnames

from .models import TaccsiteOffset, get_direction_classname

@plugin_pool.register_plugin
class TaccsiteOffsetPlugin(CMSPluginBase):
    """
    Components > "Offset Content" Plugin
    https://confluence.tacc.utexas.edu/x/FIEjCQ
    """
    module = 'TACC Site'
    model = TaccsiteOffset
    name = _('Offset Content')
    render_template = 'offset.html'

    cache = False
    text_enabled = False
    allow_children = True

    fieldsets = [
        (None, {
            'fields': (
                'direction',
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
            get_direction_classname(instance.direction),
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return context
