"""
Create a published CMS page that exercises the TACC Site Section plugin.

For manual UI checks after Core-Styles or Section plugin changes.
"""

import warnings

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from cms.api import add_plugin, create_page, publish_page

from djangocms_text_ckeditor.cms_plugins import TextPlugin

from taccsite_section.cms_plugins import TaccsiteSectionPlugin
from taccsite_cms.management.test_page_util import (
    delete_draft_pages_by_reverse_id,
    ensure_test_parent_page,
)


DEFAULT_REVERSE_ID = 'core_cms_test_page_section_style'
DEFAULT_TITLE = 'Test Section Style'
DEFAULT_SLUG = 'test-section-style'
DEFAULT_TEMPLATE = 'standard.html'


class Command(BaseCommand):
    help = (
        'Create a published page with TACC Site Section plugins '
        '(light, muted, accent, and dark section types) for visual QA.'
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

        def add_text(parent, html):
            return add_plugin(
                placeholder,
                TextPlugin,
                language,
                target=parent,
                body=html,
            )

        def add_section(name, section_type, heading, blurb):
            section = add_plugin(
                placeholder,
                TaccsiteSectionPlugin,
                language,
                label=name,
                class_name=section_type,
                tag_type='section',
            )
            add_text(
                section,
                f'<h2>{heading}</h2><p>{blurb}</p>',
            )
            return section

        add_plugin(
            placeholder,
            TextPlugin,
            language,
            body=(
                '<h1>TACC "Section" Plugin</h1>'
                '<p class="h2">Four Section plugins below—one per '
                '<strong>Section type</strong> (Light, Muted, Accent, Dark). '
                'Each uses the default <code>&lt;section&gt;</code> tag.</p>'
            ),
        )

        section_examples = (
            (
                'Light section',
                'o-section o-section--style-light',
                'Light section',
                'Compare padding and background with other types. Classes: '
                '<code>o-section o-section--style-light</code>.',
            ),
            (
                'Muted section',
                'o-section o-section--style-muted',
                'Muted section',
                'Default section type in the editor. Classes: '
                '<code>o-section o-section--style-muted</code>.',
            ),
            (
                'Accent section',
                'o-section o-section--style-accent',
                'Accent section',
                'Brand accent background. Classes: '
                '<code>o-section o-section--style-accent</code>.',
            ),
            (
                'Dark section',
                'o-section o-section--style-dark',
                'Dark section',
                'Dark background and light text. Classes: '
                '<code>o-section o-section--style-dark</code>.',
            ),
        )

        for name, section_type, heading, blurb in section_examples:
            add_section(name, section_type, heading, blurb)

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
