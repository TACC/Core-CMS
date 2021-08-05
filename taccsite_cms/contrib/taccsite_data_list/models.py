from cms.models.pluginmodel import CMSPlugin

from django.db import models
from django.utils.translation import gettext_lazy as _

from djangocms_attributes_field import fields

from taccsite_cms.contrib.helpers import get_choices

from .constants import ORIENTATION_DICT, TYPE_STYLE_DICT, DENSITY_DICT



# Constants

ORIENTATION_CHOICES = get_choices(ORIENTATION_DICT)
TYPE_STYLE_CHOICES = get_choices(TYPE_STYLE_DICT)
DENSITY_CHOICES = get_choices(DENSITY_DICT)



# Models

class TaccsiteDataList(CMSPlugin):
    """
    Components > "Data List" Model
    """
    orientation = models.CharField(
        verbose_name=_('Orientation'),
        help_text=_('The direction in which to lay out the data. Hint: Choose based on the amount of space available in the layout for the data.'),
        choices=ORIENTATION_CHOICES,
        blank=False,
        max_length=255,
    )
    type_style = models.CharField(
        verbose_name=_('Type / Style'),
        help_text=_('The type of data to display, glossary/metadata or tabular. Notice: Each type of list has a slightly different style.'),
        choices=TYPE_STYLE_CHOICES,
        blank=False,
        max_length=255,
    )
    density = models.CharField(
        verbose_name=_('Density (Layout Spacing)'),
        help_text=_('The amount of extra space in the layout. Hint: Choose based on the amount of space available in the layout for the data.'),
        choices=DENSITY_CHOICES,
        blank=False,
        max_length=255,
    )
    truncate_values = models.BooleanField(
        verbose_name=_('Truncate the values (as necessary)'),
        help_text=_('Truncate values if there is not enough space to show the label and the value. Notice: Labels are truncated as necessary.'),
        default=False,
    )

    attributes = fields.AttributesField()

    def get_short_description(self):
        orientation = ORIENTATION_DICT[self.orientation]['short_description']
        type_style = TYPE_STYLE_DICT[self.type_style]['short_description']
        density = DENSITY_DICT[self.density]['short_description']

        return density + ', ' + orientation + ' ' + type_style
