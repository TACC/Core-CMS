from cms.extensions.toolbar import ExtensionToolbar
from cms.toolbar_pool import toolbar_pool
from django.utils.translation import gettext_lazy as _

from .models import PageNavOptions


@toolbar_pool.register
class PageNavOptionsToolbar(ExtensionToolbar):
    model = PageNavOptions

    def populate(self):
        current_page_menu = self._setup_extension_toolbar()
        if current_page_menu and self.toolbar.edit_mode_active:
            page_options_menu = current_page_menu.get_or_create_menu(
                'page-custom-options',
                _('Page Options'),
            )
            page_extension, url = self.get_page_extension_admin()
            if url:
                page_options_menu.add_modal_item(
                    _('Nav Options'),
                    url=url,
                    disabled=not self.toolbar.edit_mode_active,
                )
