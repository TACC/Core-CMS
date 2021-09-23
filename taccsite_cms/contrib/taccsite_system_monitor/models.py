from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext as _

from django.db import models

from djangocms_attributes_field import fields

from taccsite_cms.contrib.helpers import get_choices

from .constants import DEFAULT_SYSTEM

# TODO: (Maybe in GH-295) Do not replicate `display_name` data from API
SYSTEM_DICT = {
    'frontera.tacc.utexas.edu': {
        'description': 'Frontera'
    },
    'stampede2.tacc.utexas.edu': {
        'description': 'Stampede2'
    },
    'maverick2.tacc.utexas.edu': {
        'description': 'Maverick2'
    },
    'longhorn.tacc.utexas.edu': {
        'description': 'Longhorn'
    },
}
SYSTEM_CHOICES = get_choices(SYSTEM_DICT)

class TaccsiteSystemMonitor(CMSPlugin):
    """
    Components > "System Monitor" Model
    """
    system = models.CharField(
        verbose_name=_('System'),
        choices=SYSTEM_CHOICES,
        blank=False,
        max_length=255,
        default=DEFAULT_SYSTEM,
    )

    attributes = fields.AttributesField()

    def get_short_description(self):
        system_choice = SYSTEM_DICT[self.system]
        return system_choice['description']
