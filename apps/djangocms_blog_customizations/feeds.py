from aldryn_apphooks_config.utils import get_app_instance
from django.utils.feedgenerator import Rss201rev2Feed

from djangocms_blog.feeds import LatestEntriesFeed as DjangoCMSBlogLatestEntriesFeed
from djangocms_blog.settings import get_setting
from djangocms_blog.cms_appconfig import BlogConfig

# XXX: This file is loaded, but it does NOT override the feed
# XXX: Logging via logger fails anywhere; via print fails inside any method
class LatestEntriesFeed(DjangoCMSBlogLatestEntriesFeed):
    feed_type = Rss201rev2Feed
    feed_items_number = get_setting("FEED_LATEST_ITEMS")

    print(f"CUSTOM FEED | FEED_LATEST_ITEMS: {feed_items_number}")

    def __call__(self, request, *args, **kwargs):
        namespace = get_setting("AUTO_NAMESPACE")

        self.request = request
        self.namespace = get_setting("AUTO_NAMESPACE")
        self.config = BlogConfig.objects.get(namespace=namespace)

        print(f"CUSTOM FEED | NAMESPACE: {self.namespace}, CONFIG: {self.config}")

        return super().__call__(request, *args, **kwargs)

    def items(self):
        items = super().items()

        print(f"CUSTOM FEED | FEED ITEMS: {items}")

        return items
