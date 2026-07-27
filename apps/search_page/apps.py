from django.apps import AppConfig
from django.conf import settings

class SearchPageConfig(AppConfig):
    name = 'apps.search_page'

    def ready(self):
        if settings.SEARCH_PAGE_AUTO_SETUP:
            from .utils import create_page
            create_page()
