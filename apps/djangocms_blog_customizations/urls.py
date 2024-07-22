from django.urls import re_path

from .feeds import LatestEntriesFeed
from .views import BlogView, BlogRemoteView


app_name = 'djangocms_blog_customizations'
urlpatterns = [
    # XXX: Does NOT render items within the feed
    re_path(r'^feed/', LatestEntriesFeed(), name='feed'),

    # XXX: Does not render blog content
    re_path(r'^local/', BlogView, name='base'),

    # XXX: URLs are still local
    re_path(r'^remote/', BlogRemoteView, name='remote'),
]
