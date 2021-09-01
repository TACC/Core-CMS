from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from django.db import models

from djangocms_attributes_field import fields

from taccsite_cms.contrib.taccsite_offset.models import DIRECTION_CHOICES

class TaccsiteBlockquote(CMSPlugin):
    """
    Components > "Blockquote" Model
    https://confluence.tacc.utexas.edu/x/FIEjCQ
    """
    text = models.TextField(
        verbose_name=_('Quote'),
        null=True,
        default='',
    )

    origin = models.CharField(
        help_text=_('The origin of the quote (i.e. citation, attribution) (e.g. author, source). This value is ignored if "Advanced origin" fields have data.'),
        blank=True,
        max_length=100,
    )

    use_cite = models.BooleanField(
        verbose_name=_('Use the "Citation" fields'),
        default=False,
    )
    cite_person = models.CharField(
        verbose_name=_('Author / Speaker'),
        help_text='The author or speaker of the quote.',
        blank=True,
        max_length=50,
    )
    cite_text = models.CharField(
        verbose_name=_('Source Text'),
        help_text=_('Text for the source of the quote.'),
        blank=True,
        max_length=50,
    )
    cite_url = models.CharField(
        verbose_name=_('Source URL'),
        help_text=_('URL for the source of the quote.'),
        blank=True,
        max_length=255,
    )

    offset = models.CharField(
        choices=DIRECTION_CHOICES,
        blank=True,
        max_length=255,
    )

    attributes = fields.AttributesField()

    def get_short_description(self):
        return self.text
