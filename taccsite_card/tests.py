from django.test import SimpleTestCase, TestCase
from django.test.client import RequestFactory

from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer

from taccsite_card.cms_plugins import TaccsiteCardPlugin
from taccsite_card.constants import (
    class_name_to_skin_modifier,
    normalize_card_class_tokens,
)


class TaccsiteCardConstantsTests(SimpleTestCase):
    def test_skin_modifier_mapping(self):
        self.assertEqual(class_name_to_skin_modifier('c-card'), '')
        self.assertEqual(class_name_to_skin_modifier('c-card--plain'), 'c-card--plain')
        self.assertEqual(class_name_to_skin_modifier('c-card--standard'), 'c-card--standard')
        self.assertEqual(class_name_to_skin_modifier('card--plain'), '')

    def test_normalize_additional_classes(self):
        self.assertEqual(
            normalize_card_class_tokens('c-card--plain, foo'),
            'c-card--plain foo',
        )
        self.assertEqual(
            normalize_card_class_tokens('c-card, foo'),
            'foo',
        )


class TaccsiteCardPluginTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.placeholder = Placeholder.objects.create(slot='test')
        self.context = {'request': self.factory.get('/test')}

    def _add_card(self, **kwargs):
        defaults = {
            'class_name': 'c-card--standard',
            'template': 'default',
        }
        defaults.update(kwargs)
        return add_plugin(
            self.placeholder,
            TaccsiteCardPlugin,
            'en',
            **defaults,
        )

    def test_render_skin_classes(self):
        plugin = self._add_card(class_name='c-card--plain', template='default')
        plugin_class = plugin.get_plugin_class_instance()
        context = plugin_class.render(self.context, plugin, self.placeholder)
        self.assertEqual(context['skin_classes'], 'c-card--plain')

    def test_html_stacks_skin_and_layout(self):
        plugin = self._add_card(class_name='c-card--standard', template='image_top')
        html = ContentRenderer(request=self.factory).render_plugin(
            plugin,
            self.context,
        )
        self.assertIn('c-card', html)
        self.assertIn('c-card--standard', html)
        self.assertIn('c-card--image-top', html)

    def test_get_render_template_layout(self):
        plugin = self._add_card(template='image_bottom')
        plugin_class = plugin.get_plugin_class_instance()
        path = plugin_class.get_render_template(self.context, plugin, self.placeholder)
        self.assertEqual(path, 'taccsite_card/layouts/image_bottom.html')

        plugin.template = 'default'
        path = plugin_class.get_render_template(self.context, plugin, self.placeholder)
        self.assertEqual(path, 'taccsite_card/base.html')
