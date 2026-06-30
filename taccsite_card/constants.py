"""Card plugin: skin (class_name) and layout (template) axes for Core-Styles c-card."""

from django.utils.translation import gettext_lazy as _

CARD_SKIN_CLASS_NAME_CHOICES = (
    ('c-card', _('Base (no background)')),
    ('c-card--plain', _('Plain')),
    ('c-card--standard', _('Standard')),
)
CARD_SKIN_CLASS_NAME_DEFAULT = 'c-card--plain'

CARD_LAYOUT_TEMPLATES = (
    ('default', _('Default (no image layout)')),
    ('image_top', _('Image Top')),
    ('image_bottom', _('Image Bottom')),
    ('image_left', _('Image Left')),
    ('image_right', _('Image Right')),
)
