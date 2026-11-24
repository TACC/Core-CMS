from django.test import SimpleTestCase, override_settings

from taccsite_cms.djangocms_blog.list_layout import portal_blog_list_layout


class PortalBlogListLayoutTests(SimpleTestCase):
    def test_string_applies_to_all_namespaces(self):
        with override_settings(PORTAL_BLOG_LIST_LAYOUT='grid'):
            self.assertEqual(portal_blog_list_layout('News'), 'grid')
            self.assertEqual(portal_blog_list_layout(None), 'grid')

    def test_dict_per_namespace_with_list_default(self):
        with override_settings(
            PORTAL_BLOG_LIST_LAYOUT={'News': 'list', 'Project Highlights': 'grid'},
        ):
            self.assertEqual(portal_blog_list_layout('News'), 'list')
            self.assertEqual(portal_blog_list_layout('Project Highlights'), 'grid')
            self.assertEqual(portal_blog_list_layout('Other'), 'list')

    def test_dict_default_key(self):
        with override_settings(PORTAL_BLOG_LIST_LAYOUT={'default': 'grid', 'News': 'list'}):
            self.assertEqual(portal_blog_list_layout('News'), 'list')
            self.assertEqual(portal_blog_list_layout('Other'), 'grid')

    def test_invalid_values_fall_back_to_list(self):
        with override_settings(PORTAL_BLOG_LIST_LAYOUT='carousel'):
            with self.assertLogs('portal.taccsite_cms.djangocms_blog.list_layout', level='WARNING') as logs:
                self.assertEqual(portal_blog_list_layout('News'), 'list')
            self.assertIn('carousel', logs.output[0])
