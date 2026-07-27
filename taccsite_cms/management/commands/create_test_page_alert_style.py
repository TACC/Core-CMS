"""
Create a published CMS page that exercises Bootstrap 4 Alert plugin contexts.

For manual UI checks after Core-Styles or alert plugin setting changes.
"""

import warnings

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from cms.api import add_plugin, create_page, publish_page

from djangocms_bootstrap4.contrib.bootstrap4_alerts.cms_plugins import (
    Bootstrap4AlertsPlugin,
)
from djangocms_text_ckeditor.cms_plugins import TextPlugin

from taccsite_cms.management.test_page_util import (
    delete_draft_pages_by_reverse_id,
    ensure_test_parent_page,
)


DEFAULT_REVERSE_ID = 'core_cms_test_page_alert_style'
DEFAULT_TITLE = 'Test Alert Style'
DEFAULT_SLUG = 'test-alert-style'
DEFAULT_TEMPLATE = 'standard.html'

CONTEXTS = [
    'primary',
    'secondary',
    'success',
    'danger',
    'warning',
    'info',
    'light',
    'dark',
]


class Command(BaseCommand):
    help = (
        'Create a published page with Bootstrap 4 Alert plugins '
        '(all context variants) for visual QA.'
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

        for context in CONTEXTS:
            alert = add_plugin(
                placeholder,
                Bootstrap4AlertsPlugin,
                language,
                alert_context=context,
            )
            add_plugin(
                placeholder,
                TextPlugin,
                language,
                target=alert,
                body=f'<strong>{context.capitalize()} alert.</strong> '
                     f'This is a <code>alert-{context}</code> Bootstrap 4 alert. '
                     f'<a href="#" class="alert-link">Example link</a>.',
            )

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
