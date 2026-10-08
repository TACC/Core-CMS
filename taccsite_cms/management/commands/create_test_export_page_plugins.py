"""
Create a published CMS page with one instance of each plugin type used for DOCX export QA.

See docs/export-page.md and Core-CMS-Plugin-Export-Page docs/plugin-support.md.
"""

import warnings

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from cms.api import add_plugin, create_page, publish_page
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap4.contrib.bootstrap4_grid.cms_plugins import (
    Bootstrap4GridColumnPlugin,
    Bootstrap4GridContainerPlugin,
    Bootstrap4GridRowPlugin,
)
from djangocms_snippet.cms_plugins import SnippetPlugin
from djangocms_snippet.models import Snippet
from djangocms_style.cms_plugins import StylePlugin
from djangocms_text_ckeditor.cms_plugins import TextPlugin

from taccsite_card.cms_plugins import TaccsiteCardPlugin
from taccsite_cms.djangocms_bootstrap4.contrib.bootstrap4_alerts.appearance import (
    ALERT_APPEARANCE_BOOTSTRAP,
    appearance_attributes,
)
from taccsite_cms.management.test_page_util import (
    delete_draft_pages_by_reverse_id,
    ensure_test_parent_page,
)
from taccsite_section.cms_plugins import TaccsiteSectionPlugin

Bootstrap4LinkPlugin = plugin_pool.plugins['Bootstrap4LinkPlugin']
Bootstrap4AlertsPlugin = plugin_pool.get_plugin('Bootstrap4AlertsPlugin')

DEFAULT_REVERSE_ID = 'core_cms_test_export_page_plugins'
DEFAULT_TITLE = 'Test Export Page Plugins'
DEFAULT_SLUG = 'test-export-page'
DEFAULT_TEMPLATE = 'standard.html'

EXPORT_SNIPPET_SLUG = 'export-page-test'
EXPORT_SNIPPET_NAME = 'Export page test snippet'
EXPORT_SNIPPET_HTML = (
    '<h2>Snippet heading</h2>'
    '<p>Snippet body with <strong>bold</strong> and '
    '<a href="https://example.com/snippet">snippet link</a>.</p>'
)


class Command(BaseCommand):
    help = (
        'Create a page under /test/ with one of each plugin type relevant to '
        'export page (Text, Snippet, Link, Style, Grid, Alert, Section, Card).'
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

        snippet = self._ensure_snippet()

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
        self._build_plugins(placeholder, language, snippet)

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
        self.stdout.write(f'Snippet: {snippet.name} (slug={snippet.slug})')

    def _ensure_snippet(self):
        snippet, created = Snippet.objects.get_or_create(
            slug=EXPORT_SNIPPET_SLUG,
            defaults={
                'name': EXPORT_SNIPPET_NAME,
                'html': EXPORT_SNIPPET_HTML,
            },
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Created snippet {snippet.name!r}.')
            )
        else:
            self.stdout.write(self.style.SUCCESS(f'Using snippet {snippet.name!r}.'))
        return snippet

    def _build_plugins(self, placeholder, language, snippet):
        def add_text(parent, body):
            return add_plugin(
                placeholder,
                TextPlugin,
                language,
                target=parent,
                body=body,
            )

        add_plugin(
            placeholder,
            TextPlugin,
            language,
            body=(
                '<h1>Page export plugin matrix</h1>'
                '<p>One instance per supported export reader. Download as DOCX '
                'and compare to this page.</p>'
            ),
        )

        add_plugin(
            placeholder,
            TextPlugin,
            language,
            body=(
                '<h2>Text</h2>'
                '<p><strong>Bold lead-in.</strong> Plain text with '
                '<code>inline code</code> and '
                '<a href="https://example.com/text">text link</a>.</p>'
                '<ul><li>Bullet one</li><li>Bullet two</li></ul>'
            ),
        )

        add_plugin(
            placeholder,
            SnippetPlugin,
            language,
            snippet=snippet,
        )

        add_plugin(
            placeholder,
            Bootstrap4LinkPlugin,
            language,
            name='Export test button',
            link_type='btn',
            link_context='primary',
            external_link='https://example.com/button',
        )

        style = add_plugin(
            placeholder,
            StylePlugin,
            language,
            label='EDITOR-ONLY Style name (must not export)',
            class_name='',
            tag_type='div',
        )
        add_text(
            style,
            '<h2>Style wrapper</h2><p>Content inside generic Style plugin.</p>',
        )

        container = add_plugin(
            placeholder,
            Bootstrap4GridContainerPlugin,
            language,
            container_type='container',
        )
        row = add_plugin(
            placeholder,
            Bootstrap4GridRowPlugin,
            language,
            target=container,
            vertical_alignment='',
            horizontal_alignment='',
        )
        column = add_plugin(
            placeholder,
            Bootstrap4GridColumnPlugin,
            language,
            target=row,
            column_type='col',
            column_alignment='',
            xs_col=12,
            md_col=6,
        )
        add_text(
            column,
            '<h2>Grid column</h2><p>Text inside container → row → column.</p>',
        )

        alert = add_plugin(
            placeholder,
            Bootstrap4AlertsPlugin,
            language,
            alert_context='primary',
            attributes=appearance_attributes(ALERT_APPEARANCE_BOOTSTRAP),
        )
        add_text(
            alert,
            '<strong>Primary alert.</strong> '
            '<a href="https://example.com/alert">Alert link</a>.',
        )

        section = add_plugin(
            placeholder,
            TaccsiteSectionPlugin,
            language,
            label='EDITOR-ONLY Section name (must not export)',
            class_name='o-section o-section--style-muted',
            tag_type='section',
        )
        add_text(
            section,
            '<h2>TACC Site Section</h2><p>Visible section body copy.</p>',
        )

        card = add_plugin(
            placeholder,
            TaccsiteCardPlugin,
            language,
            class_name='c-card',
            template='default',
            tag_type='article',
        )
        add_text(
            card,
            '<h3>Card title</h3><p>Card body for export.</p>',
        )
        add_plugin(
            placeholder,
            Bootstrap4LinkPlugin,
            language,
            target=card,
            name='Card CTA',
            link_type='btn',
            link_context='secondary',
            external_link='https://example.com/card',
        )
