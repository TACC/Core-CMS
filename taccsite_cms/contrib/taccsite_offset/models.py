from cms.models.pluginmodel import CMSPlugin

from django.db import models
from django.utils.translation import gettext_lazy as _

from djangocms_attributes_field import fields

from taccsite_cms.contrib.helpers import get_choices

# Constants

DIRECTION_DICT = {
    'left': {
        'classname':    'o-offset-content--left',
        'description':  'Left',
    },
    'right': {
        'classname':    'o-offset-content--right',
        'description':  'Right',
    },
}
DIRECTION_CHOICES = get_choices(DIRECTION_DICT)



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
