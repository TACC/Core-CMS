from django.core.exceptions import ValidationError

from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_text

from django.db import models
from djangocms_link.models import AbstractLink

from djangocms_attributes_field import fields

from taccsite_cms.contrib.helpers import (
    get_indices_that_start_with
)

# Constants

ANY_CHOICES_NAME = _('Any Layouts')
ROWS_CHOICES_NAME = _('Row Layouts')
COLS_CHOICES_NAME = _('Column Layouts')

LAYOUT_CHOICES = (
    (ROWS_CHOICES_NAME, (
        ('always-rows-N--even',  _('N Equal-Height Rows (always)')),
    )),
    (COLS_CHOICES_NAME, (
        ('widest-cols-2--even', _('2 Equal-Width Columns (when list is at its widest)')),
        ('widest-cols-2--wide-narr', _('2 Columns: 1 Wide, 1 Narrow (when list is at its widest)')),
        ('widest-cols-2--narr-wide', _('2 Columns: 1 Narrow, 1 Wide (when list is at its widest)')),
        ('widest-cols-3--even', _('3 Equal-Width Columns (when list is at its widest)')),
    )),
)
STYLE_CHOICES = (
    (ROWS_CHOICES_NAME, (
        ('rows-divided', _('Dividers Between Articles')),
    )),
    (ANY_CHOICES_NAME, (
        ('all-gapless', _('Remove Gaps Between Articles')),
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
        help_text='The title at the top of the list.',
        blank=True,
        max_length=100,
    )

    layout_type = models.CharField(
        verbose_name=_('Layout Option'),
        help_text='Layout of the articles within.',
        choices=LAYOUT_CHOICES,
        default=LAYOUT_CHOICES[0][0],
        blank=False,
        max_length=255,
    )
    style_type = models.CharField(
        verbose_name=_('Style Option'),
        help_text='Optional styles for the list itself.',
        choices=STYLE_CHOICES,
        blank=True,
        max_length=255,
    )

    attributes = fields.AttributesField()

    def get_short_description(self):
        return self.title_text

    def clean(self):
        # Bypass irrelevant parent validation
        # SEE: ./_docs/how-to-override-validation-error-from-parent-model.md
        try:
            super().clean()
        except ValidationError as err:
            # Intercept single-field errors
            if hasattr(err, 'error_list'):
                for i in range(len(err.error_list)):
                    error = err.error_list[i]
                    # Do not require a link
                    if 'Please provide a link.' in error:
                        # Unless user provided link text
                        if self.name and not self.get_link():
                            err.error_list[i] = ValidationError(
                                _('Please provide a footer link or delete its display name.'), code='invalid')
                        else:
                            del err.error_list[i]

            # Intercept multi-field errors
            if hasattr(err, 'error_dict'):
                for field, errors in err.message_dict.items():
                    # Reduce verbosity of original error message
                    # FAQ: Original error message assumes more fields exist
                    indices = get_indices_that_start_with(
                        'Only one of ', errors
                    )
                    for i in indices:
                        err.error_dict[field] = ValidationError(
                            _('Only one of External link or Internal link may be given.'), code='invalid')

            if len(err.messages) == 0:
                pass
            else:
                raise err

        if (
            ('rows' in self.layout_type and 'cols' in self.style_type) or
            ('cols' in self.layout_type and 'rows' in self.style_type)
        ):
            layout_name = force_text(
                self._meta.get_field('layout_type').verbose_name)
            style_name = force_text(
                self._meta.get_field('style_type').verbose_name)
            raise ValidationError(
                _(f'Choose {layout_name} and {style_name} that are both for {ROWS_CHOICES_NAME} or both for {COLS_CHOICES_NAME}.'),
                code='invalid'
            )

    class Meta:
        abstract = False
