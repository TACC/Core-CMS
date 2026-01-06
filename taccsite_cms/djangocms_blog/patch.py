import logging

logger = logging.getLogger(f"portal.{__name__}")

# To monkey-patch nephila/djangocms-blog until v2.0.6+
# TODO: After upgrading to v2.0.6+, delete this file and its imports
def patchDjangoCMSBlog():
        from django.apps import apps
        if not apps.is_installed('djangocms_blog'):
            logger.debug('djangocms_blog not installed, skipping patches')
            return

        from djangocms_blog.models import BasePostPlugin, FeaturedPostsPlugin

        # To monkey-patch nephila/djangocms-blog#782 into v2.0.3
        # https://github.com/nephila/djangocms-blog/pull/782
        logger.info(f'Patching FeaturedPostsPlugin with nephila/djangocms-blog#782')
        def patched_str(self):
            # TACC: deps ad-hoc
            from django.utils.encoding import force_str
            from django.utils.translation import gettext_lazy as _
            # /TACC: deps ad-hoc

            return force_str(_("Featured posts"))

        FeaturedPostsPlugin.__str__ = patched_str

        # To monkey-patch nephila/djangocms-blog#783 into v2.0.3
        # https://github.com/nephila/djangocms-blog/pull/783
        logger.info(f'Patching BasePostPlugin, FeaturedPostsPlugin with nephila/djangocms-blog#783')
        def patched_post_queryset(self, request=None, published_only=True, selected_posts=None):
            # TACC: deps ad-hoc
            from djangocms_blog.models import Post
            from django.contrib.sites.shortcuts import get_current_site
            from django.utils.translation import get_language
            # /TACC: deps ad-hoc

            language = get_language()
            posts = Post.objects if not selected_posts else selected_posts
            if self.app_config:
                posts = posts.namespace(self.app_config.namespace)
            if self.current_site:
                posts = posts.on_site(get_current_site(request))
            posts = posts.active_translations(language_code=language)
            if (
                published_only
                or not request
                or not getattr(request, "toolbar", False)
                or not request.toolbar.edit_mode_active
            ):
                posts = posts.published(current_site=self.current_site)
            return self.optimize(posts.all())

        def patched_get_posts(self, request, published_only=True):
            posts = self.post_queryset(request, published_only, selected_posts=self.posts.all())
            return posts

        BasePostPlugin.post_queryset = patched_post_queryset
        FeaturedPostsPlugin.get_posts = patched_get_posts
