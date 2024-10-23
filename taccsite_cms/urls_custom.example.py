from django.urls import re_path, include
from django.conf import settings

custom_urls = [

    # CUSTOM APP
    re_path(r'^custom_test/', include('apps.custom_example.urls', namespace='custom_test')),

    # DJANGOCMS_BLOG
    re_path(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),

]
