from django.contrib import admin
from cms.extensions.admin import PageExtensionAdmin

from .models import PageMenuTarget


@admin.register(PageMenuTarget)
class PageMenuTargetAdmin(PageExtensionAdmin):
    # PageExtensionAdmin hides this model from the Django admin index intentionally,
    # so it is not discoverable by browsing. Access it directly:
    # - View: /admin/taccsite_cms/pagemenutarget/
    # - Edit: /admin/taccsite_cms/pagemenutarget/<extension_pk>/change/
    # - Add:  /admin/taccsite_cms/pagemenutarget/add/?extended_object=<page_pk>
    # The CMS toolbar item (cms_toolbars.py) generates these URLs automatically.
    pass
