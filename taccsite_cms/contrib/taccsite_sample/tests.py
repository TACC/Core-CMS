from django.test import TestCase
from django.test.client import RequestFactory

from django.contrib.auth.models import AnonymousUser, User

from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer

from taccsite_cms.contrib.taccsite_sample.cms_plugins import TaccsiteSamplePlugin
from taccsite_cms.contrib.taccsite_sample.models import TaccsiteSample

class TaccsiteSampleTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.auth_user = User()
        self.anon_user = AnonymousUser()
        self.context = { 'request': self.factory.get('/test/user') }
        self.placeholder = Placeholder.objects.create(slot='test')
        self.plugin = add_plugin(
            self.placeholder,
            TaccsiteSamplePlugin,
            'en',
        )

        print('[setUp] self.auth_user: ', self.auth_user)
        print('[setUp] User(): ', User())
        print('[setUp] self.anon_user: ', self.anon_user)
        print('[setUp] AnonymousUser(): ', AnonymousUser())

    # Helpers

    def _get_data(self):
        """Return context necessary for testing plugin logic"""
        plugin_instance = self.plugin.get_plugin_class_instance()
        context = plugin_instance.render(self.context, self.plugin, None)
        return context

    def _get_html(self):
        """Return markup necessary for testing plugin template"""
        renderer = ContentRenderer(request=self.factory)
        html = renderer.render_plugin(self.plugin, self.context)
        return html

    def _test_data(self, assertVals):
        """Reusable plugin logic test"""
        context = self._get_data()
        self.assertIn('name', context)
        self.assertEqual(context['name'], assertVals['name'])

    def _test_html(self, assertVals):
        """Reusable plugin markup test"""
        html = self._get_html()
        self.assertTrue(html.find('Hello') != -1)
        self.assertTrue(html.find(assertVals['name']) != -1)

    def _get_anon_user_vals(self):
        self.context['request'].user = self.anon_user

        return { 'name': 'Guest' }

    def _get_auth_user_vals(self):
        self.context['request'].user = self.auth_user

        print('self.auth_user: ', self.auth_user)
        print('self.auth_user.first_name: ', self.auth_user.first_name)
        print('self.auth_user.last_name: ', self.auth_user.last_name)

        return {
            'name': self.auth_user.first_name + ' ' + self.auth_user.last_name
        }

    # Tests

    def test_anon_user_data(self):
        """Test context of guest user"""
        assertVals = self._get_anon_user_vals()
        self._test_data(assertVals)

    def test_anon_user_html(self):
        """Test markup of guest user"""
        assertVals = self._get_anon_user_vals()
        self._test_html(assertVals)

    def test_auth_user_data(self):
        """Test context of logged-in user"""
        assertVals = self._get_auth_user_vals()
        self._test_data(assertVals)

    def test_auth_user_html(self):
        """Test markup of logged-in user"""
        assertVals = self._get_auth_user_vals()
        self._test_html(assertVals)
