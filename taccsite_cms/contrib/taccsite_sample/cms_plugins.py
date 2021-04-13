from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from .models import TaccsiteSample

from .defaults import name as default_name

@plugin_pool.register_plugin
class TaccsiteSamplePlugin(CMSPluginBase):
    """
    Components > "Sample (Greet User)" Plugin
    https://url.to/docs/components/sample/
    """
    module = 'TACC Site'
    model = TaccsiteSample
    name = _('Sample (Greet User)')
    render_template = 'sample.html'
    cache = False
    text_enabled = True

    def get_name(self, instance, user):
        """Get name of authenticated user or the name for any guest."""

        if user.is_authenticated:
            name = user.first_name + ' ' + user.last_name
        elif bool(instance.guest_name):
            name = instance.guest_name
        else:
            name = default_name

        return name

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        request = context['request']

        context.update({
            'user_name': self.get_name(instance, request.user)
        })
        return context
