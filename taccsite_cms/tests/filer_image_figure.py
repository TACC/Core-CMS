"""Tests for shared filer image figure/alt partials (Picture plugin and blog main image)."""

from django.template import Context, Template
from django.test import SimpleTestCase


class _FakeImage:
    def __init__(self, default_alt_text='', default_caption=''):
        self.default_alt_text = default_alt_text
        self.default_caption = default_caption


class _TruthyEmpty:
    def __bool__(self):
        return True

    def __iter__(self):
        return iter(())


def _render_blog_visual(image):
    template = Template(
        '{% include "includes/filer_image/figure_open.html" '
        'with image=image wrapper_class="blog-visual" figure_class="blog-visual" %}'
        '<img alt="{% include "includes/filer_image/img_alt.html" with image=image %}">'
        '{% include "includes/filer_image/figure_close.html" with image=image %}'
    )
    return template.render(Context({'image': image}))


class FilerImageFigureTests(SimpleTestCase):
    def test_default_caption_renders_figure_and_figcaption(self):
        html = _render_blog_visual(_FakeImage(default_caption='Library caption'))
        self.assertIn('<figure class="blog-visual">', html)
        self.assertIn('<figcaption>', html)
        self.assertIn('Library caption', html)
        self.assertNotIn('<div class="blog-visual">', html)

    def test_no_caption_renders_div_wrapper_not_figure(self):
        html = _render_blog_visual(_FakeImage())
        self.assertIn('<div class="blog-visual">', html)
        self.assertNotIn('<figure', html)
        self.assertNotIn('<figcaption', html)

    def test_default_alt_on_img(self):
        html = _render_blog_visual(_FakeImage(default_alt_text='Describe the scene'))
        self.assertIn('alt="Describe the scene"', html)

    def test_empty_alt_when_no_default(self):
        html = _render_blog_visual(_FakeImage())
        self.assertIn('alt=""', html)
