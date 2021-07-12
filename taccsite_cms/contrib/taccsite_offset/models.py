# SEE: https://github.com/django-cms/djangocms-bootstrap4/blob/2.0.0/djangocms_bootstrap4/contrib/bootstrap4_content/models.py

from cms.models.pluginmodel import CMSPlugin

from django.db import models
from django.utils.translation import gettext_lazy as _

from djangocms_attributes_field import fields



# Constants

DIRECTION_CHOICES = (
    ('left', _('Left')),
    # ('center', _('Center')), # GH-66: Support centered offset content
    ('right', _('Right')),
)

# Helpers

def get_direction_classname(offset):
    """Get offset content class based on standard offset value."""

    # HELP: Should we limit input by coupling this map to DIRECTION_CHOICES?
    switcher = {
        'right': 'o-offset-content--right',
        'left': 'o-offset-content--left'
    }

# Models

class TaccsiteOffset(CMSPlugin):
    """
    Components > "Offset Content" Model
    https://confluence.tacc.utexas.edu/x/GIEjCQ
    """
    direction = models.CharField(
        choices=DIRECTION_CHOICES,
        blank=True,
        max_length=255,
    )

    attributes = fields.AttributesField()

    def get_short_description(self):
        return self.direction
