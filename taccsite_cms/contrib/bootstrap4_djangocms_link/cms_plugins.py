# Reregister unregistered LinkPlugin without uninstalling Bootstrap4's
# FAQ: A Bootstrap link is undesirable but may be used by migrated legacy sites
# TODO: Drop try/except & load non-standard plugin set for migrated legacy sites
# FAQ: If we can import both plugins, then re-register LinkPlugin
#      (because Bootstrap4Link unregistered LinkPlugin)
try:
    from cms.plugin_pool import plugin_pool
    from djangocms_link.cms_plugins import LinkPlugin
    from djangocms_bootstrap4.contrib.bootstrap4_link.cms_plugins import Bootstrap4LinkPlugin

    # Restore original fields
    # SEE: https://github.com/django-cms/djangocms-bootstrap4/blob/2.0.0/djangocms_bootstrap4/contrib/bootstrap4_link/cms_plugins.py#L26-L42
    # SEE: https://github.com/django-cms/djangocms-link/blob/3.0.0/djangocms_link/cms_plugins.py#L20-L23
    LinkPlugin.fieldsets[0][1]['fields'] = (
        'name',
        ('external_link', 'internal_link'),
    )

    # SEE: https://github.com/django-cms/djangocms-link/issues/163
    plugin_pool.register_plugin(LinkPlugin)
# CAVEAT: If import statement fails for reason other than Bootstrap presence,
#         then that failure, and the failure of this plugin, is silent
except ImportError:
    pass
