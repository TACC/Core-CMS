from cms.models.pluginmodel import CMSPlugin

from django.db import models

from .defaults import user_name as default_name

class TaccsiteBlockquote(CMSPlugin):
    """
    Components > "Blockquote" Model
    https://confluence.tacc.utexas.edu/x/FIEjCQ
    """
    guest_name = models.CharField(
        max_length=50,
        default=default_name,
        help_text=f'If user is logged in they are greeted by their name. If not logged in, they are greeted as this value. If this value is blank, they are greeted as "{default_name}".',
        blank=True
    )

    def get_short_description(self):
        return 'Hello, […]'
