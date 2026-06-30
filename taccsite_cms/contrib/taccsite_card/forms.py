from django import forms
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from djangocms_style.models import Style

from .constants import (
    CARD_LAYOUT_TEMPLATES,
    CARD_SKIN_DEFAULT,
    get_card_skin_class_name_choices,
)

CARD_TAG_TYPE_CHOICES = (
    ('article', _('article')),
    ('aside', _('aside')),
    ('div', _('div')),
)

MDN_ARTICLE_URL = 'https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article'
MDN_ASIDE_URL = 'https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside'
MDN_DIV_URL = 'https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div'

TAG_TYPE_HELP_TEXT = format_html(
    'Use <a href="{}">article</a> for self-contained composition, '
    '<a href="{}">aside</a> for tangentially related content, or '
    '<a href="{}">div</a> if previous options are inaccurate.',
    MDN_ARTICLE_URL,
    MDN_ASIDE_URL,
    MDN_DIV_URL,
)


def _code(class_name):
    return format_html('<code>{}</code>', class_name)


CARD_STYLE_HELP_TEXT = format_html(
    'Skin modifier for the card. Published markup always includes the block class {}.',
    _code('c-card'),
)

CARD_LAYOUT_HELP_TEXT = format_html(
    'Image placement layout modifier ({}). Composes with card style.',
    _code('c-card--image-*'),
)

class TaccsiteCardPluginForm(forms.ModelForm):
    class Meta:
        model = Style
        fields = (
            'label',
            'class_name',
            'template',
            'tag_type',
            'additional_classes',
            'id_name',
            'attributes',
            'padding_top',
            'padding_right',
            'padding_bottom',
            'padding_left',
            'margin_top',
            'margin_right',
            'margin_bottom',
            'margin_left',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        should_default_tag_type_to_article = (
            not self.instance.pk # is new plugin
            and self.instance.tag_type == 'div' # has Style default tag
        )
        if should_default_tag_type_to_article:
            self.instance.tag_type = 'article'
        should_default_card_style_to_plain = (
            not self.instance.pk
            and self.instance.class_name in ('', 'card')
        )
        if should_default_card_style_to_plain:
            self.instance.class_name = CARD_SKIN_DEFAULT
        self.fields['class_name'].choices = get_card_skin_class_name_choices()
        self.fields['class_name'].label = _('Card style')
        self.fields['class_name'].initial = CARD_SKIN_DEFAULT
        self.fields['class_name'].help_text = CARD_STYLE_HELP_TEXT
        self.fields['template'].choices = CARD_LAYOUT_TEMPLATES
        self.fields['template'].label = _('Card layout')
        self.fields['template'].help_text = CARD_LAYOUT_HELP_TEXT
        self.fields['tag_type'].choices = CARD_TAG_TYPE_CHOICES
        self.fields['tag_type'].initial = 'article'
        self.fields['tag_type'].help_text = TAG_TYPE_HELP_TEXT
