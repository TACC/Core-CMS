from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from taccsite_cms.contrib.helpers import concat_classnames
from taccsite_cms.contrib.taccsite_static_article_list.models import (
    get_layout_classname, get_content_classname, get_style_classname
)

from .models import TaccsiteArticleList

@plugin_pool.register_plugin
class TaccsiteArticleListPlugin(CMSPluginBase):
    """
    Components > "Article List" Plugin
    https://confluence.tacc.utexas.edu/x/OIAjCQ
    """
    module = 'TACC Site'
    model = TaccsiteArticleList
    name = _('Article List (Static)')
    render_template = 'article_list.html'

    cache = True
    text_enabled = False
    allow_children = True
    child_classes = [
        'TaccsiteStaticNewsArticlePreviewPlugin'
    ]

    fieldsets = [
        (None, {
            'fields': (
                'header_title_text',
                'footer_link_text',
            )
        }),
        (_('Options'), {
            'fields': (
                'content_type',
                ('layout_type', 'style_type')
            )
        }),
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
            'c-article-list',
            get_layout_classname(instance.layout_type),
            get_content_classname(instance.content_type),
            get_style_classname(instance.style_type),
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        # for plugin_instance in instance.child_plugin_instances:
        #     plugin_instance.attributes['class'] += 'c-article-list__item'

        return context
