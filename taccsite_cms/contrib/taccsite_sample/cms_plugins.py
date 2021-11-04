from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_text

from .models import TaccsiteSample

from .defaults import user_name as default_name
from .utils import has_proper_name

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
    allow_children = False
    # NOTE: Use case is unclear
    # admin_preview = True
    # NOTE: To change for all TACC plugins add taccsite_cms/templates/admin/...
    # change_form_template = 'templates/plugin_change_form.html'
    # NOTE: To change field widget and other attribute beyond `models.…Field`
    #       (Optionally, consider `formfield_overrides`:
    #        https://django.readthedocs.io/en/latest/ref/contrib/admin/index.html#django.contrib.admin.ModelAdmin.formfield_overrides)
    # form = TaccsiteSamplePluginForm # TODO: Provide example

    # FAQ: Sets tooltip of preview of this plugin within a Text plugin
    def icon_alt(self, instance):
        super_value = force_text(super().icon_alt(instance))
        return f'Hello, […] ({super_value})'
    # NOTE: Our previews (see `icon_alt`) are rich and have no icon...
    # TODO: Confirm whether these are ever necessary
    # def icon_src(self, instance)
    # def text_editor_button_icon(...)

    # Render

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        request = context['request']

        context.update({
            'name': instance.get_name(request.user),
            'has_proper_name': has_proper_name(request.user),
            'is_authenticated': request.user.is_authenticated
        })
        return context
