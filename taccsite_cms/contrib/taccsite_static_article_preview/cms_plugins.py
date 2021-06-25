
from django.core.exceptions import ValidationError

from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from taccsite_cms.contrib.helpers import (
    concat_classnames,
    insert_at_position,
    which_date_is_nearest_today,
    CMSPluginBaseWithMaxChildren,
)

from .models import (
    MEDIA_SUPPORT_CHOICES,
    TaccsiteStaticNewsArticlePreview,
    TaccsiteStaticAllocsArticlePreview,
)

# Helpers

def get_kind_classname(value):
    """Get kind class based on value."""

    switcher = {
        'news': 'c-article-preview--news',
        'docs': 'c-article-preview--links',
        'allocs': 'c-article-preview--allocs',
        'events': 'c-article-preview--events',
    }

    return switcher.get(value, '')

# Bases

class AbstractArticlePreviewPlugin(CMSPluginBaseWithMaxChildren):
    module = 'TACC Site'
    # abstract
    # model = TaccsiteStatic___ArticlePreview
    # abstract
    # name = _('______ Article Preview (Static)')
    render_template = 'static_article_preview.html'

    cache = True
    text_enabled = False
    # NOTE: Should article previews be allowed to exist in isolation?
    #       Consider [hero banner](https://github.com/TACC/Core-CMS/issues/134).
    # require_parent = True

    fieldsets = [
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'attributes',
            )
        }),
    ]

    # Custom

    # abstract
    # kind = '______'

    # Render

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        request = context['request']

        classes = concat_classnames([
            'c-article-preview',
            get_kind_classname(self.kind),
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        context.update({
            'kind': self.kind
        })
        return context

class AbstractArticlePreviewWithMediaPlugin(AbstractArticlePreviewPlugin):
    allow_children = True
    child_classes = [
        'PicturePlugin', # HELP: Why does this not show up in plugin list?
        'Bootstrap4PicturePlugin'
    ]

    fieldsets = insert_at_position(0, AbstractArticlePreviewPlugin.fieldsets, [
        (_('Image'), {
            # To enable these fields, see `./README.md`
            # 'fields': ('picture', 'external_picture')
            'fields': ('media_support',)
        }),
    ])

    # Set `readonly_fields` that can be populated upon instance creation
    # SEE: https://stackoverflow.com/a/17614057/11817077
    # HELP: Instead, how can we disable a field with minimal effort?
    def get_readonly_fields(self, request, obj=None):
        if obj: # i.e. user is editing instance
            return ['media_support'] if len(MEDIA_SUPPORT_CHOICES) == 1 else []
        else:   # i.e. user is creating instance
            return []

# Plugins
# TODO: Add `TaccsiteStatic___ArticlePreviewPlugin` (Docs, Allocs, Events)

@plugin_pool.register_plugin
class TaccsiteStaticNewsArticlePreviewPlugin(AbstractArticlePreviewWithMediaPlugin):
    """
    Components > "(Static) News Article Preview" Plugin
    https://confluence.tacc.utexas.edu/x/OYAjCQ
    """
    model = TaccsiteStaticNewsArticlePreview
    name = _('News Article Preview (Static)')

    parent_classes = [
        'TaccsiteNewsArticleListPlugin'
    ]

    fieldsets = insert_at_position(0, AbstractArticlePreviewWithMediaPlugin.fieldsets, [
        (None, {
            # To enable these fields, see `./README.md`
            # 'fields': ('picture', 'external_picture')
            'fields': ('title_text', 'abstract_text')
        }),
    ])
    fieldsets = insert_at_position(len(fieldsets) - 1, fieldsets, [
        (_('Metadata'), {
            'fields': ('publish_date', 'type_text', 'author_text')
        }),
    ])

    # Custom

    kind = 'news'

@plugin_pool.register_plugin
class TaccsiteStaticAllocsArticlePreviewPlugin(AbstractArticlePreviewWithMediaPlugin):
    """
    Components > "(Static) Allocations Article Preview" Plugin
    https://confluence.tacc.utexas.edu/x/OYAjCQ
    """
    model = TaccsiteStaticAllocsArticlePreview
    name = _('Allocations Article Preview (Static)')

    parent_classes = [
        'TaccsiteAllocsArticleListPlugin'
    ]

    fieldsets = insert_at_position(0, AbstractArticlePreviewWithMediaPlugin.fieldsets, [
        (None, {
            # To enable these fields, see `./README.md`
            # 'fields': ('picture', 'external_picture')
            'fields': ('title_text',)
        }),
    ])
    fieldsets = insert_at_position(len(fieldsets) - 1, fieldsets, [
        (_('Dates'), {
            'description': 'If available, the nearest future date is shown. Otherwise, the nearest past date is shown. Matching dates will both be shown.',
            'fields': (('publish_date', 'expiry_date'),)
        }),
    ])

    # Custom

    kind = 'allocs'

    # Render

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        request = context['request']

        show_show_dates = which_date_is_nearest_today(
            instance.publish_date,
            instance.expiry_date,
            'future'
        )

        context.update({
            'should_show_open_date': show_show_dates[0],
            'should_show_close_date': show_show_dates[1]
        })
        return context
