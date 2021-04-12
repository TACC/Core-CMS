from django.test import TestCase
from django.test.client import RequestFactory

from django.contrib.auth.models import AnonymousUser, User

from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer

from taccsite_cms.contrib.taccsite_greet.cms_plugins import TaccsiteGreetPlugin
from taccsite_cms.contrib.taccsite_greet.models import TaccsiteGreet

class TaccsiteGreetTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.auth_user = User()
        self.anon_user = AnonymousUser()
        self.context = { 'request': self.factory.get('/test/user') }
        self.placeholder = Placeholder.objects.create(slot='test')
        self.plugin = add_plugin(
            self.placeholder,
            TaccsiteGreetPlugin,
            'en',
        )

    # Helpers

    def _get_context(self):
        """Return context necessary for testing plugin logic"""
        plugin_instance = self.plugin.get_plugin_class_instance()
        context = plugin_instance.render(self.context, self.plugin, None)
        return context

    def _get_html(self):
        """Return markup necessary for testing plugin template"""
        renderer = ContentRenderer(request=self.factory)
        html = renderer.render_plugin(self.plugin, self.context)
        return html

    def _test_context(self, assertVals):
        """Reusable plugin logic test"""
        context = self._get_context()
        self.assertIn('user_name', context)
        self.assertEqual(context['user_name'], assertVals['name'])

    def _test_html(self, assertVals):
        """Reusable plugin markup test"""
        html = self._get_html()
        self.assertEqual(html, '<h1>Hello, ' + assertVals['name'] + '.</h1>\n')

    # Tests

    def test_anon_user(self):
        """Test name of unauthenticated user"""
        self.context['request'].user = self.anon_user

        assertVals = { 'name': 'Guest' }

        self._test_context(assertVals)
        self._test_html(assertVals)

    def test_auth_user_context(self):
        """Test name of authenticated user"""
        self.context['request'].user = self.auth_user

        assertVals = {
            'name': self.auth_user.first_name + ' ' + self.auth_user.last_name
        }

        self._test_context(assertVals)
        self._test_html(assertVals)
