from cms.extensions import PageExtension, extension_pool
from django.db import models
from django.utils.translation import gettext_lazy as _


class DummyModel(models.Model):
    """
    Exists solely to trigger Django to send post_migrate signal (see apps.py)
    """
    class Meta:
        app_label = 'taccsite_cms'


TARGET_CHOICES = (
    ('_blank', _('Open in new window')),
    ('_self',  _('Open in same window')),
)


class PageMenuTarget(PageExtension):
    """
    Per-page menu link target, editable in the CMS toolbar or Django admin.
    An empty value defers to the default target_blank tag logic (external URLs
    open in a new tab, internal URLs do not).
    """
    target = models.CharField(
        verbose_name=_('Target'),
        choices=TARGET_CHOICES,
        blank=True,
        default='',
        max_length=255,
    )

    def __str__(self):
        return self.extended_object.get_title()

    class Meta:
        app_label = 'taccsite_cms'
        verbose_name = 'menu link target'


extension_pool.register(PageMenuTarget)
