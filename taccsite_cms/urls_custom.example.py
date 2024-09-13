from django.urls import re_path, include

custom_urls = [
    re_path(r'^custom_test/', include('apps.custom_example.urls', namespace='custom_test')),
]
