from django import forms
from django.utils.translation import gettext_lazy as _

from djangocms_bootstrap4.contrib.bootstrap4_alerts.models import Bootstrap4Alerts

from .presentation import (
    ALERT_PRESENTATION_ADMONITION,
    ALERT_PRESENTATION_ATTR,
    ALERT_PRESENTATION_BOOTSTRAP,
    get_alert_presentation,
)


class Bootstrap4AlertForm(forms.ModelForm):
    alert_presentation = forms.ChoiceField(
        label=_('Presentation'),
        choices=(
            (ALERT_PRESENTATION_BOOTSTRAP, _('Bootstrap alert')),
            (ALERT_PRESENTATION_ADMONITION, _('Admonition (Core Styles)')),
        ),
        initial=ALERT_PRESENTATION_BOOTSTRAP,
        help_text=_(
            'Bootstrap alert uses standard alert styling; '
            'Admonition uses Core-Styles admonition blocks and icons.'
        ),
    )

    class Meta:
        model = Bootstrap4Alerts
        fields = (
            'alert_context',
            'alert_dismissable',
            'tag_type',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['alert_presentation'].initial = get_alert_presentation(
            self.instance,
        )

    def save(self, commit=True):
        instance = super().save(commit=False)
        attrs = dict(instance.attributes or {})
        attrs[ALERT_PRESENTATION_ATTR] = self.cleaned_data['alert_presentation']
        instance.attributes = attrs
        if commit:
            instance.save()
        return instance
