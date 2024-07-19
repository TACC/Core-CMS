from django.urls import path
from .feeds import LatestEntriesFeed

app_name = 'djangocms_blog_customizations'
urlpatterns = [
    path('', LatestEntriesFeed(), name="custom-posts-latest-feed"),
]
