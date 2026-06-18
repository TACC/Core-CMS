"""Tests for header logo picture class handling (portal-logo on <img>)."""

from django.template.loader import get_template
from django.test import SimpleTestCase

from taccsite_cms.contrib.taccsite_header_logo.cms_plugins import apply_header_logo_classes
from taccsite_cms.tests.djangocms_picture_default_caption import _FakePicture


def _render_default(instance, *, picture_link='', picture_img_class=None):
    context = {
        'instance': instance,
        'picture_link': picture_link,
        'img_srcset_data': [],
    }
    if picture_img_class is not None:
        context['picture_img_class'] = picture_img_class
    return get_template('djangocms_picture/default/picture.html').render(context)


class PortalLogoPictureTests(SimpleTestCase):
    def test_portal_logo_on_img_when_no_link(self):
        instance = _FakePicture(attributes={'alt': 'Project logo'})
        ctx = {}
        apply_header_logo_classes(instance, ctx, picture_link='')
        instance.attributes_str = (
            f' class="{instance.attributes["class"]}"'
            f' alt="{instance.attributes["alt"]}"'
        )
        html = _render_default(instance, picture_link='')
        self.assertIn('navbar-brand portal-logo', html)
        self.assertNotIn('picture_img_class', ctx.keys())

    def test_portal_logo_on_img_when_linked(self):
        instance = _FakePicture(
            attributes={'alt': 'Project logo'},
            attributes_str=' class="navbar-brand"',
        )
        ctx = {}
        apply_header_logo_classes(instance, ctx, picture_link='/')
        html = _render_default(
            instance,
            picture_link='/',
            picture_img_class=ctx.get('picture_img_class'),
        )
        self.assertEqual(ctx.get('picture_img_class'), 'portal-logo')
        self.assertIn('navbar-brand', html)
        self.assertIn('class="portal-logo"', html)
