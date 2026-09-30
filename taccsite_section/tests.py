from django.test import SimpleTestCase, TestCase
from django.test.client import RequestFactory

from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer

from taccsite_section.cms_plugins import TaccsiteSectionPlugin
from taccsite_section.utils import (
    section_type_to_class_string,
    normalize_section_class_tokens,
)


class TaccsiteSectionUtilsTests(SimpleTestCase):
    def test_section_type_mapping(self):
        self.assertEqual(section_type_to_class_string('_'), '')
        self.assertEqual(
            section_type_to_class_string('container  o-section o-section--style-muted'),
            'container  o-section o-section--style-muted',
        )

    def test_normalize_additional_classes(self):
        self.assertEqual(
            normalize_section_class_tokens('foo, bar'),
            'foo bar',
        )


class TaccsiteSectionPluginTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.placeholder = Placeholder.objects.create(slot='test')
        self.context = {'request': self.factory.get('/test')}

    def _add_section(self, **kwargs):
        defaults = {
            'class_name': 'o-section o-section--style-muted',
            'tag_type': 'section',
        }
        defaults.update(kwargs)
        return add_plugin(
            self.placeholder,
            TaccsiteSectionPlugin,
            'en',
            **defaults,
        )

    def test_render_section_classes(self):
        section_type = 'o-section o-section--style-accent'
        plugin = self._add_section(class_name=section_type)
        plugin_class = plugin.get_plugin_class_instance()
        context = plugin_class.render(self.context, plugin, self.placeholder)
        self.assertEqual(
            context['section_class_str'],
            'o-section o-section--style-accent',
        )

    def test_html_renders_section_element(self):
        plugin = self._add_section(
            class_name='o-section o-section--style-light',
        )
        html = ContentRenderer(request=self.factory).render_plugin(
            plugin,
            self.context,
        )
        self.assertIn('<section', html)
        self.assertIn('o-section o-section--style-light', html)
