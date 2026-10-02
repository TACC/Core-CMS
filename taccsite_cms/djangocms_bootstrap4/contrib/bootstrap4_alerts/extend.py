import copy

from djangocms_bootstrap4.helpers import concat_classes

ALERT_PRESENTATION_ATTR = 'data-cms-alert-style'
ALERT_PRESENTATION_BOOTSTRAP = 'bootstrap'
ALERT_PRESENTATION_ADMONITION = 'admonition'

ADMONITION_TEMPLATE = 'djangocms_bootstrap4/alert.html'
BOOTSTRAP_TEMPLATE = 'djangocms_bootstrap4/alerts.html'

# Map Bootstrap alert contexts to Core-Styles admonition type classes.
ALERT_CONTEXT_TO_ADMONITION_TYPE = {
    'primary': 'tip',
    'secondary': 'note',
    'success': 'hint',
    'danger': 'danger',
    'warning': 'warning',
    'info': 'note',
    'light': 'note',
    'dark': 'note',
}


def get_alert_presentation(instance):
    attrs = instance.attributes or {}
    return attrs.get(ALERT_PRESENTATION_ATTR, ALERT_PRESENTATION_BOOTSTRAP)


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

        fieldsets = list(copy.deepcopy(OriginalBootstrap4AlertsPlugin.fieldsets))
        fieldsets[0][1]['fields'] = (
            'alert_presentation',
            'alert_context',
            'alert_dismissable',
        )

        def get_render_template(self, context, instance, placeholder):
            if get_alert_presentation(instance) == ALERT_PRESENTATION_ADMONITION:
                return ADMONITION_TEMPLATE
            return BOOTSTRAP_TEMPLATE

        def render(self, context, instance, placeholder):
            presentation = get_alert_presentation(instance)
            extra_class = (instance.attributes or {}).get('class')

            if presentation == ALERT_PRESENTATION_ADMONITION:
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
