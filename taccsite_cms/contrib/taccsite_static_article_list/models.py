from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from django.db import models

from djangocms_attributes_field import fields

# Constants

CONTENT_CHOICES = (
    ('news', _('News')),
    ('docs', _('Documents')),
    ('allocs', _('Allocations')),
    ('events', _('Events')),
)
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

# Helpers

def get_content_classname(value):
    """Get content class based on value."""

    # TODO: Couple this map to TYPE_CHOICES
    switcher = {
        'news': 's-article-list--news',
        'docs': 's-article-list--links',
        'allocs': 's-article-list--allocations',
        'events': 's-article-list--events',
    }

    return switcher.get(value, '')

def get_layout_classname(value):
    """Get layout class based on value."""

    # TODO: Couple this map to LAYOUT_CHOICES
    switcher = {
        'widest-cols-2--even': 'c-article-list--layout-a',
        'widest-cols-2--wide-narr': 'c-article-list--layout-b',
        'widest-cols-2--narr-wide': 'c-article-list--layout-c',
        'widest-cols-3--even': 'c-article-list--layout-d',
        'always-rows-N--even': 'c-article-list--layout-e',
    }

    return switcher.get(value, '')

def get_style_classname(value):
    """Get style class based on value."""

    # TODO: Couple this map to STYLE_CHOICES
    switcher = {
        'divided': 'c-article-list--style-divided',
    }

    return switcher.get(value, '')

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
        help_text='The "See All ..." link at the bottom of the list.',
        blank=True,
        max_length=100,
    )
    # TODO: Add `footer_link_url`

    content_type = models.CharField(
        choices=CONTENT_CHOICES,
        blank=True,
        max_length=255,
    )
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
