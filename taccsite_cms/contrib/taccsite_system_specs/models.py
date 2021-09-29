from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.db import models

from djangocms_link.models import AbstractLink

from taccsite_cms.contrib.helpers import clean_for_abstract_link

from .constants import DEFAULT_OTHER_TITLE

class TaccsiteSystemSpecs(AbstractLink):
    """
    Components > "System Specs" Model
    """
    system_desc = models.TextField(
        verbose_name=_('System Description'),
        help_text=_('Description of the system machine and mission.'),
        blank=False,
        max_length=500,
        default=''
    )
    system_processor_count = models.IntegerField(
        verbose_name=_('Processors'),
        help_text=_('The number of processors in the system'),
        blank=True,
        null=True,
        # HELP: Is it worth it to create a min. value zero to avoid neg. values?
        # SEE: https://stackoverflow.com/a/849426/11817077
        # min_value=0,
    )
    system_processor_type = models.CharField(
        verbose_name=_('Processor Type'),
        help_text=_('The number of processors in the system'),
        blank=True,
        max_length=50,
    )
    system_node_ram = models.CharField(
        verbose_name=_('RAM per Node'),
        help_text=_('The amount of RAM in each node of the system, including the unit. (Reminder: Type "GB" for Gigabyte, not "Gb".)'),
        blank=True,
        max_length=50,
    )
    system_network = models.CharField(
        verbose_name=_('Network'),
        help_text=_('The network hardware in the system. (Reminder: Type "Gb" for Gigabit, not GB.)'),
        blank=True,
        max_length=50,
    )
    system_performance = models.CharField(
        verbose_name=_('Peak Performance'),
        help_text=_('The peak performance of the system, including the unit. (Reminder: Type number, then space, then unit; example: "38.8 PetaFLOPS".)'),
        blank=True,
        max_length=50,
    )
    system_memory = models.CharField(
        verbose_name=_('Memory'),
        help_text=_('The amount of memory for the system, including the unit. (Reminder: Type "PB" for Petabyte, not "Pb".)'),
        blank=True,
        max_length=50,
    )

    other_title = models.CharField(
        verbose_name=_('Alternate Resources Title'),
        help_text=_('An alternate title to replace "%(default_value)s".') % { 'default_value': DEFAULT_OTHER_TITLE },
        blank=True,
        max_length=40, # Based on approx. space available in design
    )
    other_desc = models.TextField(
        verbose_name=_('Resources Description'),
        help_text=_('Description of "%(default_value)s".') % { 'default_value': DEFAULT_OTHER_TITLE },
        blank=True,
        max_length=500,
        default=''
    )

    def get_short_description(self):
        return self.system_desc



    # Parent

    link_is_optional = True

    class Meta:
        abstract = False

    # Validate
    def clean(self):
        clean_for_abstract_link(__class__, self)

        # If user provided link text, then require link
        if self.name and not self.get_link():
            raise ValidationError(
                _('Please provide a footer link or delete its display name.'), code='invalid'
            )
