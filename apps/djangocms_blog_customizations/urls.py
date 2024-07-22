from django.urls import path
from .feeds import LatestEntriesFeed


app_name = 'djangocms_blog_customizations'
urlpatterns = [
    # Fails with `NoReverseMatch`
    # path('feed', LatestEntriesFeed(), name="djangocms_blog_customizations_feed"),
]
