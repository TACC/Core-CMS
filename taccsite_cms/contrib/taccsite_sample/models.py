from cms.models.pluginmodel import CMSPlugin

from django.db import models

from .defaults import name as default_name

class TaccsiteSample(CMSPlugin):
    """
    Components > "Sample (Greet User)" Model
    https://url.to/docs/components/sample/
    """
    guest_name = models.CharField(
        max_length=50,
        default=default_name,
        help_text=f'If user is logged in they are greeted by their name. If not logged in, they are greeted as this value. If this value is blank, they are greeted as "{default_name}".',
        # To change the widget, a new Form class is required
        # FAQ: Wesley B searched for hours to find this important information
        # SEE: http://disq.us/p/210zgp2
        # SEE: [`TaccsiteSamplePlugin.form`](./cms_plugins.py)
        # widget=forms.TextInput(attrs={'placeholder': 'Search'}),
        blank=True
    )

    def get_short_description(self):
        return 'Hello, […]'
