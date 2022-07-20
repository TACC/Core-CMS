from django.urls import path, include

custom_urls = [
    path('test/', include('apps.test.urls', namespace='custom_test')),
]
