from django.conf import settings
from menus.base import Modifier
from menus.menu_pool import menu_pool


class NewTabModifier(Modifier):
    """
    Annotate CMS nav nodes whose reverse_id is in PORTAL_CMS_MENU_NEW_TAB_PAGE_IDS
    with attr['new_tab'] = True, so the menu template can render target="_blank".

    SEE: https://docs.django-cms.org/en/release-3.11.x/how_to/menus.html#navigation-modifiers
    """

    # To run this modification AFTER built-in CMS modifiers
    # https://docs.django-cms.org/en/release-3.11.x/how_to/menus.html#performance-issues-in-menu-modifiers
    rating = 20

    # https://docs.django-cms.org/en/release-3.11.x/how_to/menus.html#how-it-works
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        if post_cut:
            page_ids = getattr(settings, 'PORTAL_CMS_MENU_NEW_TAB_PAGE_IDS', [])
            if page_ids:
                for node in nodes:
                    if node.attr.get('reverse_id') in page_ids:
                        node.attr['new_tab'] = True
        return nodes


menu_pool.register_modifier(NewTabModifier)
