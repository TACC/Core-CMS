from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _

from taccsite_cms.contrib.helpers import concat_classnames

from .models import TaccsiteSystemMonitor

@plugin_pool.register_plugin
class TaccsiteSystemMonitorPlugin(CMSPluginBase):
    """
    Components > "System Monitor" Plugin
    https://url.to/docs/components/system_monitor/
    """
    module = 'TACC Site'
    model = TaccsiteSystemMonitor
    name = _('System Monitor')
    render_template = 'system_monitor.html'

    cache = True
    text_enabled = False
    allow_children = False

    fieldsets = [
        (_('Single System'), {
            # NOTE: Can GH-295 fix the reload caveat?
            'description': 'Only a single system may be shown. After editing this plugin, reload the page to load system data.',
            'fields': (
                'system',
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
            's-system-monitor',
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return context
