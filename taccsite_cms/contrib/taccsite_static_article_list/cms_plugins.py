from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from taccsite_cms.contrib.helpers import concat_classnames

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
        'divided': 'c-article-list--style-divided',
    }

    return switcher.get(value, '')

# Plugin

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
        'TaccsiteStaticNewsArticlePreviewPlugin',
        'TaccsiteStaticAllocsArticlePreviewPlugin'
    ]

    fieldsets = [
        (None, {
            'fields': (
                'header_title_text',
                'footer_link_text',
                # TODO: Add `footer_link_url`
            )
        }),
        (_('Options'), {
            'fields': (
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
            get_style_classname(instance.style_type),
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        # for plugin_instance in instance.child_plugin_instances:
        #     plugin_instance.attributes['class'] += 'c-article-list__item'

        return context
