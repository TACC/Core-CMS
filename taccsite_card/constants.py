from django.conf import settings
from django.utils.translation import gettext_lazy as _

STYLE_TAGS = getattr(
    settings,
    'DJANGOCMS_STYLE_TAGS',
    ('div', 'article', 'section'),
)
# djangocms_style uses the first DJANGOCMS_STYLE_TAGS entry as Style.tag_type default.
CARD_STYLE_INHERITED_TAG = STYLE_TAGS[0]

CARD_SKIN_CLASS_NAME_CHOICES = (
    ('c-card', _('No background')),
    ('c-card--plain', _('Plain')),
    ('c-card--standard', _('Standard')),
)
CARD_SKIN_CLASS_NAME_DEFAULT = 'c-card--plain'

CARD_LAYOUT_TEMPLATES = (
    ('default', _('No image')),
    ('image_top', _('Image Top')),
    ('image_bottom', _('Image Bottom')),
    ('image_left', _('Image Left')),
    ('image_right', _('Image Right')),
)

CARD_TAG_TYPE_CHOICES = (
    ('article', _('article')),
    ('aside', _('aside')),
    ('div', _('div')),
)
CARD_TAG_TYPE_DEFAULT = 'article'
