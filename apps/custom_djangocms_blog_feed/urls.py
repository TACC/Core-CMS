from django.urls import path

from .feeds import LatestEntriesFeed

# from apps.custom_example.views import CustomExampleView

app_name = 'custom_djangocms_blog_feed'
urlpatterns = [
    # To render styled Blog feed
    # XXX: Does NOT style the feed
    # XXX: Does NOT customize the feed
    # FAQ: See errors at `/blog/feed/`, items at `/blog/feed/fb`
    # FAQ: See Blog app feed root at `/news/feed/`, items at `/news/feed/fb`
    path('feed/', LatestEntriesFeed(), name='feed'),
    # path('feed/', CustomExampleView, name='feed'),
]
