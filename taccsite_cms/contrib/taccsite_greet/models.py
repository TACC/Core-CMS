from cms.models.pluginmodel import CMSPlugin

from django.db import models

class TaccsiteGreet(CMSPlugin):
    """
    Components > "Greet" Plugin (Sample)
    https://url.to/docs/components/sample/
    """
    guest_name = models.CharField(max_length=50, default='Guest', blank=True)

    def get_short_description(self):
        return 'Hello, […]'
