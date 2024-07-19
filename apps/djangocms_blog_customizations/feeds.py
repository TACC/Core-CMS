from html import unescape
from io import BytesIO

from aldryn_apphooks_config.utils import get_app_instance
from django.contrib.sites.models import Site
from django.urls import reverse
from django.utils.feedgenerator import Rss201rev2Feed
from django.utils.translation import gettext as _

from djangocms_blog.feeds import LatestEntriesFeed as DjangoCMSBlogLatestEntriesFeed
from djangocms_blog.settings import get_setting
from djangocms_blog.models import Post


class LatestEntriesFeed(DjangoCMSBlogLatestEntriesFeed):
    feed_type = Rss201rev2Feed
    feed_items_number = get_setting("FEED_LATEST_ITEMS")
