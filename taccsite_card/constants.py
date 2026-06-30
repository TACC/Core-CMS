"""Card plugin: skin (class_name) and layout (template) axes for Core-Styles c-card."""

from django.utils.translation import gettext_lazy as _

from taccsite_cms.contrib.helpers import concat_classnames

# Skin axis — stored in Style.class_name (c-card block + modifiers)
CARD_SKIN_CLASS_NAME_CHOICES = (
    ('c-card', _('Base (block only)')),
    ('c-card--plain', _('Plain')),
    ('c-card--standard', _('Standard')),
)

CARD_SKIN_DEFAULT = 'c-card--plain'

# Layout axis — stored in Style.template; each value selects a layout template (Way 1)
CARD_LAYOUT_TEMPLATES = (
    ('default', _('Default (no image layout)')),
    ('image_top', _('Image Top')),
    ('image_bottom', _('Image Bottom')),
    ('image_left', _('Image Left')),
    ('image_right', _('Image Right')),
)


def class_name_to_skin_modifier(class_name):
    """
    Map Style.class_name to a skin modifier (not including block c-card in base.html).

    c-card → (none)
    c-card--plain → c-card--plain
    """
    if not class_name or class_name == 'c-card':
        return ''
    if class_name.startswith('c-card--'):
        return class_name
    return ''


def normalize_card_class_tokens(class_string):
    """Drop redundant c-card block tokens from additional_classes / attributes.class."""
    if not class_string:
        return ''
    parts = []
    for raw in class_string.replace(',', ' ').split():
        token = raw.strip()
        if not token or token == 'c-card':
            continue
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
