from django.urls import re_path, include
from django.conf import settings

custom_urls = [

    # CUSTOM APP
    re_path(r'^custom_test/', include('apps.custom_example.urls', namespace='custom_test')),

    # SEARCH_PAGE
    re_path(r'^' + settings.PORTAL_SEARCH_PATH.strip('/') + '/', include('apps.search_page.urls', namespace='search')),

    # DJANGOCMS_BLOG
    re_path(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),

]
