def extendPicturePlugin():
    from django.utils.translation import gettext_lazy as _

    from cms.plugin_pool import plugin_pool

    ZOOM_TEMPLATE_NAME = 'zoom_effect'
    ZOOM_TEMPLATE_LABEL = 'Zoom image on hover'
    ZOOM_TEMPLATE_NOTE = _('The "%(zoom_template_label)s" templates only have effect if Image either has a Link or is within a Link.') % {"zoom_template_label": ZOOM_TEMPLATE_LABEL}
    ZOOM_TEMPLATE_ERROR = _(' "%(zoom_template_label)s" templates require Image to either have a Link or be within a Link.') % {"zoom_template_label": ZOOM_TEMPLATE_LABEL}

    LINK_TEMPLATE_NAME = 'no_link_to_ext_image'

    def add_help_text(form_instance):
        """Adds help text for: 'Template' field"""

        if 'template' in form_instance.fields:
            form_instance.fields['template'].help_text += _(' %(ZOOM_TEMPLATE_NOTE)s') % {"ZOOM_TEMPLATE_NOTE": ZOOM_TEMPLATE_NOTE}

    def whether_to_render_link(instance):
        has_explicit_link = bool(instance.link_url or instance.link_page_id)
        # FAQ: The djangocms_picture has "feature" such that an image with
        #      "External image" URL will automatically link to that resource
        has_implicit_link = bool(instance.get_link()) and not has_explicit_link

        allow_implicit_link = not LINK_TEMPLATE_NAME in instance.template

        if has_explicit_link or (has_implicit_link and allow_implicit_link):
            return True

        return False

    def validate_zoom_template(instance):
        """Validates: 'Template' field choice 'Zoom image …'"""
        from django.core.exceptions import ValidationError
        from djangocms_link.cms_plugins import LinkPlugin

        errors = {}

        would_render_link = whether_to_render_link(instance)
        should_add_zoom_effect = ZOOM_TEMPLATE_NAME in instance.template
        parent_plugin = instance.parent.get_plugin_instance()[0] if instance.parent else None
        is_in_link = instance.parent.plugin_type == 'LinkPlugin' if instance.parent else False

        if (should_add_zoom_effect and not would_render_link and not is_in_link):
            errors['template'] = ZOOM_TEMPLATE_ERROR

        if errors:
            raise ValidationError(errors)

    def get_more_context_variables(instance):
        """
        Calculate boolean context variables to simplify template logic.
        Returns a dictionary of context variables.
        """
        # Figure/Caption
        has_caption_text = bool(instance.caption_text)
        has_child_plugins = bool(instance.child_plugin_instances)
        has_figure_content = has_caption_text or has_child_plugins

        # Template
        is_zoom_template = ZOOM_TEMPLATE_NAME in instance.template

        # Link
        should_render_link = whether_to_render_link(instance)

        # Zoom Effect
        should_add_zoom_effect = is_zoom_template
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
            'should_render_link': should_render_link,
            'has_figure_content': has_figure_content,
            'should_wrap_image_for_zoom': should_wrap_image_for_zoom,
            'should_add_zoom_class_to_link': should_add_zoom_class_to_link,
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
