from django.urls import re_path

from .feeds import LatestEntriesFeed
from .views import BlogView, BlogRemoteView


app_name = 'djangocms_blog_customizations'
urlpatterns = [
    # WARNING: Renders feed, but does nto render items within the feed
    re_path(r'^feed/', LatestEntriesFeed(), name='djangocms_blog_customizations_feed'),

    re_path(r'^local/', BlogView, name='djangocms_blog_customizations_base'),
    re_path(r'^remote/', BlogRemoteView, name='djangocms_blog_customizations_remote'),
]
