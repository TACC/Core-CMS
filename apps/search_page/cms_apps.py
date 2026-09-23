from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class SearchPageApphook(CMSApp):
    app_name = 'apps.search_page'
    name = 'SearchPage'

    def get_urls(self, page=None, language=None, **kwargs):
        return ['apps.search_page.urls']
