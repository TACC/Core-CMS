from django.conf import settings

def cms_excluded_plugins(request):
    """
    Plugin names from CMS_PLACEHOLDER_CONF[None]['excluded_plugins']
    """
    placeholder_defaults = settings.CMS_PLACEHOLDER_CONF.get(None) or {}
    return {
        'cms_excluded_plugins': placeholder_defaults.get('excluded_plugins') or [],
    }
