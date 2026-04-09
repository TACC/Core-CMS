"""
Create a published CMS page that exercises Style and Bootstrap 4 Container
plugins (including section--accent / o-section--style-accent).

For manual UI checks after Core-Styles or plugin setting changes.
"""

import warnings

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from cms.api import add_plugin, create_page, publish_page
from cms.models import Page

from djangocms_bootstrap4.contrib.bootstrap4_grid.cms_plugins import (
    Bootstrap4GridColumnPlugin,
    Bootstrap4GridContainerPlugin,
    Bootstrap4GridRowPlugin,
)
from djangocms_style.cms_plugins import StylePlugin
from djangocms_text_ckeditor.cms_plugins import TextPlugin


DEFAULT_REVERSE_ID = 'core_cms_section_style_qa'
DEFAULT_TITLE = 'Section / Container style QA'
DEFAULT_SLUG = 'section-style-qa'
DEFAULT_TEMPLATE = 'standard.html'


class Command(BaseCommand):
    help = (
        'Create a published page with Style and Grid Container plugins '
        '(section variants including accent) for visual QA.'
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
            # Only delete the draft: deleting every matching Page row can hit a
            # published sibling whose TreeNode is already gone (django CMS 3).
            removed = 0
            while True:
                draft = Page.objects.drafts().filter(reverse_id=reverse_id).first()
                if not draft:
                    break
                draft.delete()
                removed += 1
            if removed:
                self.stdout.write(
                    self.style.WARNING(
                        f'Removed {removed} draft page tree(s) with reverse_id={reverse_id!r}'
                    )
                )

        page = create_page(
            title=title,
            template=template,
            language=language,
            slug=slug,
            reverse_id=reverse_id,
            created_by=publisher,
            in_navigation=False,
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

        def add_style_section(class_name, heading, blurb, tag_type='section'):
            style = add_plugin(
                placeholder,
                StylePlugin,
                language,
                class_name=class_name,
                tag_type=tag_type,
            )
            add_text(
                style,
                f'<h2>{heading}</h2><p>{blurb}</p>',
            )
            return style

        # Stacked Style plugins (legacy section + o-section accent)
        add_style_section(
            'section--light',
            'Style: section--light',
            'First block; compare spacing and color with Core-Styles section docs.',
        )
        add_style_section(
            'section--accent',
            'Style: section--accent',
            'Accent surface via Style plugin (new in Core-Styles 2.55).',
        )
        add_style_section(
            'o-section o-section--style-accent',
            'Style: o-section--style-accent',
            'Object-section accent variant.',
        )

        # Bootstrap 4 Container + accent section (GRID_CONTAINERS)
        container = add_plugin(
            placeholder,
            Bootstrap4GridContainerPlugin,
            language,
            container_type='container  o-section o-section--style-accent',
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
        )
        add_text(
            column,
            '<h2>Grid: Container + accent section</h2>'
            '<p>Bootstrap Container plugin: '
            'fixed-width container plus <code>o-section--style-accent</code> '
            '(see <code>DJANGOCMS_BOOTSTRAP4_GRID_CONTAINERS</code>).</p>',
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
