from django.core.exceptions import ValidationError

from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from djangocms_link.cms_plugins import LinkPlugin

from taccsite_cms.contrib.helpers import (
    concat_classnames,
    insert_at_position,
    which_date_is_nearest_today,
    AbstractMaxChildrenPlugin,
)

from .models import (
    MEDIA_SUPPORT_CHOICES,
    TaccsiteStaticNewsArticlePreview,
    TaccsiteStaticAllocsArticlePreview,
    TaccsiteStaticDocsArticlePreview,
    TaccsiteStaticEventsArticlePreview,
)



# Constants

KIND_DICT = {
    'news': 'c-article-preview--news',
    'docs': 'c-article-preview--docs',
    'allocs': 'c-article-preview--allocs',
    'events': 'c-article-preview--events',
}



# Helpers

# FAQ: This exists to retireve classnames via consistently-named functions
# SEE: taccsite_cms.contrib.taccsite_static_article_list.cms_plugins
def get_kind_classname(value):
    """Get kind class based on value."""
    return KIND_DICT[value]



# Abstracts

class AbstractArticlePreviewPlugin(LinkPlugin, AbstractMaxChildrenPlugin):
    module = 'TACC Site'
    # model = TaccsiteStatic___ArticlePreview # abstract
    # name = _('______ Article Preview (Static)') # abstract
    render_template = 'static_article_preview.html'
    def get_render_template(self, context, instance, placeholder):
        return self.render_template

    cache = True
    text_enabled = False
    # NOTE: Should article previews be allowed to exist in isolation?
    #       Consider [hero banner](https://github.com/TACC/Core-CMS/issues/134).
    # require_parent = True

    fieldsets = [
        (_('Link'), {
            'fields': (
                ('external_link', 'internal_link'),
                ('anchor', 'target'),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'attributes',
            )
        }),
    ]



    # Helpers

    # kind = '______' # abstract



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
            'kind': self.kind,
            'link_url': instance.get_link(),
            'link_text': instance.name,
            'link_target': instance.target
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
            # 'fields': (..., 'picture', 'external_picture')
            'fields': ('title_text', 'abstract_text')
        }),
    ])
    fieldsets = insert_at_position(len(fieldsets) - 1, fieldsets, [
        (_('Metadata'), {
            'fields': ('publish_date', 'type_text', 'author_text')
        }),
    ])



    # Helpers

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
            'description': 'Two dates will show a range. If given one date, the nearest future date is shown. Otherwise, the nearest past date is shown.',
            'fields': (('publish_date', 'expiry_date'),)
        }),
    ])



    # Helper

    kind = 'allocs'



    # Render
    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        request = context['request']

        dates = which_date_is_nearest_today(
            instance.publish_date,
            instance.expiry_date,
            'future'
        )
        (should_show_open_date, open_date_time_period) = dates[0]
        (should_show_close_date, close_date_time_period) = dates[1]

        context.update({
            'open_date': instance.publish_date,
            'should_show_open_date': should_show_open_date,
            'open_date_time_period': open_date_time_period,

            'close_date': instance.expiry_date,
            'should_show_close_date': should_show_close_date,
            'close_date_time_period': close_date_time_period,
        })
        return context

@plugin_pool.register_plugin
class TaccsiteStaticDocsArticlePreviewPlugin(AbstractArticlePreviewPlugin):
    """
    Components > "(Static) Document Article Preview" Plugin
    https://confluence.tacc.utexas.edu/x/OYAjCQ
    """
    model = TaccsiteStaticDocsArticlePreview
    name = _('Document Article Preview (Static)')

    parent_classes = [
        'TaccsiteDocsArticleListPlugin'
    ]

    fieldsets = insert_at_position(0, AbstractArticlePreviewPlugin.fieldsets, [
        (None, {
            'fields': ('title_text', 'abstract_text')
        }),
    ])



    # Helpers

    kind = 'docs'

@plugin_pool.register_plugin
class TaccsiteStaticEventsArticlePreviewPlugin(AbstractArticlePreviewPlugin):
    """
    Components > "(Static) Event Article Preview" Plugin
    https://confluence.tacc.utexas.edu/x/OYAjCQ
    """
    model = TaccsiteStaticEventsArticlePreview
    name = _('Event Article Preview (Static)')

    parent_classes = [
        'TaccsiteEventsArticleListPlugin'
    ]

    fieldsets = insert_at_position(0, AbstractArticlePreviewPlugin.fieldsets, [
        (None, {
            'fields': (
                ('publish_date', 'expiry_date'),
                'title_text',
                'abstract_text'
            )
        }),
    ])



    # Helpers

    kind = 'events'



    # Render
    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        request = context['request']

        context.update({
            'open_date': instance.publish_date,
            'close_date': instance.expiry_date,
        })
        return context
