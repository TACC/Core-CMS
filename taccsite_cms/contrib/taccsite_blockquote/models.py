# SEE: https://github.com/django-cms/djangocms-bootstrap4/blob/2.0.0/djangocms_bootstrap4/contrib/bootstrap4_content/models.py

from cms.models.pluginmodel import CMSPlugin

from django.db import models

from djangocms_attributes_field import fields

from taccsite_cms.contrib.constants import ALIGN_CHOICES

from .defaults import user_name as default_name

class TaccsiteBlockquote(CMSPlugin):
    """
    Components > "Blockquote" Model
    https://confluence.tacc.utexas.edu/x/FIEjCQ
    """
    quote_text = models.TextField(
        default=None,
    )
    quote_origin = models.CharField(
        help_text='The origin of the quote (i.e. citation, attribution) (e.g. author, source).',
        blank=True,
        max_length=50,
    )
    quote_alignment = models.CharField(
        choices=ALIGN_CHOICES,
        default=ALIGN_CHOICES[0][0],
        blank=True,
        max_length=255,
    )
    attributes = fields.AttributesField()

    def get_short_description(self):
        return self.quote_text
