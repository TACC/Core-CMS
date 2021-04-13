from cms.models.pluginmodel import CMSPlugin

from django.db import models

class TaccsiteSample(CMSPlugin):
    """
    Components > "Sample (Greet User)" Model
    https://url.to/docs/components/sample/
    """
    guest_name = models.CharField(max_length=50, default='Guest', blank=True)

    def get_short_description(self):
        return 'Hello, […]'
