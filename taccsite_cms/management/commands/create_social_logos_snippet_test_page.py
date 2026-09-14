"""Create a published CMS page to test logos-social-media.html via Snippet. See commands/README.md."""

import warnings

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from cms.api import add_plugin, create_page, publish_page
from cms.models import CMSPlugin

from djangocms_snippet.cms_plugins import SnippetPlugin
from djangocms_snippet.models import Snippet

from taccsite_cms.management.test_page_util import (
    delete_draft_pages_by_reverse_id,
    ensure_test_parent_page,
)


DEFAULT_REVERSE_ID = 'core_cms_test_page_social_logos'
DEFAULT_TITLE = 'Test Social Logos Snippet'
DEFAULT_SLUG = 'social-logos-snippet-test'
DEFAULT_TEMPLATE = 'standard.html'

SNIPPET_SLUG = 'logos-social-media'
SNIPPET_NAME = 'Logos: Social Media'
SNIPPET_TEMPLATE = 'snippets/logos-social-media.html'
SNIPPET_HTML = '{# SEE: "Template:" field #}'


class Command(BaseCommand):
    help = (
        'Create or update a test page for the logos-social-media snippet template.'
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--replace',
            action='store_true',
            help='Delete existing draft page tree with this reverse_id before creating.',
        )
        parser.add_argument(
            '--language',
            default='en',
            help='CMS language code (default: en).',
        )
        parser.add_argument(
            '--reverse-id',
            default=DEFAULT_REVERSE_ID,
            help=f'Page reverse_id (default: {DEFAULT_REVERSE_ID}).',
        )
        parser.add_argument(
            '--title',
            default=DEFAULT_TITLE,
            help=f'Page title (default: {DEFAULT_TITLE}).',
        )
        parser.add_argument(
            '--slug',
            default=DEFAULT_SLUG,
            help=f'Page slug under /test/ (default: {DEFAULT_SLUG}).',
        )
        parser.add_argument(
            '--template',
            default=DEFAULT_TEMPLATE,
            help=f'Page template (default: {DEFAULT_TEMPLATE}).',
        )
        parser.add_argument(
            '--no-publish',
            action='store_true',
            help='Leave the page as draft.',
        )

    def handle(self, *args, **options):
        language = options['language']
        reverse_id = options['reverse_id']

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

        page = self._get_or_create_page(options, language, publisher, reverse_id)
        self._ensure_snippet_plugin(page, language, snippet)

        if not options['no_publish']:
            with warnings.catch_warnings():
                warnings.simplefilter('ignore', UserWarning)
                publish_page(page, publisher, language)
            self.stdout.write(self.style.SUCCESS('Published.'))
        else:
            self.stdout.write(self.style.WARNING('Left as draft (--no-publish).'))

        url = page.get_absolute_url()
        self.stdout.write(f'Page title: {options["title"]}')
        self.stdout.write(f'URL: {url}')
        self.stdout.write(
            f'Snippet: {snippet.name} ({snippet.template})'
        )

    def _ensure_snippet(self):
        snippet, created = Snippet.objects.get_or_create(
            slug=SNIPPET_SLUG,
            defaults={
                'name': SNIPPET_NAME,
                'html': SNIPPET_HTML,
                'template': SNIPPET_TEMPLATE,
            },
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f'Created snippet {snippet.name!r} → {snippet.template}'
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(f'Using snippet {snippet.name!r}.')
            )
        return snippet

    def _get_or_create_page(self, options, language, publisher, reverse_id):
        from cms.models import Page

        page = Page.objects.drafts().filter(reverse_id=reverse_id).first()
        if page is not None:
            return page

        parent = ensure_test_parent_page(
            language,
            publisher,
            publish=True,
            stdout=self.stdout,
            style=self.style,
        )

        page = create_page(
            title=options['title'],
            template=options['template'],
            language=language,
            slug=options['slug'],
            reverse_id=reverse_id,
            created_by=publisher,
            parent=parent,
            in_navigation=True,
            published=False,
        )

        placeholder = page.placeholders.get(slot='content')
        add_plugin(
            placeholder,
            'TextPlugin',
            language,
            body=(
                '<h1>Social logos snippet test</h1>'
                '<p>This page tests <code>snippets/logos-social-media.html</code> '
                'via a Snippet plugin.</p>'
            ),
        )
        self.stdout.write(self.style.SUCCESS('Created test page.'))
        return page

    def _ensure_snippet_plugin(self, page, language, snippet):
        placeholder = page.placeholders.get(slot='content')
        existing = CMSPlugin.objects.filter(
            placeholder=placeholder,
            language=language,
            plugin_type='SnippetPlugin',
        )
        if existing.exists():
            self.stdout.write('Snippet plugin already on page.')
            return

        add_plugin(
            placeholder,
            SnippetPlugin,
            language,
            snippet=snippet,
        )
        self.stdout.write(self.style.SUCCESS('Added Snippet plugin to page.'))
