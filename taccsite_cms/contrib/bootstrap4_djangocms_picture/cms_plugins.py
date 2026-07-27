# To support generic Image plugin without uninstalling Bootstrap's
# FAQ: Bootstrap Image plugin has features not desirable in TACC plugins
# FAQ: We must not break sites that already use Bootstrap Image plugin
try:
    from django.utils.translation import gettext as _

    from cms.plugin_pool import plugin_pool

    from djangocms_picture.cms_plugins import PicturePlugin
    from djangocms_bootstrap4.contrib.bootstrap4_picture.cms_plugins import Bootstrap4PicturePlugin

    # To clairfy for users how this plugin differs from Generic > Image
    Bootstrap4PicturePlugin.name = _('Picture / Image (Responsive)')

    # To re-register generic Picture plugin
    # SEE: https://github.com/django-cms/djangocms-bootstrap4/blob/master/djangocms_bootstrap4/contrib/bootstrap4_picture/cms_plugins.py#L54
    plugin_pool.register_plugin(PicturePlugin)

# To avoid server crash if Boostrap plugin is not registered
# CAVEAT: If import statement fails for reason other than Bootstrap presence,
#         then that failure, and the failure of this plugin, is silent
except ImportError:
    pass
