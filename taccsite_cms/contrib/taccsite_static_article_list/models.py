from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_text
from django.db import models

from djangocms_link.models import AbstractLink

from taccsite_cms.contrib.helpers import clean_for_abstract_link

# Constants

ANY_CHOICES_NAME = _('Any Layouts')
ROWS_CHOICES_NAME = _('Row Layouts')
COLS_CHOICES_NAME = _('Column Layouts')

LAYOUT_CHOICES = (
    (ROWS_CHOICES_NAME, (
        ('rows-always-N-even',  _('Multiple Rows')),
    )),
    (COLS_CHOICES_NAME, (
        ('cols-widest-2-even', _('2 Equal-Width Columns')),
        ('cols-widest-2-wide-narr', _('2 Columns: 1 Wide, 1 Narrow')),
        ('cols-widest-2-narr-wide', _('2 Columns: 1 Narrow, 1 Wide')),
        ('cols-widest-3-even', _('3 Equal-Width Columns')),
    )),
)
STYLE_CHOICES = (
    (ROWS_CHOICES_NAME, (
        ('rows-divided', _('Dividers Between Articles')),
        ('rows-gapless', _('Remove Gaps Between Articles')),
    )),
    (COLS_CHOICES_NAME, (
        ('cols-gapless', _('Remove Gaps Between Articles')),
    )),
)

# Models

class TaccsiteArticleList(AbstractLink):
    """
    Components > "Article List" Model
    https://confluence.tacc.utexas.edu/x/OIAjCQ
    """
    title_text = models.CharField(
        verbose_name=_('Title Text'),
        help_text=_('The title at the top of the list.'),
        blank=True,
        max_length=100,
    )

    layout_type = models.CharField(
        verbose_name=_('Layout Option'),
        help_text=_(f'Layout of the articles within. Notice: All {COLS_CHOICES_NAME} become multiple rows when screen width is narrow.'),
        choices=LAYOUT_CHOICES,
        default=LAYOUT_CHOICES[0][0],
        blank=False,
        max_length=255,
    )
    style_type = models.CharField(
        verbose_name=_('Style Option'),
        help_text=_('Optional styles for the list itself.'),
        choices=STYLE_CHOICES,
        blank=True,
        max_length=255,
    )

    link_is_optional = True

    def get_short_description(self):
        return self.title_text

    def clean(self):
        # If user provided link text, then require link
        if self.name and not self.get_link():
            err.error_list[i] = ValidationError(
                _('Please provide a footer link or delete its display name.'), code='invalid')

        # If user mix-and-matched layout and styles, then explain their mistake
        layout_name = force_text(
            self._meta.get_field('layout_type').verbose_name)
        style_name = force_text(
            self._meta.get_field('style_type').verbose_name)
        if 'cols' in self.layout_type and 'rows' in self.style_type:
            raise ValidationError(
                _(f'If you choose a {layout_name} for {ROWS_CHOICES_NAME}, then choose a {style_name} for {ROWS_CHOICES_NAME} (or no {style_name}).'),
                code='invalid'
            )
        if 'rows' in self.layout_type and 'cols' in self.style_type:
            raise ValidationError(
                _(f'If you choose a {layout_name} for {COLS_CHOICES_NAME}, then choose a {style_name} for {COLS_CHOICES_NAME} (or no {style_name}).'),
                code='invalid'
            )

        clean_for_abstract_link(__class__, self)

    class Meta:
        abstract = False
