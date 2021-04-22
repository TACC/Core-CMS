from django.test import TestCase
from django.test.client import RequestFactory

from django.contrib.auth.models import AnonymousUser, User

from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer

from taccsite_cms.contrib.taccsite_sample.cms_plugins import TaccsiteSamplePlugin
from taccsite_cms.contrib.taccsite_sample.models import TaccsiteSample

# TODO: Isolate model test from plugin test
class TaccsiteSampleTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.auth_user = None # set via _create_user()
        self.anon_user = AnonymousUser()
        self.context = None # set via _create_user()
        self.placeholder = Placeholder.objects.create(slot='test')
        self.plugin = None # set via _populate_plugin_model()



    # Helpers

    def _create_auth_user(self, username='test', first_name='', last_name=''):
        self.auth_user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email='123@test.com',
            password='top_secret'
        )
        self.context = { 'request': self.factory.get('/test/user') }
        self.context['request'].user = self.auth_user

    def _create_anon_user(self, guest_name='Guest'):
        self.auth_user = AnonymousUser()
        self.context = { 'request': self.factory.get('/test/user') }
        self.context['request'].user = self.anon_user

    def _populate_plugin_model(self, guest_name=None):
        data = {'guest_name': guest_name} if bool(guest_name) else {}
        self.plugin = add_plugin(
            self.placeholder,
            TaccsiteSamplePlugin,
            'en',
            **data
        )

    def _get_data(self):
        """Return context necessary for testing plugin logic"""
        plugin_instance = self.plugin.get_plugin_class_instance()
        data = plugin_instance.render(self.context, self.plugin, None)
        return data

    def _get_html(self):
        """Return markup necessary for testing plugin template"""
        renderer = ContentRenderer(request=self.factory)
        html = renderer.render_plugin(self.plugin, self.context)
        return html

    def _test_data(self, assertDict):
        """Reusable plugin logic test"""
        context = self._get_data()
        for key in assertDict.keys():
            self.assertIn(key, context)
            self.assertEqual(context[key], assertDict[key], msg=f"key='{key}'")

    def _test_html(self, assertDict):
        """Reusable plugin markup test"""
        html = self._get_html()
        self.assertTrue(html.find('Hello') > -1)
        self.assertTrue(html.find(assertDict['name']) > -1)



    # Tests

    # Tests: Guest User

    def test_anon_user_default(self):
        """Test guest user with plugin default value(s)"""
        self._create_anon_user()
        self._populate_plugin_model()
        assertDict = {
            'name': 'Guest',
            'has_proper_name': None,
            'is_authenticated': False
        }

        self._test_data(assertDict)
        self._test_html(assertDict)

    def test_anon_user_custom(self):
        """Test guest user with plugin custom value(s)"""
        self._create_anon_user(guest_name='Friend')
        self._populate_plugin_model(guest_name='Friend')
        assertDict = {
            'name': 'Friend',
            'has_proper_name': None,
            'is_authenticated': False
        }

        self._test_data(assertDict)
        self._test_html(assertDict)

    # Tests: Auth'd User

    def test_auth_user_username(self):
        """Test logged-in user with no first nor last name"""
        self._create_auth_user(username='fred')
        self._populate_plugin_model()
        assertDict = {
            'name': 'fred',
            'has_proper_name': False,
            'is_authenticated': True
        }

        self._test_data(assertDict)
        self._test_html(assertDict)

    def test_auth_user_lastname(self):
        """Test logged-in user with only last name"""
        self._create_auth_user(username='fred', last_name='Flintstone')
        self._populate_plugin_model()
        assertDict = {
            'name': 'fred',
            'has_proper_name': False,
            'is_authenticated': True
        }

        self._test_data(assertDict)
        self._test_html(assertDict)

    def test_auth_user_firstname(self):
        """Test logged-in user with only first name"""
        self._create_auth_user(username='fred', first_name='Fred')
        self._populate_plugin_model()
        assertDict = {
            'name': 'Fred',
            'has_proper_name': True,
            'is_authenticated': True
        }

        self._test_data(assertDict)
        self._test_html(assertDict)

    def test_auth_user_fullname(self):
        """Test logged-in user with first and last name"""
        self._create_auth_user(
            username='fred', first_name='Fred', last_name='Flintstone')
        self._populate_plugin_model()
        assertDict = {
            'name': 'Fred Flintstone',
            'has_proper_name': True,
            'is_authenticated': True
        }

        self._test_data(assertDict)
        self._test_html(assertDict)
