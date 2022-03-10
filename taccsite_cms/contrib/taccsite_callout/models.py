from cms.models.pluginmodel import CMSPlugin

from django.db import models
from django.utils.translation import gettext_lazy as _

from djangocms_link.models import AbstractLink
from djangocms_attributes_field import fields

from taccsite_cms.contrib.helpers import clean_for_abstract_link

class TaccsiteCallout(AbstractLink):
    """
    Components > "Callout" Model
    """
    title = models.CharField(
        verbose_name=_('Title'),
        help_text=_('A heading for the callout.'),
        blank=False,
        max_length=100,
    )
    description = models.CharField(
        verbose_name=_('Description'),
        help_text=_('A paragraph for the callout.'),
        blank=False,
        max_length=200,
    )

    attributes = fields.AttributesField()

    def get_short_description(self):
        return self.title



    # Parent

    link_is_optional = False

    class Meta:
        abstract = False

    # Validate
    def clean(self):
        clean_for_abstract_link(__class__, self)
