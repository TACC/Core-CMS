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

    def get_more_context_variables(instance):
        """
        Calculate boolean context variables to simplify template logic.
        Returns a dictionary of context variables.
        """
        # Link (set 1)
        has_explicit_link = bool(instance.link_url or instance.link_page_id)
        parent_plugin = instance.parent.get_plugin_instance()[0] if instance.parent else None
        is_in_link_plugin = isinstance(parent_plugin, LinkPlugin) if parent_plugin else False
        has_any_link = has_explicit_link or is_in_link_plugin

        # Figure/Caption
        has_caption_text = bool(instance.caption_text)
        has_child_plugins = bool(instance.child_plugin_instances)
        has_figure_content = has_caption_text or has_child_plugins

        # Template
        template_name = getattr(instance, 'template', '')
        is_zoom_template = ZOOM_TEMPLATE_NAME_PREFIX in template_name
        is_no_link_template = 'no_link_to_image' in template_name

        # Link (set 2)
        should_render_link = has_explicit_link
        # To link to image to itself by default
        # FAQ: This default behavior is retained from djangocms_picture
        if not is_no_link_template and not has_explicit_link:
            should_render_link = True

        # Zoom Effect
        should_add_zoom_effect = is_zoom_template and has_any_link
        should_wrap_image_for_zoom = (
            should_add_zoom_effect and
            (has_figure_content or not should_render_link)
        )
        should_add_zoom_class_to_link = (
            should_add_zoom_effect and
            should_render_link and
            not has_figure_content
        )

        # Attributes
        should_add_attributes_to_image = (
            not has_figure_content and
            not should_render_link
        )

        return {
            # Link
            'has_explicit_link': has_explicit_link,
            'is_in_link_plugin': is_in_link_plugin,
            'has_any_link': has_any_link,
            'should_render_link': should_render_link,

            # Figure/Caption
            'has_caption_text': has_caption_text,
            'has_child_plugins': has_child_plugins,
            'has_figure_content': has_figure_content,

            # Template
            'is_zoom_template': is_zoom_template,
            'is_no_link_template': is_no_link_template,

            # Zoom Effect
            'should_add_zoom_effect': should_add_zoom_effect,
            'should_wrap_image_for_zoom': should_wrap_image_for_zoom,
            'should_add_zoom_class_to_link': should_add_zoom_class_to_link,

            # Attributes
            'should_add_attributes_to_image': should_add_attributes_to_image,
        }


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

        def render(self, context, instance, placeholder):
            context = super().render(context, instance, placeholder)

            more_context = get_more_context_variables(instance)
            context.update(more_context)

            return context

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

        def render(self, context, instance, placeholder):
            context = super().render(context, instance, placeholder)

            more_context = get_more_context_variables(instance)
            context.update(more_context)

            return context

    plugin_pool.unregister_plugin(OriginalBootstrap4PicturePlugin)
    plugin_pool.register_plugin(Bootstrap4PicturePlugin)

    logger.info("Extended PicturePlugin (and Bootstrap4PicturePlugin).")
