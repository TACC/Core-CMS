import logging

logger = logging.getLogger(f"portal.{__name__}")

from .utils import is_app_installed

def extendBlogFeaturedPostsPlugin():
    if not is_app_installed():
        logger.debug('Not extending djangocms_blog, because it is not installed')
        return

    from django import forms
    from django.utils.html import format_html
    from django.utils.translation import gettext_lazy as _

    from cms.plugin_pool import plugin_pool

    from djangocms_blog.cms_plugins import BlogFeaturedPostsPlugin as OriginalBlogFeaturedPostsPlugin
    from djangocms_blog.models import FeaturedPostsPlugin

    class FeaturedPostsForm(forms.ModelForm):
        class Media:
            css = {
                'all': ('djangocms_blog/css/admin/featured_posts_ordered.css',)
            }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if 'posts' in self.fields:
                def label_with_data_attr(obj):
                    if obj.publish:
                        status_value = 'true'
                        status_text = _('Published')
                    else:
                        status_value = 'false'
                        status_text = _('Unpublished')
                    return format_html(
                        '<span data-published="{}">{}</span> {}',
                        status_value,
                        status_text,
                        obj.title
                    )
                self.fields['posts'].label_from_instance = label_with_data_attr

        class Meta:
            model = FeaturedPostsPlugin
            fields = '__all__'

    class BlogFeaturedPostsPlugin(OriginalBlogFeaturedPostsPlugin):
        form = FeaturedPostsForm

    plugin_pool.unregister_plugin(OriginalBlogFeaturedPostsPlugin)
    plugin_pool.register_plugin(BlogFeaturedPostsPlugin)

def extendBlogFeaturedPostsPluginCached():
    if not is_app_installed():
        logger.debug('Not extending djangocms_blog, because it is not installed')
        return

    from django import forms
    from cms.plugin_pool import plugin_pool
    from djangocms_blog.cms_plugins import BlogFeaturedPostsPluginCached as OriginalBlogFeaturedPostsPluginCached
    from djangocms_blog.models import FeaturedPostsPlugin

    class FeaturedPostsForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if 'posts' in self.fields:
                self.fields['posts'].label_from_instance = lambda obj: (
                    f"✓ {obj.title}" if obj.publish else f"○ {obj.title}"
                )

        class Meta:
            model = FeaturedPostsPlugin
            fields = '__all__'

    class BlogFeaturedPostsPluginCached(OriginalBlogFeaturedPostsPluginCached):
        form = FeaturedPostsForm

    plugin_pool.unregister_plugin(OriginalBlogFeaturedPostsPluginCached)
    plugin_pool.register_plugin(BlogFeaturedPostsPluginCached)
