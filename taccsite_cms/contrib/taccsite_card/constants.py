"""Card plugin: skin (class_name) and layout (template) axes for Core-Styles c-card."""

from django.conf import settings
from django.utils.translation import gettext_lazy as _

from taccsite_cms.contrib.helpers import concat_classnames

# Skin axis — stored in Style.class_name (legacy card--* tokens, mapped to c-card--* on output)
CARD_SKIN_CLASS_NAMES = (
    'card',
    'card--plain',
    'card--standard',
)

# Layout axis — stored in Style.template; each value selects a layout template (Way 1)
CARD_LAYOUT_TEMPLATES = (
    ('default', _('Default (no image layout)')),
    ('image_top', _('Image top')),
    ('image_bottom', _('Image bottom')),
    ('image_left', _('Image left')),
    ('image_right', _('Image right')),
)


def get_card_skin_class_name_choices():
    """Subset of DJANGOCMS_STYLE_CHOICES for the Card plugin skin field."""
    all_choices = getattr(
        settings,
        'DJANGOCMS_STYLE_CHOICES',
        list(CARD_SKIN_CLASS_NAMES),
    )
    return [
        (entry, entry)
        for entry in all_choices
        if entry in CARD_SKIN_CLASS_NAMES
    ]


def class_name_to_skin_modifier(class_name):
    """
    Map Style.class_name skin token to a c-card--* modifier (not including block c-card).

    card → (none)
    card--plain → c-card--plain
    """
    if not class_name or class_name == 'card':
        return ''
    if class_name.startswith('card--'):
        return 'c-card' + class_name[4:]
    return ''


def normalize_card_class_tokens(class_string):
    """
    Map legacy card--* and c-card--* tokens in additional_classes / attributes.class.

    Leaves unrelated tokens unchanged.
    """
    if not class_string:
        return ''
    parts = []
    for raw in class_string.replace(',', ' ').split():
        token = raw.strip()
        if not token:
            continue
        if token == 'card':
            continue
        if token.startswith('card--'):
            parts.append('c-card' + token[4:])
        else:
            parts.append(token)
    return concat_classnames(parts)


def attributes_str_without_class(instance):
    """Render attributes except class (class is composed on the wrapper element)."""
    attributes = dict(instance.attributes or {})
    attributes.pop('class', None)
    if not attributes:
        return ''
    return ' '.join(
        f'{key}="{value}"'
        for key, value in attributes.items()
    )
