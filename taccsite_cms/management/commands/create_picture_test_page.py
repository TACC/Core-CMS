"""
Create a published CMS page that exercises djangocms_picture attribute and
wrapper (link/figure/alignment) combinations.

For manual UI checks after Core-Styles or Picture plugin/template changes.
"""

import warnings

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from cms.api import add_plugin, create_page, publish_page

from djangocms_style.cms_plugins import StylePlugin

from taccsite_cms.management.test_page_util import (
    delete_draft_pages_by_reverse_id,
    ensure_test_parent_page,
)


DEFAULT_REVERSE_ID = 'core_cms_test_page_picture_style'
DEFAULT_TITLE = 'Test Picture Style'
DEFAULT_SLUG = 'test-picture-style'
DEFAULT_TEMPLATE = 'standard.html'

# A reliable externally-hosted placeholder; no local file upload needed.
EXT_IMAGE = 'https://placehold.co/800x400/336699/white.png?text=Test+Image'
LINK_URL = 'https://example.com'
CAPTION = 'Test caption text'

# Each entry: (label, image attributes dict, add link?, add caption?)
# 'alt' in attributes tests the primary bug (alt leaking to parent elements).
# Bootstrap classes in attributes test secondary styling concerns.
CASES = [
    # ── no class ──────────────────────────────────────────────────────────
    ('no class | no link | no figure',       {},                                 False, False),
    ('no class | link',                       {},                                 True,  False),
    ('no class | figure',                     {},                                 False, True),
    ('no class | link + figure',              {},                                 True,  True),

    # ── alt only (primary regression) ─────────────────────────────────────
    ('alt | no link | no figure',             {'alt': 'Image alt text'},          False, False),
    ('alt | link',                            {'alt': 'Image alt text'},          True,  False),
    ('alt | figure',                          {'alt': 'Image alt text'},          False, True),
    ('alt | link + figure',                   {'alt': 'Image alt text'},          True,  True),

    # ── img-fluid ─────────────────────────────────────────────────────────
    ('img-fluid | no link | no figure',       {'class': 'img-fluid',
                                               'alt':   'img-fluid alt'},        False, False),
    ('img-fluid | link',                      {'class': 'img-fluid',
                                               'alt':   'img-fluid alt'},        True,  False),
    ('img-fluid | figure',                    {'class': 'img-fluid',
                                               'alt':   'img-fluid alt'},        False, True),
    ('img-fluid | link + figure',             {'class': 'img-fluid',
                                               'alt':   'img-fluid alt'},        True,  True),

    # ── img-thumbnail ─────────────────────────────────────────────────────
    ('img-thumbnail | no link | no figure',   {'class': 'img-thumbnail',
                                               'alt':   'thumbnail alt'},        False, False),
    ('img-thumbnail | link',                  {'class': 'img-thumbnail',
                                               'alt':   'thumbnail alt'},        True,  False),
    ('img-thumbnail | figure',                {'class': 'img-thumbnail',
                                               'alt':   'thumbnail alt'},        False, True),
    ('img-thumbnail | link + figure',         {'class': 'img-thumbnail',
                                               'alt':   'thumbnail alt'},        True,  True),

    # ── rounded ───────────────────────────────────────────────────────────
    ('rounded | no link | no figure',         {'class': 'rounded',
                                               'alt':   'rounded alt'},          False, False),
    ('rounded | link',                        {'class': 'rounded',
                                               'alt':   'rounded alt'},          True,  False),
    ('rounded | figure',                      {'class': 'rounded',
                                               'alt':   'rounded alt'},          False, True),
    ('rounded | link + figure',               {'class': 'rounded',
                                               'alt':   'rounded alt'},          True,  True),

    # ── align-left / align-right (tests the :has() wrapper-float CSS) ──────
    ('align-left | no link | no figure',      {'class': 'align-left'},           False, False),
    ('align-left | link',                     {'class': 'align-left'},           True,  False),
    ('align-left | figure',                   {'class': 'align-left'},           False, True),

    ('align-right | no link | no figure',     {'class': 'align-right'},          False, False),
    ('align-right | link',                    {'class': 'align-right'},          True,  False),
    ('align-right | figure',                  {'class': 'align-right'},          False, True),

    # ── align-center (tests interaction with display:block on <img>) ───────
    ('align-center | no link | no figure',    {'class': 'align-center'},         False, False),
    ('align-center | link',                   {'class': 'align-center'},         True,  False),
    ('align-center | figure',                 {'class': 'align-center'},         False, True),

    # ── combined: img-fluid + align-* ───────────────────────────────────────
    ('img-fluid align-left | link',           {'class': 'img-fluid align-left',
                                               'alt':   'fluid left alt'},        True,  False),
    ('img-fluid align-left | figure',         {'class': 'img-fluid align-left',
                                               'alt':   'fluid left alt'},        False, True),

    ('img-fluid align-right | link',          {'class': 'img-fluid align-right',
                                               'alt':   'fluid right alt'},       True,  False),
    ('img-fluid align-right | figure',        {'class': 'img-fluid align-right',
                                               'alt':   'fluid right alt'},       False, True),

    ('img-fluid align-center | link',         {'class': 'img-fluid align-center',
                                               'alt':   'fluid centered alt'},   True,  False),
    ('img-fluid align-center | figure',       {'class': 'img-fluid align-center',
                                               'alt':   'fluid centered alt'},   False, True),
]


