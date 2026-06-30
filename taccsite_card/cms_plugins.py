from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from djangocms_style.cms_plugins import StylePlugin
from djangocms_style.models import Style

from taccsite_cms.contrib.helpers import concat_classnames

from .utils import (
    attributes_str_without_class,
    class_name_to_skin_modifier,
    normalize_card_class_tokens,
)
from .forms import TaccsiteCardPluginForm


@plugin_pool.register_plugin
class TaccsiteCardPlugin(StylePlugin):
    """
    TACC Site wrapper around Style for Core-Styles c-card (block + stacked BEM modifiers).

    Skin: class_name. Layout: template (separate Django templates, Way 1).
    """

    module = 'TACC Site'
    model = Style
    name = _('Card')
    form = TaccsiteCardPluginForm

    fieldsets = (
        (None, {
            'fields': (
                ('label'),
                ('class_name', 'template'),
                'tag_type',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'id_name',
                'additional_classes',
                'attributes',
            ),
        }),
        (_('Inline style settings'), {
            'classes': ('collapse',),
            'fields': (
                ('padding_top', 'padding_right',
                 'padding_bottom', 'padding_left'),
                ('margin_top', 'margin_right',
                 'margin_bottom', 'margin_left'),
            ),
        }),
    )

    def get_render_template(self, context, instance, placeholder):
        layout = instance.template or 'default'
        if layout == 'default':
            return 'taccsite_card/base.html'
        return f'taccsite_card/layouts/{layout}.html'

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)

        skin_classes = class_name_to_skin_modifier(instance.class_name)
        additional_class_str = normalize_card_class_tokens(
            instance.get_additional_classes()
        )
        attr_class = (instance.attributes or {}).get('class')
        if attr_class:
            additional_class_str = concat_classnames([
                additional_class_str,
                normalize_card_class_tokens(attr_class),
            ])

        context.update({
            'skin_classes': skin_classes,
            'additional_class_str': additional_class_str,
            'attributes_str': attributes_str_without_class(instance),
        })
        return context
