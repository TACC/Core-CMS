from cms.models.pluginmodel import CMSPlugin

from django.db import models

from .constants import DEFAULT_USER_NAME as default_name
from .helpers import has_proper_name, get_proper_name

class TaccsiteSample(CMSPlugin):
    """
    Components > "Sample (Greet User)" Model
    https://url.to/docs/components/sample/
    """
    guest_name = models.CharField(
        max_length=50,
        default=default_name,
        help_text=('If user is logged in they are greeted by their name. If not logged in, they are greeted as this value. If this value is blank, they are greeted as "%(default_name)s".') % {'default_name': default_name},
        # To change the widget, a new Form class is required
        # FAQ: Wesley B searched for hours to find this important information
        # SEE: http://disq.us/p/210zgp2
        # SEE: [`TaccsiteSamplePlugin.form`](./cms_plugins.py)
        # widget=forms.TextInput(attrs={'placeholder': 'Search'}),
        blank=True
    )

    def get_short_description(self):
        return 'Hello, […]'



    # Helpers

    def get_name(self, user=None):
        """Get name by which to greet the user.

        :param django.contrib.auth.models.User: Django user object

        :returns: Name of authenticated user or the name for any guest
        :rtype: str
        """
        if has_proper_name(user):
            name = get_proper_name(user)
        elif user.is_authenticated:
            name = user.username
        elif bool(self.guest_name):
            name = self.guest_name
        else:
            name = default_name

        return name
