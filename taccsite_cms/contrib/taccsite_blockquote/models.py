from cms.models.pluginmodel import CMSPlugin

from django.db import models

class TaccsiteBlockquote(CMSPlugin):
    """
    Components > "Blockquote" Plugin
    https://confluence.tacc.utexas.edu/x/FIEjCQ
    """
    guest_name = models.CharField(max_length=50, default='Guest')

    def get_short_description(self):
        return 'Hello, […]'
