from django.urls import re_path

from .feeds import LatestEntriesFeed
from .views import BlogView, BlogRemoteView


app_name = 'djangocms_blog_customizations'
urlpatterns = [
    # To render styled Blog feed
    # XXX: Does NOT style the feed
    # XXX: Does NOT render items within the feed
    re_path(r'^feed/', LatestEntriesFeed(), name='feed'),

    # To render current blog, content only (no Core-CMS base.html)
    # XXX: Does NOT render blog content
    # XXX: Does NOT escape Core-CMS base.html
    re_path(r'^local/', BlogView, name='base'),

    # To render a blog (or any page) from another website
    # XXX: URLs are still local
    # XXX: Is NOT blog-specific, so should be a generic feature
    re_path(r'^remote/', BlogRemoteView.as_view(), name='remote'),
]
