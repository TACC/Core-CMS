from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from taccsite_cms.contrib.helpers import (
    concat_classnames,
    insert_at_position,
    CMSPluginBaseWithMaxChildren
)

from .models import TaccsiteStaticNewsArticlePreview, MEDIA_SUPPORT_CHOICES

# Base

class ArticlePreviewPlugin(CMSPluginBaseWithMaxChildren):
    cache = True
    text_enabled = False
    allow_children = False

    fieldsets = [
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'attributes',
            )
        }),
    ]

    # Render

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        request = context['request']

        classes = concat_classnames([
            'c-article-preview',
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        context.update({
            'kind': self.kind
        })
        return context

# Plugins

@plugin_pool.register_plugin
class TaccsiteStaticNewsArticlePreviewPlugin(ArticlePreviewPlugin):
    """
    Components > "(Static) News Article Preview" Plugin
    https://confluence.tacc.utexas.edu/x/OYAjCQ
    """
    module = 'TACC Site'
    model = TaccsiteStaticNewsArticlePreview
    name = _('News Article Preview (Static)')
    render_template = 'static_article_preview.html'

    cache = True
    text_enabled = False
    allow_children = False
    child_classes = [
        'PicturePlugin', # HELP: Why is this not available in plugin list?
        'Bootstrap4PicturePlugin'
    ]
    parent_classes = [
        'TaccsiteArticleListPlugin'
    ]
    # NOTE: Should article previews be allowed to exist in isolation?
    #       Consider [hero banner](https://github.com/TACC/Core-CMS/issues/134).
    # require_parent = True

    fieldsets = insert_at_position(0, ArticlePreviewPlugin.fieldsets, [
        (None, {
            # To enable these fields, see `./README.md`
            # 'fields': ('picture', 'external_picture')
            'fields': ('title_text', 'abstract_text')
        }),
        (_('Image'), {
            # To enable these fields, see `./README.md`
            # 'fields': ('picture', 'external_picture')
            'fields': ('media_support',)
        }),
        (_('Metadata'), {
            'fields': ('publish_date', 'type_text', 'author_text')
        }),
    ])

    # Custom Properties

    kind = 'news'

    # Set `readonly_fields` that can be populated upon instance creation
    # SEE: https://stackoverflow.com/a/17614057/11817077
    # HELP: Instead, how can we disable a field with minimal effort?
    def get_readonly_fields(self, request, obj=None):
        if obj: # i.e. user is editing instance
            return ['media_support'] if len(MEDIA_SUPPORT_CHOICES) == 1 else []
        else:   # i.e. user is creating instance
            return []
