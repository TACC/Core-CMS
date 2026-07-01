"""
Create a published CMS page that exercises the TACC Site Card plugin (c-card).

For manual UI checks after Core-Styles or Card plugin changes.
"""

import warnings

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from cms.api import add_plugin, create_page, publish_page

from djangocms_text_ckeditor.cms_plugins import TextPlugin

from djangocms_bootstrap4.contrib.bootstrap4_grid.cms_plugins import (
    Bootstrap4GridColumnPlugin,
    Bootstrap4GridContainerPlugin,
    Bootstrap4GridRowPlugin,
)
from djangocms_bootstrap4.contrib.bootstrap4_picture.cms_plugins import (
    Bootstrap4PicturePlugin,
)

from taccsite_card.cms_plugins import TaccsiteCardPlugin
from taccsite_cms.management.test_page_util import (
    delete_draft_pages_by_reverse_id,
    ensure_test_parent_page,
)


DEFAULT_REVERSE_ID = 'core_cms_test_page_card_style'
DEFAULT_TITLE = 'Test Card Style'
DEFAULT_SLUG = 'test-card-style'
DEFAULT_TEMPLATE = 'standard.html'

# Sized sample images via URL (no Filer upload). See https://picsum.photos/
def sample_image_url(seed, width=640, height=360):
    return f'https://picsum.photos/seed/{seed}/{width}/{height}'

PICTURE_TEMPLATE = 'no_link_to_ext_image'


class Command(BaseCommand):
    help = (
        'Create a published page with TACC Site Card plugins (c-card variants) '
        'for visual QA.'
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

        def add_picture(card, seed, width=640, height=360):
            return add_plugin(
                placeholder,
                Bootstrap4PicturePlugin,
                language,
                target=card,
                external_picture=sample_image_url(seed, width=width, height=height),
                template=PICTURE_TEMPLATE,
            )

        def add_card(
            class_name,
            card_template,
            heading,
            blurb,
            tag_type='article',
            image_seed=None,
            image_before_text=True,
            image_width=640,
            image_height=360,
            parent=None,
        ):
            card = add_plugin(
                placeholder,
                TaccsiteCardPlugin,
                language,
                target=parent,
                class_name=class_name,
                template=card_template,
                tag_type=tag_type,
            )
            body = f'<h3>{heading}</h3><p>{blurb}</p>'
            if image_seed and image_before_text:
                add_picture(card, image_seed, image_width, image_height)
                add_text(card, body)
            elif image_seed:
                add_text(card, body)
                add_picture(card, image_seed, image_width, image_height)
            else:
                add_text(card, body)
            return card

        def add_responsive_grid():
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
            return row

        def add_responsive_column(row):
            return add_plugin(
                placeholder,
                Bootstrap4GridColumnPlugin,
                language,
                target=row,
                column_type='col',
                column_alignment='',
                xs_col=12,
                md_col=6,
                lg_col=6,
                xl_col=3,
            )

        add_plugin(
            placeholder,
            TextPlugin,
            language,
            body=(
                '<h1>TACC "Card" Plugin</h1>'
                '<p class="h2">Cards automatically have `c-card` class, are skinned via "Card style", and given layout via "Card layout".</p>'
            ),
        )

        skin_row = add_responsive_grid()
        skin_cards = (
            (
                'c-card',
                'default',
                'Card',
                'Expect <code>c-card</code> with no skin modifier.',
            ),
            (
                'c-card--plain',
                'default',
                'Card: Plain',
                'Expect <code>c-card</code> <code>c-card--plain</code>.',
            ),
            (
                'c-card--standard',
                'default',
                'Card: Standard',
                'Expect <code>c-card</code> <code>c-card--standard</code>.',
            ),
        )
        for class_name, card_template, heading, blurb in skin_cards:
            add_card(
                class_name,
                card_template,
                heading,
                blurb,
                parent=add_responsive_column(skin_row),
            )

        image_row = add_responsive_grid()

        # layout, heading, seed, image_before_text, image_width, image_height
        image_layout_cards = (
            ('image_top', 'Image Top', 'core-cms-card-image-top', True, 640, 360),
            ('image_left', 'Image Left', 'core-cms-card-image-left', True, 480, 720),
            ('image_bottom', 'Image Bottom', 'core-cms-card-image-bottom', False, 640, 360),
            ('image_right', 'Image Right', 'core-cms-card-image-right', True, 480, 720),
        )

        for (
            layout_template,
            heading,
            seed,
            image_before_text,
            image_width,
            image_height,
        ) in image_layout_cards:
            add_card(
                'c-card--plain',
                layout_template,
                f'Card: Plain<br><small>{heading}</small>',
                f'Expect <code>c-card</code> <code>c-card--plain</code> '
                f'<code>c-card--{layout_template.replace("_", "-")}</code>.',
                image_seed=seed,
                image_before_text=image_before_text,
                image_width=image_width,
                image_height=image_height,
                parent=add_responsive_column(image_row),
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
