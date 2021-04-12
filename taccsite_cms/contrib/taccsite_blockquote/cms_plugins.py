from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from .models import TaccsiteBlockquote

@plugin_pool.register_plugin
class TaccsiteBlockquotePlugin(CMSPluginBase):
    """
    Components > "Blockquote" Plugin
    https://confluence.tacc.utexas.edu/x/FIEjCQ
    """
    module = 'TACC Site'
    model = TaccsiteBlockquote
    name = _('Blockquote')
    render_template = 'blockquote.html'
    cache = False

    def get_name(self, instance, user):
        """Get name of authenticated user or the name for any guest."""

        if user.is_authenticated:
            name = user.first_name + ' ' + user.last_name
        if False:
            name = 'Jim'
        else:
            name = instance.guest_name

        return name

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        request = context['request']

        context.update({
            'user_name': self.get_name(instance, request.user)
        })
        return context
