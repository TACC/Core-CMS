from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import gettext_lazy as _

class SearchPageMenu(Menu):

    def get_nodes(self, request):
        return [
            NavigationNode(
                title=_('Home'),
                url="/",
                id=1,
                visible=False,
            ),
            NavigationNode(
                title=_('Search'),
                url="/search/",
                id=2,
                visible=False,
            ),
        ]

menu_pool.register_menu(SearchPageMenu)
