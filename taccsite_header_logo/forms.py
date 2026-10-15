from cms.models import Page
from django.conf import settings
from django.contrib.sites.models import Site
from djangocms_picture.forms import PictureForm

HEADER_LOGO_TEMPLATE_WITH_PORTAL = 'portal_logo'


def default_home_page():
    site = Site.objects.get_current()
    return Page.objects.filter(is_home=True, node__site=site).first()


class TaccsiteHeaderLogoForm(PictureForm):
    """
    Defaults for new Header logo plugins only (admin add form).

    On a TACC/Core-Portal instance, defaults to Portal logo picture template.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            return

        if settings.PORTAL_IS_TACC_CORE_PORTAL:
            self.initial.setdefault('template', HEADER_LOGO_TEMPLATE_WITH_PORTAL)

        home = default_home_page()
        if home is not None:
            self.initial.setdefault('link_page', home.pk)

        self.initial.setdefault('use_no_cropping', True)
        self.initial.setdefault('use_automatic_scaling', False)

        attributes = dict(self.initial.get('attributes') or {})
        attributes.setdefault('alt', 'Project logo')
        self.initial['attributes'] = attributes
