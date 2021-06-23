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

def get_direction_classname(value):
    """Get direction class based on value."""

    # TODO: Couple this map to DIRECTION_CHOICES
    switcher = {
        'right': 'o-offset-content--right',
        'left': 'o-offset-content--left'
    }

    return switcher.get(value, '')



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
