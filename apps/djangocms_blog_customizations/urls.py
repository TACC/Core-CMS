from django.urls import re_path

from .feeds import LatestEntriesFeed
from .views import BlogView, BlogRemoteView


app_name = 'djangocms_blog_customizations'
urlpatterns = [
    # To render styled Blog feed
    # XXX: Does NOT style the feed
    # XXX: Does NOT customize the feed
    # FAQ: See errors at `/blog/feed/`, items at `/blog/feed/fb`
    # FAQ: See Blog app feed root at `/news/feed/`, items at `/news/feed/fb`
    re_path(r'^feed/', LatestEntriesFeed(), name='feed'),

    # To render current blog, content only (no Core-CMS base.html)
    # XXX: Does NOT render blog content
    # XXX: Does NOT escape Core-CMS base.html
    # FAQ: URL is `/blog/local`
    re_path(r'^local/', BlogView, name='base'),

    # To render a blog (or any page) from another website
    # XXX: URLs are still local
    # XXX: Is NOT blog-specific, so should be a generic feature
    # FAQ: URL is `/blog/remote`
    re_path(r'^remote/', BlogRemoteView.as_view(), name='remote'),
]
