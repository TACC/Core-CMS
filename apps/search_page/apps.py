from django.apps import AppConfig


class SearchPageConfig(AppConfig):
    name = 'apps.search_page'

    def ready(self):
        from .utils import create_search_page
        create_search_page()
