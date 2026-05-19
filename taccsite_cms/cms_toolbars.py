from cms.extensions.toolbar import ExtensionToolbar
from cms.toolbar_pool import toolbar_pool
from django.utils.translation import gettext_lazy as _

from .models import PageMenuTarget


@toolbar_pool.register
class PageMenuTargetToolbar(ExtensionToolbar):
    model = PageMenuTarget

    def populate(self):
        current_page_menu = self._setup_extension_toolbar()
        if current_page_menu and self.toolbar.edit_mode_active:
            page_extension, url = self.get_page_extension_admin()
            if url:
                current_page_menu.add_modal_item(
                    _('Menu Link Target'),
                    url=url,
                    disabled=not self.toolbar.edit_mode_active,
                )
