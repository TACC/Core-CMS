from cms.models import Page
from django.contrib.sites.models import Site
from djangocms_picture.forms import PictureForm


def default_home_page():
    site = Site.objects.get_current()
    return Page.objects.filter(is_home=True, node__site=site).first()


class HeaderLogoForm(PictureForm):
    """
    Defaults for new Header logo plugins only (admin add form).
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            return

        home = default_home_page()
        if home is not None:
            self.initial.setdefault('link_page', home.pk)

        self.initial.setdefault('use_no_cropping', True)
        self.initial.setdefault('use_automatic_scaling', False)

