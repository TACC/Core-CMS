def extendPicturePlugin():
    from djangocms_picture.cms_plugins import PicturePlugin

    class ExtendedPicturePluginForm(PicturePlugin.form):
        """Extended form with additional fields or help text"""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if 'template' in self.fields:
                zoom_template_name = "Zoom image on hover"
                self.fields['template'].help_text += f' "{zoom_template_name}" only works with Images that have links or are within links.'

    PicturePlugin.form = ExtendedPicturePluginForm
