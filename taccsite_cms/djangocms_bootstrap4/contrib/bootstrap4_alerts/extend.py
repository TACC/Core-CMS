import copy


# Map Bootstrap alert contexts to Core-Styles admonition type classes
# (colors + default ::before icon treatment in admonition.css).
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
    from djangocms_bootstrap4.helpers import concat_classes

    class Bootstrap4AlertsPlugin(OriginalBootstrap4AlertsPlugin):
        model = OriginalBootstrap4Alerts
        render_template = 'djangocms_bootstrap4/alert.html'

        fieldsets = list(copy.deepcopy(OriginalBootstrap4AlertsPlugin.fieldsets))

        def render(self, context, instance, placeholder):
            admonition_type = ALERT_CONTEXT_TO_ADMONITION_TYPE.get(
                instance.alert_context,
                'note',
            )
            link_classes = [
                'admonition',
                admonition_type,
            ]
            classes = concat_classes(link_classes + [
                instance.attributes.get('class'),
            ])
            instance.attributes['class'] = classes
            instance.tag_type = 'div'

            return super(OriginalBootstrap4AlertsPlugin, self).render(
                context, instance, placeholder
            )

    plugin_pool.unregister_plugin(OriginalBootstrap4AlertsPlugin)
    plugin_pool.register_plugin(Bootstrap4AlertsPlugin)
