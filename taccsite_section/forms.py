from django import forms
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from djangocms_style.models import Style

from .constants import (
    SECTION_STYLE_INHERITED_TAG,
    SECTION_TAG_TYPE_CHOICES,
    SECTION_TAG_TYPE_DEFAULT,
    SECTION_TYPE_CHOICES,
    SECTION_TYPE_DEFAULT,
)

MDN_SECTION_URL = 'https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section'
MDN_ARTICLE_URL = 'https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article'
MDN_ASIDE_URL = 'https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside'
MDN_DIV_URL = 'https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div'

TAG_TYPE_HELP_TEXT = format_html(
    'Use <a href="{}" target="_blank">section</a> for thematic grouping, '
    '<a href="{}" target="_blank">article</a> for self-contained content, '
    '<a href="{}" target="_blank">aside</a> for tangential content, or '
    '<a href="{}" target="_blank">div</a> if previous options are inaccurate.',
    MDN_SECTION_URL,
    MDN_ARTICLE_URL,
    MDN_ASIDE_URL,
    MDN_DIV_URL,
)


class TaccsiteSectionPluginForm(forms.ModelForm):
    class Meta:
        model = Style
        fields = (
            'label',
            'class_name',
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
        valid_section_types = {value for value, _label in SECTION_TYPE_CHOICES}
        valid_tag_types = {value for value, _label in SECTION_TAG_TYPE_CHOICES}

        should_default_tag_type = (
            is_new_plugin
            and (
                self.instance.tag_type not in valid_tag_types
                or self.instance.tag_type == SECTION_STYLE_INHERITED_TAG
            )
        )
        if should_default_tag_type:
            self.instance.tag_type = SECTION_TAG_TYPE_DEFAULT

        should_default_section_type = (
            is_new_plugin
            and self.instance.class_name not in valid_section_types
        )
        if should_default_section_type:
            self.instance.class_name = SECTION_TYPE_DEFAULT

        self.fields['label'].label = _('Name')
        self.fields['class_name'].choices = SECTION_TYPE_CHOICES
        self.fields['class_name'].label = _('Section type')
        self.fields['class_name'].initial = SECTION_TYPE_DEFAULT
        self.fields['tag_type'].choices = SECTION_TAG_TYPE_CHOICES
        self.fields['tag_type'].initial = SECTION_TAG_TYPE_DEFAULT
        self.fields['tag_type'].help_text = TAG_TYPE_HELP_TEXT
