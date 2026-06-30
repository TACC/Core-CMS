from django import forms
from django.utils.translation import gettext_lazy as _

from djangocms_style.models import Style

from .constants import CARD_LAYOUT_TEMPLATES, get_card_skin_class_name_choices


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
        self.fields['class_name'].choices = get_card_skin_class_name_choices()
        self.fields['class_name'].label = _('Card style')
        self.fields['class_name'].help_text = _(
            'Skin modifier for the card. Published markup always includes the block class c-card.'
        )
        self.fields['template'].choices = CARD_LAYOUT_TEMPLATES
        self.fields['template'].label = _('Card layout')
        self.fields['template'].help_text = _(
            'Image placement layout modifier (c-card--image-*). Composes with card style.'
        )
