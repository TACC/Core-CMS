from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from djangocms_link.cms_plugins import LinkPlugin

from taccsite_cms.contrib.helpers import (
    concat_classnames,
    add_classname_to_instances
)

from .models import TaccsiteArticleList

# Helpers

def get_layout_classname(value):
    """Get layout class based on value."""

    # HELP: Should we couple this map to LAYOUT_CHOICES? If so, how?
    switcher = {
        'widest-cols-2--even': 'c-article-list--layout-a',
        'widest-cols-2--wide-narr': 'c-article-list--layout-b',
        'widest-cols-2--narr-wide': 'c-article-list--layout-c',
        'widest-cols-3--even': 'c-article-list--layout-d',
        'always-rows-N--even': 'c-article-list--layout-e',
    }

    return switcher.get(value, '')

def get_style_classname(value):
    """Get style class based on value."""

    # HELP: Should we couple this map to STYLE_CHOICES? If so, how?
    switcher = {
        'divided-rows': 'c-article-list--style-divided',
        'gapless-cols': 'c-article-list--style-gapless',
    }

    return switcher.get(value, '')

# Bases

class AbstractArticleListPlugin(LinkPlugin):
    """
    Components > "Article List" Plugin
    https://confluence.tacc.utexas.edu/x/OIAjCQ
    """
    module = 'TACC Site'
    model = TaccsiteArticleList
    # abstract
    # name = _('______ Article List (Static)')
    render_template = 'article_list.html'
    def get_render_template(self, context, instance, placeholder):
        return self.render_template

    cache = True
    text_enabled = False
    allow_children = True

    fieldsets = [
        (None, {
            'fields': (
                'title_text',
                ('layout_type', 'style_type')
            )
        }),
        (_('Footer link'), {
            'classes': ('collapse',),
            'description': 'The "See All" link at the bottom of the list. "Display name" is the text.',
            'fields': (
                'name',
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

    # Render

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        request = context['request']

        classes = concat_classnames([
            'c-article-list',
            get_layout_classname(instance.layout_type),
            get_style_classname(instance.style_type),
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        add_classname_to_instances('c-article-list__item', instance.child_plugin_instances)

        context.update({
            'link_url': instance.get_link(),
            'link_text': instance.name,
            'link_target': instance.target
        })
        return context

# Plugin

@plugin_pool.register_plugin
class TaccsiteNewsArticleListPlugin(AbstractArticleListPlugin):
    """
    Components > "Article List" Plugin
    https://confluence.tacc.utexas.edu/x/OIAjCQ
    """
    name = _('News Article List (Static)')

    child_classes = [
        'TaccsiteStaticNewsArticlePreviewPlugin'
    ]

@plugin_pool.register_plugin
class TaccsiteAllocsArticleListPlugin(AbstractArticleListPlugin):
    """
    Components > "Article List" Plugin
    https://confluence.tacc.utexas.edu/x/OIAjCQ
    """
    name = _('Allocations Article List (Static)')

    child_classes = [
        'TaccsiteStaticAllocsArticlePreviewPlugin'
    ]
