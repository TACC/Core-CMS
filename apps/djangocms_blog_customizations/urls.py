from django.urls import path
from .feeds import LatestEntriesFeed
from .views import BlogView


app_name = 'djangocms_blog_customizations'
urlpatterns = [
    # Fails with `NoReverseMatch`
    # path('feed', LatestEntriesFeed(), name="djangocms_blog_customizations_feed"),

    path('', BlogView, name='djangocms_blog_customizations_base'),
]
