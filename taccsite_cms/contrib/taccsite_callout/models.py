from cms.models.pluginmodel import CMSPlugin

from django.db import models
from django.utils.translation import gettext_lazy as _

from djangocms_attributes_field import fields

class TaccsiteCallout(CMSPlugin):
    """
    Components > "Callout" Model
    """
    title = models.CharField(
        verbose_name=_('Title'),
        help_text=_('A heading for the callout.'),
        blank=True,
        max_length=100,
    )
    description = models.CharField(
        verbose_name=_('Description'),
        help_text=_('A paragraph for the callout.'),
        blank=True,
        max_length=200,
    )

    attributes = fields.AttributesField()

    def get_short_description(self):
        return self.title
