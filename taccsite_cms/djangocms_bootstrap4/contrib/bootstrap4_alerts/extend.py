from django.utils.translation import gettext_lazy as _

from djangocms_bootstrap4.helpers import concat_classes

from .appearance import (
    ALERT_APPEARANCE_ADMONITION,
    ALERT_APPEARANCE_BOOTSTRAP,
    get_alert_appearance,
)

ADMONITION_TEMPLATE = 'djangocms_bootstrap4/alert.html'
BOOTSTRAP_TEMPLATE = 'djangocms_bootstrap4/alerts.html'

# Map Bootstrap alert contexts to Core-Styles admonition type classes.
ALERT_CONTEXT_TO_ADMONITION_TYPE = {
    'primary': 'tip',
    'secondary': 'note',
    'success': 'hint',
    'danger': 'danger',
    'warning': 'caution',
    'info': 'note',
    'light': 'note',
    'dark': 'note',
}


def extendBootstrap4AlertsPlugin():
    # IMPORTANT: Do not use a proxy model, or else GH-1099
    # https://github.com/TACC/Core-CMS/issues/1099

    from cms.plugin_pool import plugin_pool

    from djangocms_bootstrap4.contrib.bootstrap4_alerts.cms_plugins import (
        Bootstrap4AlertsPlugin as OriginalBootstrap4AlertsPlugin,
    )
    from djangocms_bootstrap4.contrib.bootstrap4_alerts.models import (
        Bootstrap4Alerts as OriginalBootstrap4Alerts,
    )

    from .forms import Bootstrap4AlertForm

    class Bootstrap4AlertsPlugin(OriginalBootstrap4AlertsPlugin):
        model = OriginalBootstrap4Alerts
        form = Bootstrap4AlertForm
        change_form_template = (
            'djangocms_bootstrap4/admin/alerts.html'
        )

        def get_fieldsets(self, request, obj=None):
            return [
                (None, {
                    'fields': (
                        'alert_appearance',
                        'alert_context',
                        'alert_dismissable',
                    ),
                }),
                (_('Advanced settings'), {
                    'classes': ('collapse',),
                    'fields': ('tag_type',),
                }),
            ]

        def get_form(self, request, obj=None, change=False, **kwargs):
            kwargs.setdefault('form', Bootstrap4AlertForm)
            return super().get_form(request, obj, change=change, **kwargs)

        def get_render_template(self, context, instance, placeholder):
            if get_alert_appearance(instance) == ALERT_APPEARANCE_ADMONITION:
                return ADMONITION_TEMPLATE
            return BOOTSTRAP_TEMPLATE

        def render(self, context, instance, placeholder):
            appearance = get_alert_appearance(instance)
            extra_class = (instance.attributes or {}).get('class')

            if appearance == ALERT_APPEARANCE_ADMONITION:
                admonition_type = ALERT_CONTEXT_TO_ADMONITION_TYPE.get(
                    instance.alert_context,
                    'note',
                )
                classes = concat_classes([
                    'admonition',
                    admonition_type,
                    extra_class,
                ])
                instance.tag_type = 'div'
            else:
                classes = concat_classes([
                    'alert',
                    f'alert-{instance.alert_context}',
                    extra_class,
                ])

            if instance.attributes is None:
                instance.attributes = {}
            instance.attributes['class'] = classes

            from cms.plugin_base import CMSPluginBase

            return CMSPluginBase.render(
                self, context, instance, placeholder,
            )

    plugin_pool.unregister_plugin(OriginalBootstrap4AlertsPlugin)
    plugin_pool.register_plugin(Bootstrap4AlertsPlugin)
