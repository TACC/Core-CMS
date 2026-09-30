from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from djangocms_style.cms_plugins import StylePlugin
from djangocms_style.models import Style

from taccsite_cms.contrib.helpers import concat_classnames

from .forms import TaccsiteSectionPluginForm
from .utils import (
    attributes_str_without_class,
    normalize_section_class_tokens,
    section_type_to_class_string,
)


@plugin_pool.register_plugin
class TaccsiteSectionPlugin(StylePlugin):
    """
    TACC Site wrapper around Style plugin for Core-Styles sections.
    - Name: label.
    - Type: class_name (Bootstrap Container plugin “Section only” choices).
    """

    module = 'TACC Site'
    model = Style
    name = _('Section')
    form = TaccsiteSectionPluginForm
    render_template = 'taccsite_section/base.html'

    fieldsets = (
        (None, {
            'fields': (
                'label',
                'class_name',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'tag_type',
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
        return self.render_template

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)

        type_classes = section_type_to_class_string(instance.class_name)
        additional_class_str = normalize_section_class_tokens(
            instance.get_additional_classes()
        )

        attr_class = (instance.attributes or {}).get('class')
        if attr_class:
            additional_class_str = concat_classnames([
                additional_class_str,
                normalize_section_class_tokens(attr_class),
            ])

        context.update({
            'section_class_str': concat_classnames([
                type_classes,
                additional_class_str,
            ]),
            'attributes_str': attributes_str_without_class(instance),
        })
        return context
