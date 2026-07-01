from django import forms
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from djangocms_style.models import Style

from .constants import (
    CARD_LAYOUT_TEMPLATES,
    CARD_SKIN_CLASS_NAME_CHOICES,
    CARD_SKIN_CLASS_NAME_DEFAULT,
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
    'Use <a href="{}">article</a> for self-contained content, '
    '<a href="{}">aside</a> for tangential content, or '
    '<a href="{}">div</a> if previous options are inaccurate.',
    MDN_ARTICLE_URL,
    MDN_ASIDE_URL,
    MDN_DIV_URL,
)


def _code(class_name):
    return format_html('<code>{}</code>', class_name)


CARD_STYLE_HELP_TEXT = _('How a card looks.')

CARD_LAYOUT_HELP_TEXT = _('What content a card supports.')

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

        is_new_plugin = not self.instance.pk

        should_default_tag_type_to_article = (
            is_new_plugin
            and self.instance.tag_type == 'div' # has Style default tag
        )
        if should_default_tag_type_to_article:
            self.instance.tag_type = 'article'

        valid_card_skins = {value for value, _label in CARD_SKIN_CLASS_NAME_CHOICES}

        should_default_card_style_to_plain = (
            is_new_plugin
            and self.instance.class_name not in valid_card_skins
        )
        if should_default_card_style_to_plain:
            self.instance.class_name = CARD_SKIN_CLASS_NAME_DEFAULT

        self.fields['class_name'].choices = CARD_SKIN_CLASS_NAME_CHOICES
        self.fields['class_name'].label = _('Card style')
        self.fields['class_name'].initial = CARD_SKIN_CLASS_NAME_DEFAULT
        self.fields['class_name'].help_text = CARD_STYLE_HELP_TEXT
        self.fields['template'].choices = CARD_LAYOUT_TEMPLATES
        self.fields['template'].label = _('Card layout')
        self.fields['template'].help_text = CARD_LAYOUT_HELP_TEXT
        self.fields['tag_type'].choices = CARD_TAG_TYPE_CHOICES
        self.fields['tag_type'].initial = 'article'
        self.fields['tag_type'].help_text = TAG_TYPE_HELP_TEXT
