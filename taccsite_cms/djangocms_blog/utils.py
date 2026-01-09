def is_app_installed():
    """Whether djangocms_blog is installed"""
    from django.apps import apps
    return apps.is_installed('djangocms_blog')
