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
        blank=True
    )

    def get_short_description(self):
        return 'Hello, […]'
