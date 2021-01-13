from cms.models.pluginmodel import CMSPlugin

from django.db import models

class TaccsiteGreet(CMSPlugin):
    guest_name = models.CharField(max_length=50, default='Guest')
