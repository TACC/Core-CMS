from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_text
from django.db import models

from djangocms_link.models import AbstractLink

from taccsite_cms.contrib.helpers import (
    get_choices,
    filter_choices_by_prefix,
    clean_for_abstract_link,
)

from .constants import LAYOUT_DICT, STYLE_DICT



# Constants

ANY_CHOICES_NAME = _('Any Layouts')
ROWS_CHOICES_NAME = _('Row Layouts')
COLS_CHOICES_NAME = _('Column Layouts')

LAYOUT_CHOICES = (
    ( ROWS_CHOICES_NAME, filter_choices_by_prefix(
        get_choices(LAYOUT_DICT), 'row'
    ) ),
    ( COLS_CHOICES_NAME, filter_choices_by_prefix(
        get_choices(LAYOUT_DICT), 'cols'
    ) ),
)
STYLE_CHOICES = (
    ( ROWS_CHOICES_NAME, filter_choices_by_prefix(
        get_choices(STYLE_DICT), 'rows'
    ) ),
    ( COLS_CHOICES_NAME, filter_choices_by_prefix(
        get_choices(STYLE_DICT), 'cols'
    ) ),
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
        help_text=_('Layout of the articles within. Notice: All %(col_layouts)s become multiple rows when screen width is narrow.') % { 'col_layouts': COLS_CHOICES_NAME },
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

    def get_short_description(self):
        return self.title_text



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

        # If user mix-and-matched layout and styles, then explain their mistake
        layout_name = force_text(
            self._meta.get_field('layout_type').verbose_name )
        style_name = force_text(
            self._meta.get_field('style_type').verbose_name )
        if 'cols' in self.layout_type and 'rows' in self.style_type:
            raise ValidationError(
                _('If you choose a %(layout)s from %(row_layouts)s, then choose a %(style)s from %(row_layouts)s (or no %(style)s).') % {
                    'style': style_name, 'layout': layout_name,
                    'row_layouts': ROWS_CHOICES_NAME
                },
                code='invalid'
            )
        if 'rows' in self.layout_type and 'cols' in self.style_type:
            raise ValidationError(
                _('If you choose a %(layout)s from %(col_layouts)s, then choose a %(style)s from %(col_layouts)s (or no %(style)s).') % {
                    'style': style_name, 'layout': layout_name,
                    'col_layouts': COLS_CHOICES_NAME
                },
                code='invalid'
            )
