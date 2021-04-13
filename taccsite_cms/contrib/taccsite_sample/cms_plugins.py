from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_text

from .models import TaccsiteSample

from .defaults import user_name as default_name

# SEE: http://docs.django-cms.org/en/release-3.7.x/reference/plugins.html
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
    # NOTE: Use case is unclear
    # admin_preview = True
    # NOTE: To change for all TACC plugins add taccsite_cms/templates/admin/...
    # change_form_template = 'templates/plugin_change_form.html'
    # NOTE: To change field widget and other attribute beyond `models.…Field`
    # form = TaccsiteSamplePluginForm # TODO: Provide example

    # FAQ: Sets tooltip of preview of this plugin within a Text plugin
    def icon_alt(self, instance):
        super_value = force_text(super().icon_alt(instance))
        name = self.get_name(instance)
        return f'Hello, {{{name}}} [{super_value}]'
    # NOTE: Our previews (see `icon_alt`) are rich and have no icon...
    # TODO: Confirm whether these are ever necessary
    # def icon_src(self, instance)
    # def text_editor_button_icon(...)

    # Helpers

    def get_name(self, instance, user=None):
        """Get name of authenticated user or the name for any guest."""

        if user and user.is_authenticated:
            name = user.first_name + ' ' + user.last_name
        elif bool(instance.guest_name):
            name = instance.guest_name
        else:
            name = default_name

        return name

    # Render

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        request = context['request']

        context.update({
            'user_name': self.get_name(instance, request.user)
        })
        return context
