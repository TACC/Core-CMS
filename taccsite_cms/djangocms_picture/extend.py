import logging

logger = logging.getLogger(f"django.{__name__}")

def extendPicturePlugin():
    from django.core.exceptions import ValidationError
    from django.utils.translation import gettext_lazy as _

    from cms.plugin_pool import plugin_pool

    from djangocms_link.cms_plugins import LinkPlugin

    ZOOM_TEMPLATE_NAME_PREFIX = 'zoom'
    ZOOM_TEMPLATE_LABEL = 'Zoom image on hover'
    ZOOM_TEMPLATE_NOTE = _('The "%(zoom_template_label)s" templates only have effect if Image either has a Link or is within a Link.') % {"zoom_template_label": ZOOM_TEMPLATE_LABEL}
    ZOOM_TEMPLATE_ERROR = _(' "%(zoom_template_label)s" templates require Image to either have a Link or be within a Link.') % {"zoom_template_label": ZOOM_TEMPLATE_LABEL}

    logger.info("Extending PicturePlugin (and Bootstrap4PicturePlugin)...")

    def add_help_text(form_instance):
        """Adds help text for: 'Template' field"""

        if 'template' in form_instance.fields:
            form_instance.fields['template'].help_text += _(' %(ZOOM_TEMPLATE_NOTE)s') % {"ZOOM_TEMPLATE_NOTE": ZOOM_TEMPLATE_NOTE}


    def validate_zoom_template(instance):
        """Validates: 'Template' field choice 'Zoom image …'"""

        errors = {}

        has_picture_link = bool(instance.link_url or instance.link_page_id)
        use_zoom_template = ZOOM_TEMPLATE_NAME_PREFIX in instance.template
        parent_plugin = instance.parent.get_plugin_instance()[0] if instance.parent else None
        is_in_link = isinstance(parent_plugin, LinkPlugin) if parent_plugin else False

        logger.info(f'validate_zoom_template: %s', {
            'link': instance.link_url or instance.link_page_id,
            'has_picture_link' : has_picture_link,
            'use_zoom_template' : use_zoom_template,
            'is_in_link': is_in_link,
        })

        if (use_zoom_template and not has_picture_link and not is_in_link ):
            errors['template'] = ZOOM_TEMPLATE_ERROR

        if errors:
            raise ValidationError(errors)


    # djangocms_picture
    from djangocms_picture.cms_plugins import PicturePlugin as OriginalPicturePlugin
    from djangocms_picture.models import Picture as OriginalPicture

    class PicturePluginForm(OriginalPicturePlugin.form):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            add_help_text(self)

    class PicturePluginModel(OriginalPicture):
        class Meta:
            proxy = True

        def clean(self):
            super().clean()
            validate_zoom_template(self)

    class PicturePlugin(OriginalPicturePlugin):
        model = PicturePluginModel
        form = PicturePluginForm
        name = 'Image'

    # To support generic Image plugin without uninstalling Bootstrap's
    # FAQ: Had been done cuz Image plugin had percieved use cases,
    #      but is since not regularly used, but is used, thus maintained
    # FAQ: No need to unregister cuz Bootstrap4PicturePlugin does that
    # https://github.com/django-cms/djangocms-bootstrap4/blob/3.0.0/djangocms_bootstrap4/contrib/bootstrap4_picture/cms_plugins.py#L54
    # plugin_pool.unregister_plugin(OriginalPicturePlugin)
    plugin_pool.register_plugin(PicturePlugin)


    # djangocms_bootstrap4: bootstrap4_picture
    from djangocms_bootstrap4.contrib.bootstrap4_picture.cms_plugins import Bootstrap4PicturePlugin as OriginalBootstrap4PicturePlugin
    from djangocms_bootstrap4.contrib.bootstrap4_picture.models import Bootstrap4Picture as OriginalBootstrap4Picture

    class Bootstrap4PictureForm(OriginalBootstrap4PicturePlugin.form):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            add_help_text(self)

    class Bootstrap4PictureModel(OriginalBootstrap4Picture):
        class Meta:
            proxy = True

        def clean(self):
            super().clean()
            validate_zoom_template(self)

    class Bootstrap4PicturePlugin(OriginalBootstrap4PicturePlugin):
        model = Bootstrap4PictureModel
        form = Bootstrap4PictureForm
        name = 'Picture / Image (Responsive)'

    plugin_pool.unregister_plugin(OriginalBootstrap4PicturePlugin)
    plugin_pool.register_plugin(Bootstrap4PicturePlugin)

    logger.info("Extended PicturePlugin (and Bootstrap4PicturePlugin).")
