from django.contrib import admin
from cms.extensions.admin import PageExtensionAdmin

from .models import PageNavOptions


@admin.register(PageNavOptions)
class PageNavOptionsAdmin(PageExtensionAdmin):
    # PageExtensionAdmin hides this model from the Django admin index intentionally,
    # so it is not discoverable by browsing. Access it directly:
    # - Add:    /admin/taccsite_cms/pagenavoptions/add/?extended_object=<page_pk>
    # - Change: /admin/taccsite_cms/pagenavoptions/<extension_pk>/change/
    # The CMS toolbar item (cms_toolbars.py) generates these URLs automatically.
    pass
