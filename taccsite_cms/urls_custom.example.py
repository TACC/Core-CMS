from django.urls import path, include

custom_urls = [
    path('custom_test/', include('apps.custom_example.urls', namespace='custom_test')),
]
