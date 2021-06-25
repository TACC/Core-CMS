from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from django.db import models

from djangocms_attributes_field import fields

# Constants

LAYOUT_CHOICES = (
    ('always-rows-N--even',  _('(always) N Even Rows')),
    ('widest-cols-2--even', _('(at widest) 2 Equal Columns')),
    ('widest-cols-2--wide-narr', _('(at widest) 2 Cols: 1 Wide, 1 Narrow')),
    ('widest-cols-2--narr-wide', _('(at widest) 2 Cols: 1 Narrow, 1 Wide')),
    ('widest-cols-3--even', _('(at widest) 3 Equal Columns')),
)
STYLE_CHOICES = (
    ('divided', _('Dividers Between Articles')),
)

# Models

class TaccsiteArticleList(CMSPlugin):
    """
    Components > "Article List" Model
    https://confluence.tacc.utexas.edu/x/OIAjCQ
    """
    header_title_text = models.CharField(
        help_text='The title at the top of the list.',
        blank=True,
        max_length=100,
    )
    footer_link_text = models.CharField(
        help_text='The "See All" link at the bottom of the list.',
        blank=True,
        max_length=100,
    )
    # TODO: Add `footer_link_url`

    layout_type = models.CharField(
        choices=LAYOUT_CHOICES,
        default=LAYOUT_CHOICES[0][0],
        blank=True,
        max_length=255,
    )
    style_type = models.CharField(
        choices=STYLE_CHOICES,
        blank=True,
        max_length=255,
    )

    attributes = fields.AttributesField()

    def get_short_description(self):
        return self.header_title_text
