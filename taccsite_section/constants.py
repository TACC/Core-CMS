from django.conf import settings
from django.utils.translation import gettext_lazy as _

from djangocms_bootstrap4.contrib.bootstrap4_grid.constants import (
    GRID_CONTAINER_CHOICES,
)

STYLE_TAGS = getattr(
    settings,
    'DJANGOCMS_STYLE_TAGS',
    ('div', 'article', 'section'),
)
# djangocms_style uses the first DJANGOCMS_STYLE_TAGS entry as Style.tag_type default.
SECTION_STYLE_INHERITED_TAG = STYLE_TAGS[0]

SECTION_ONLY_GROUP_LABEL = _('Section only')


def _choices_for_group(choices, group_label):
    for value, label in choices:
        if isinstance(label, (tuple, list)) and value == group_label:
            return label
    return ()


SECTION_TYPE_CHOICES = _choices_for_group(
    GRID_CONTAINER_CHOICES,
    SECTION_ONLY_GROUP_LABEL,
)
SECTION_TYPE_DEFAULT = 'o-section o-section--style-muted'

SECTION_TAG_TYPE_DEFAULT = 'section'

SECTION_TAG_TYPE_CHOICES = (
    ('section', _('section')),
    ('article', _('article')),
    ('aside', _('aside')),
    ('div', _('div')),
)
