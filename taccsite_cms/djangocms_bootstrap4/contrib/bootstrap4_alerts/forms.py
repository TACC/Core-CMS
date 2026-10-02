from django import forms
from django.utils.translation import gettext_lazy as _

from djangocms_bootstrap4.contrib.bootstrap4_alerts.models import Bootstrap4Alerts

from .appearance import (
    ALERT_APPEARANCE_ADMONITION,
    ALERT_APPEARANCE_ATTR,
    ALERT_APPEARANCE_ATTR_LEGACY,
    ALERT_APPEARANCE_BOOTSTRAP,
    get_alert_appearance,
)


class Bootstrap4AlertForm(forms.ModelForm):
    alert_appearance = forms.ChoiceField(
        label=_('Appearance'),
        choices=(
            (ALERT_APPEARANCE_BOOTSTRAP, _('Bootstrap (TACC)')),
            (ALERT_APPEARANCE_ADMONITION, _('Admonition (TACC)')),
        ),
        initial=ALERT_APPEARANCE_BOOTSTRAP,
        help_text=_(
            'Bootstrap (TACC) uses standard alert styling. '
            'Admonition (TACC) uses Core-Styles admonition blocks and icons. '
            'Admonition does not support dismissible.'
        ),
    )

    class Meta:
        model = Bootstrap4Alerts
        fields = (
            'alert_context',
            'alert_dismissable',
            'tag_type',
        )

    class Media:
        js = ('site_cms/js/admin/bootstrap4-alert-appearance.js',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['alert_appearance'].initial = get_alert_appearance(
            self.instance,
        )
        if get_alert_appearance(self.instance) == ALERT_APPEARANCE_ADMONITION:
            self.fields['alert_dismissable'].disabled = True

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('alert_appearance') == ALERT_APPEARANCE_ADMONITION:
            cleaned_data['alert_dismissable'] = False
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        attrs = dict(instance.attributes or {})
        attrs[ALERT_APPEARANCE_ATTR] = self.cleaned_data['alert_appearance']
        attrs.pop(ALERT_APPEARANCE_ATTR_LEGACY, None)
        instance.attributes = attrs
        if self.cleaned_data['alert_appearance'] == ALERT_APPEARANCE_ADMONITION:
            instance.alert_dismissable = False
        if commit:
            instance.save()
        return instance
