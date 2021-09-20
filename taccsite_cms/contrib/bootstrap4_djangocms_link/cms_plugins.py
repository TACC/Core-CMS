# To support generic Link plugin without uninstalling Bootstrap4's
# FAQ: Bootstrap Link plugin has features not desirable within TACC plugins
# FAQ: We must not break sites that already use Bootstrap Link plugin
try:
    # CAVEAT: Solution must be more than that for `bootstrap4_djangocms_picture`
    # SEE: https://github.com/django-cms/djangocms-bootstrap4/pull/138
    import copy

    from django.utils.translation import gettext as _

    from cms.plugin_pool import plugin_pool

    from djangocms_link.cms_plugins import LinkPlugin
    from djangocms_bootstrap4.contrib.bootstrap4_link.cms_plugins import Bootstrap4LinkPlugin

    # To unlink Bootstrap's plugin fieldsets from Generic's
    # SEE: https://github.com/django-cms/djangocms-bootstrap4/blob/2.0.0/djangocms_bootstrap4/contrib/bootstrap4_link/cms_plugins.py#L44
    Bootstrap4LinkPlugin.fieldsets = copy.deepcopy(Bootstrap4LinkPlugin.fieldsets)

    # To restore generic Link plugin fieldsets to state before Bootstrap's
    # SEE: https://github.com/django-cms/djangocms-link/blob/3.0.0/djangocms_link/cms_plugins.py#L19-L24
    # SEE: https://github.com/django-cms/djangocms-bootstrap4/blob/2.0.0/djangocms_bootstrap4/contrib/bootstrap4_link/cms_plugins.py#L38-L42
    LinkPlugin.fieldsets[0] = (
        None, {
            'fields': (
                'name',
                ('external_link', 'internal_link'),
            )
        }
    )

    # To signal to users that plugin is not desirable
    Bootstrap4LinkPlugin.name = _('⚠️ Link / Button')
    Bootstrap4LinkPlugin.fieldsets.insert(0, (
        None, {
            'description': _('⚠️ This plugin is <strong>deprecated</strong>. Please use "Generic" > "Link" plugin instead.<br /><small>If the "Generic" > "Link" plugin is inadequate, please inform the CMS development team.</small>'),
            'fields': ()
        }
    ))

    # To re-register generic Link plugin
    # SEE: https://github.com/django-cms/djangocms-bootstrap4/blob/master/djangocms_bootstrap4/contrib/bootstrap4_link/cms_plugins.py#L81
    plugin_pool.register_plugin(LinkPlugin)

# To avoid server crash if Boostrap plugin is not registered
# CAVEAT: If import statement fails for reason other than Bootstrap presence,
#         then that failure, and the failure of this plugin, is silent
except ImportError:
    pass
