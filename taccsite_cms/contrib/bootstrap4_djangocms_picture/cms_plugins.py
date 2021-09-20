# To support generic Image plugin without uninstalling Bootstrap's
# FAQ: Bootstrap Image plugin has features not desirable in TACC plugins
# FAQ: We must not break sites that already use Bootstrap Image plugin
try:
    from django.utils.translation import gettext as _

    from cms.plugin_pool import plugin_pool

    from djangocms_picture.cms_plugins import PicturePlugin
    from djangocms_bootstrap4.contrib.bootstrap4_picture.cms_plugins import Bootstrap4PicturePlugin

    # To signal to users that plugin is not desirable
    Bootstrap4PicturePlugin.name = _('⚠️ Picture / Image')
    Bootstrap4PicturePlugin.fieldsets.insert(0, (
        None, {
            'description': _('⚠️ This plugin is <strong>deprecated</strong>. Please use "Generic" > "Image" plugin instead.<br /><small>If the "Generic" > "Image" plugin is inadequate, please inform the CMS development team.</small>'),
            'fields': ()
        }
    ))

    # To re-register generic Picture plugin
    # SEE: https://github.com/django-cms/djangocms-bootstrap4/blob/master/djangocms_bootstrap4/contrib/bootstrap4_picture/cms_plugins.py#L54
    plugin_pool.register_plugin(PicturePlugin)

# To avoid server crash if Boostrap plugin is not registered
# CAVEAT: If import statement fails for reason other than Bootstrap presence,
#         then that failure, and the failure of this plugin, is silent
except ImportError:
    pass
