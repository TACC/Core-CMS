from cms.extensions import PageExtension, extension_pool
from django.db import models
from django.utils.translation import gettext_lazy as _


class DummyModel(models.Model):
    """
    Exists solely to trigger Django to send post_migrate signal (see apps.py)
    """
    class Meta:
        app_label = 'taccsite_cms'


NAV_TARGET_CHOICES = (
    ('',       _('Default')),
    ('_blank', _('Open in new window')),
    ('_self',  _('Open in same window')),
)


class PageNavOptions(PageExtension):
    """
    Per-page nav options, editable via the CMS toolbar (Page > Page Options >
    Nav Options) or Django admin.
    """
    target = models.CharField(
        verbose_name=_('Target'),
        choices=NAV_TARGET_CHOICES,
        blank=True,
        default='',
        max_length=255,
        help_text=_('Override the default link target for this page\'s nav menu entry. '
                    'Leave empty to use automatic detection (external URLs open in a new tab).'),
    )

    def __str__(self):
        return self.extended_object.get_title()

    class Meta:
        app_label = 'taccsite_cms'
        verbose_name = 'page nav options'


extension_pool.register(PageNavOptions)