class Command(BaseCommand):
    help = (
        'Create a published page with djangocms_picture attribute/wrapper '
        'combinations (link, figure, alignment) for visual QA.'
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--title',
            default=DEFAULT_TITLE,
            help=f'Default: {DEFAULT_TITLE!r}',
        )
        parser.add_argument(
            '--slug',
            default=DEFAULT_SLUG,
            help=f'Default: {DEFAULT_SLUG!r}',
        )
        parser.add_argument(
            '--reverse-id',
            dest='reverse_id',
            default=DEFAULT_REVERSE_ID,
            help=f'Default: {DEFAULT_REVERSE_ID!r} (used with --replace)',
        )
        parser.add_argument(
            '--language',
            default=settings.LANGUAGE_CODE,
            help='Page language (default: LANGUAGE_CODE)',
        )
        parser.add_argument(
            '--template',
            default=DEFAULT_TEMPLATE,
            help=f'CMS template key (default: {DEFAULT_TEMPLATE!r})',
        )
        parser.add_argument(
            '--replace',
            action='store_true',
            help='Delete any existing page with the same reverse_id first',
        )
        parser.add_argument(
            '--no-publish',
            action='store_true',
            help='Leave the page as draft (plugins are still created)',
        )

    def handle(self, *args, **options):
        language = options['language']
        reverse_id = options['reverse_id']
        title = options['title']
        slug = options['slug']
        template = options['template']

        User = get_user_model()
        publisher = User.objects.filter(is_superuser=True).first()
        if not publisher:
            raise CommandError(
                'No superuser found; create one or publish the draft manually.'
            )

        if options['replace']:
            delete_draft_pages_by_reverse_id(
                reverse_id,
                stdout=self.stdout,
                style=self.style,
            )

        parent = ensure_test_parent_page(
            language,
            publisher,
            publish=True,
            stdout=self.stdout,
            style=self.style,
        )

        page = create_page(
            title=title,
            template=template,
            language=language,
            slug=slug,
            reverse_id=reverse_id,
            created_by=publisher,
            parent=parent,
            in_navigation=True,
            published=False,
        )

        placeholder = page.placeholders.get(slot='content')

        add_plugin(
            placeholder, 'TextPlugin', language,
            body=(
                '<h1>Picture Plugin Test: Alt &amp; Class on Parent Elements</h1>'
                '<p>Each section below tests one combination of Bootstrap class, '
                'alt attribute, and wrapper (link / figure). '
                'Inspect the DOM and verify:</p>'
                '<ul>'
                '<li><code>&lt;img&gt;</code> has the expected <code>class</code> and <code>alt</code>.</li>'
                '<li><code>&lt;a&gt;</code> does <strong>not</strong> have <code>class</code> nor <code>alt</code> from the image.</li>'
                '<li><code>&lt;figure&gt;</code> does <strong>not</strong> have <code>class</code> nor <code>alt</code> from the image.</li>'
                '<li>Bootstrap styles (border, border-radius, max-width) render correctly on the image itself.</li>'
                '<li>For align-left/align-right/align-center cases, the whole wrapper (not just the image) floats or centers, without double-floating.</li>'
                '</ul>'
            ),
        )

        for i, (label, attrs, has_link, has_caption) in enumerate(CASES):
            self._add_case(placeholder, language, i, label, attrs, has_link, has_caption)

        if not options['no_publish']:
            with warnings.catch_warnings():
                warnings.simplefilter('ignore', UserWarning)
                page = publish_page(page, publisher, language)
            self.stdout.write(self.style.SUCCESS('Published.'))
        else:
            self.stdout.write(self.style.WARNING('Left as draft (--no-publish).'))

        url = page.get_absolute_url()
        self.stdout.write(f'Page title: {title}')
        self.stdout.write(f'URL: {url}')
        self.stdout.write(
            '\nDebug overlay (labels each element): open the page and run in '
            'the browser console —\n\n'
            "  let l = document.createElement('link');\n"
            "  l.rel = 'stylesheet';\n"
            "  l.href = 'https://cdn.jsdelivr.net/gh/TACC/Core-CMS@5a42643b"
            "/taccsite_cms/static/site_cms/css/test/djangocms-picture.css';\n"
            "  document.head.appendChild(l);\n"
            '\n(Ships with v4.36 / PR #968; not present before that.)\n'
        )

    def _add_case(self, placeholder, language, index, label, attrs, has_link, has_caption):
        attrs_display = ', '.join(f'{k}="{v}"' for k, v in attrs.items()) or '(none)'
        wrapper = []
        if has_link:
            wrapper.append('link')
        if has_caption:
            wrapper.append('figure/caption')
        wrapper_display = ' + '.join(wrapper) if wrapper else 'no wrapper'

        section_class = 'o-section o-section--light' if index % 2 == 0 else 'o-section o-section--muted'
        section = add_plugin(
            placeholder, StylePlugin, language,
            class_name=section_class,
            tag_type='section',
        )

        add_plugin(
            placeholder, 'TextPlugin', language,
            target=section,
            body=(
                f'<h2>{label}</h2>'
                f'<p>Attributes: <code>{attrs_display}</code> &nbsp;|&nbsp; '
                f'Wrapper: <code>{wrapper_display}</code></p>'
            ),
        )
        # Use default template for linked cases: its picture_link_end block
        # correctly closes </a> when picture_link is truthy.
        # Use no_link_to_ext_image only when there is no link, to suppress
        # the external_picture URL from auto-becoming the href.
        # (Combining link_url + no_link_to_ext_image leaves <a> unclosed
        # because that template's picture_link_end is unconditionally empty.)
        picture_template = 'default' if has_link else 'no_link_to_ext_image'
        add_plugin(
            placeholder, 'PicturePlugin', language,
            target=section,
            external_picture=EXT_IMAGE,
            template=picture_template,
            attributes=attrs,
            link_url=LINK_URL if has_link else '',
            link_target='_blank' if has_link else '',
            caption_text=CAPTION if has_caption else '',
        )
