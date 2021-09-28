from cms.models.pluginmodel import CMSPlugin

from django.db import models
from django.utils.translation import gettext as _

from djangocms_attributes_field import fields

from taccsite_cms.contrib.helpers import get_choices

from .constants import ORIENTATION_DICT, TYPE_STYLE_DICT, DENSITY_DICT



# Helpers

def get_short_description(dict, value):
    """Get layout class based on value."""
    return dict.get(value, {}).get('short_description')



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
        orientation = get_short_description(ORIENTATION_DICT, self.orientation)
        type_style = get_short_description(TYPE_STYLE_DICT, self.type_style)
        density = get_short_description(DENSITY_DICT, self.density)

        return density + ', ' + orientation + ' ' + type_style

class TaccsiteDataListItem(CMSPlugin):
    """
    Components > "Data List Item" Model
    """
    key = models.CharField(
        verbose_name=_('Label'),
        help_text=_('A label for the data value.'),
        blank=True,
        max_length=50,
    )
    value = models.CharField(
        verbose_name=_('Value'),
        help_text=_('The data value.'),
        blank=False,
        max_length=100,
    )
    use_plugin_as_key = models.BooleanField(
        verbose_name=_('Support child plugin for Label'),
        help_text=_('If a child plugin is added, and this option is checked, then the child plugin will be used (not the Label field text).'),
        default=True,
    )

    attributes = fields.AttributesField()

    def get_short_description(self):
        key = self.key
        val = self.value
        max_len = 4

        should_truncate_key = len(key) > max_len
        key_desc = key[0:max_len] + '…' if should_truncate_key else key

        should_truncate_val = len(key) > max_len
        val_desc = val[0:max_len] + '…' if should_truncate_val else val

        return key_desc + ': ' + val_desc
