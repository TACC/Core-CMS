"""
Management command to build a test page covering all djangocms_picture
wrapper/attribute combinations relevant to PR #1127 (fix: alt on parent
elements).

Usage:
    docker exec core_cms python manage.py create_picture_test_page
    docker exec core_cms python manage.py create_picture_test_page --delete

Options:
    --delete    Remove the test page instead of creating it.

What to check after running:
    1.  Open http://localhost:8000/picture-test/ and inspect the DOM.
    2.  For every picture, verify:
        - <img> has the expected class and alt (if set).
        - <a> does NOT have class nor alt from the image's attributes.
        - <figure> does NOT have class nor alt from the image's attributes.
    3.  Visually verify that Bootstrap classes (img-fluid, img-thumbnail,
        rounded) look correct on the image itself in each wrapper context.

Debug overlay:
    To see which element is which, add a snippet (via CMS "Snippet" plugin or
    browser console) containing:
        <link rel="stylesheet"
              href="https://cdn.jsdelivr.net/gh/TACC/Core-CMS@5a42643b/taccsite_cms/static/site_cms/css/test/djangocms-picture.css">
    (This file ships with v4.36 / PR #968 and is not present before that.)
"""

from django.core.management.base import BaseCommand
from cms.api import create_page, add_plugin, publish_page
from cms.models import Page


LANG = 'en'
PAGE_TITLE = 'Picture Test: PR-1126 Alt Fix'
PAGE_SLUG = 'picture-test'

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

    # ── align-center (tests interaction with display:block on <img>) ───────
    ('align-center | no link | no figure',    {'class': 'align-center'},         False, False),
    ('align-center | link',                   {'class': 'align-center'},         True,  False),
    ('align-center | figure',                 {'class': 'align-center'},         False, True),

    # ── combined: img-fluid + align-center ────────────────────────────────
    ('img-fluid align-center | link',         {'class': 'img-fluid align-center',
                                               'alt':   'fluid centered alt'},   True,  False),
    ('img-fluid align-center | figure',       {'class': 'img-fluid align-center',
                                               'alt':   'fluid centered alt'},   False, True),
]


class Command(BaseCommand):
    help = 'Create (or delete) a test page for djangocms_picture attribute handling.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete the test page instead of creating it.',
        )

    def handle(self, *args, **options):
        if options['delete']:
            self._delete_page()
        else:
            self._create_page()

    # ── helpers ──────────────────────────────────────────────────────────

    def _delete_page(self):
        deleted = Page.objects.filter(title_set__slug=PAGE_SLUG).delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted: {deleted}'))

    def _create_page(self):
        # Reuse if the page already exists so the command is idempotent.
        existing = Page.objects.filter(title_set__slug=PAGE_SLUG).first()
        if existing:
            existing.delete()
            self.stdout.write('Deleted previous test page.')

        page = create_page(
            title=PAGE_TITLE,
            template='standard.html',
            language=LANG,
            slug=PAGE_SLUG,
            published=False,
        )
        placeholder = page.placeholders.get(slot='content')

        # Intro heading + instructions
        add_plugin(
            placeholder, 'TextPlugin', LANG,
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
                '</ul>'
            ),
        )

        for label, attrs, has_link, has_caption in CASES:
            self._add_case(placeholder, label, attrs, has_link, has_caption)

        publish_page(page, self._get_superuser(), LANG)

        url = f'http://localhost:8000/{PAGE_SLUG}/'
        self.stdout.write(self.style.SUCCESS(
            f'\nTest page created and published: {url}\n'
        ))
        self.stdout.write(
            'To enable the debug overlay that labels each element, open the\n'
            'page in a browser and run this in the console:\n\n'
            "  let l = document.createElement('link');\n"
            "  l.rel = 'stylesheet';\n"
            "  l.href = 'https://cdn.jsdelivr.net/gh/TACC/Core-CMS@5a42643b"
            "/taccsite_cms/static/site_cms/css/test/djangocms-picture.css';\n"
            "  document.head.appendChild(l);\n"
            '\n(This file ships with v4.36 / PR #968 and is not present before that.)\n'
        )

    def _add_case(self, placeholder, label, attrs, has_link, has_caption):
        attrs_display = ', '.join(f'{k}="{v}"' for k, v in attrs.items()) or '(none)'
        wrapper = []
        if has_link:
            wrapper.append('link')
        if has_caption:
            wrapper.append('figure/caption')
        wrapper_display = ' + '.join(wrapper) if wrapper else 'no wrapper'

        add_plugin(
            placeholder, 'TextPlugin', LANG,
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
        template = 'default' if has_link else 'no_link_to_ext_image'
        add_plugin(
            placeholder, 'PicturePlugin', LANG,
            external_picture=EXT_IMAGE,
            template=template,
            attributes=attrs,
            link_url=LINK_URL if has_link else '',
            link_target='_blank' if has_link else '',
            caption_text=CAPTION if has_caption else '',
        )

    def _get_superuser(self):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        return User.objects.filter(is_superuser=True).first()
