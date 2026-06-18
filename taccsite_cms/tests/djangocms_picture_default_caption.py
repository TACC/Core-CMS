"""Tests for the TACC `default_caption` fallback in the Picture template.

The override at
``taccsite_cms/templates/djangocms_picture/default/picture.html`` falls back to
the filer Image's ``default_caption`` for the ``<figcaption>`` when the editor
provides no instance-specific caption content (neither ``caption_text`` nor
child plugins), mirroring the existing ``default_alt_text`` fallback for ``alt``.
"""

from django.template.loader import get_template
from django.test import SimpleTestCase


class _FakeImage:
    """Stand-in for a django-filer Image (``instance.picture``)."""

    def __init__(self, default_alt_text='', default_caption=''):
        self.default_alt_text = default_alt_text
        self.default_caption = default_caption


class _TruthyEmpty:
    """Truthy container that iterates to nothing.

    Lets the "child plugins are present" branches be exercised without invoking
    the ``{% render_plugin %}`` machinery (which needs full CMS request context).
    The template only checks truthiness of ``child_plugin_instances`` and then
    iterates it; this is truthy yet yields no items, so the loop renders nothing.
    """

    def __bool__(self):
        return True

    def __len__(self):
        return 1

    def __iter__(self):
        return iter(())


class _FakePicture:
    """Stand-in for a djangocms_picture Picture plugin instance."""

    def __init__(self, caption_text='', children=None, default_caption='',
                 default_alt_text='', attributes=None):
        self.caption_text = caption_text
        self.child_plugin_instances = children if children is not None else []
        self.picture = _FakeImage(default_alt_text=default_alt_text,
                                  default_caption=default_caption)
        self.attributes = attributes or {}
        self.attributes_str = ''
        self.link_attributes_str = ''
        self.link_target = ''
        self.img_src = '/media/test.jpg'
        self.width = None
        self.height = None


def _render(instance):
    template = get_template('djangocms_picture/default/picture.html')
    return template.render({
        'instance': instance,
        'picture_link': '',
        'img_srcset_data': [],
    })


class DefaultCaptionFallbackTests(SimpleTestCase):
    def test_default_caption_used_when_no_instance_caption(self):
        """No caption_text and no children -> default_caption renders."""
        html = _render(_FakePicture(default_caption='From the library'))
        self.assertIn('<figure', html)
        self.assertIn('<figcaption>', html)
        self.assertIn('From the library', html)

    def test_caption_text_overrides_default_caption(self):
        """caption_text wins; default_caption is not shown."""
        html = _render(_FakePicture(caption_text='Specific caption',
                                    default_caption='Default caption'))
        self.assertIn('Specific caption', html)
        self.assertNotIn('Default caption', html)

    def test_child_plugins_suppress_default_caption(self):
        """Child plugins are instance-specific content; default is suppressed."""
        html = _render(_FakePicture(default_caption='Default caption',
                                    children=_TruthyEmpty()))
        self.assertIn('<figure', html)
        self.assertNotIn('Default caption', html)

    def test_no_caption_no_default_no_figure(self):
        """Nothing to caption -> no <figure>/<figcaption> (unchanged behavior)."""
        html = _render(_FakePicture())
        self.assertNotIn('<figure', html)
        self.assertNotIn('<figcaption', html)
