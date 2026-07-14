"""Shared helpers for create_test_page_* management commands."""

import warnings

from cms.api import create_page, publish_page
from cms.models import Page

TEST_PAGE_PARENT_REVERSE_ID = 'core_cms_test_page_parent'
TEST_PAGE_PARENT_TITLE = 'Test'
TEST_PAGE_PARENT_SLUG = 'test'
TEST_PAGE_PARENT_TEMPLATE = 'standard.html'


def delete_draft_pages_by_reverse_id(reverse_id, stdout=None, style=None):
    """Remove draft page trees matching reverse_id (django CMS 3-safe)."""
    removed = 0
    while True:
        draft = Page.objects.drafts().filter(reverse_id=reverse_id).first()
        if not draft:
            break
        draft.delete()
        removed += 1
    if removed and stdout and style:
        stdout.write(
            style.WARNING(
                f'Removed {removed} draft page tree(s) with reverse_id={reverse_id!r}'
            )
        )
    return removed


def ensure_test_parent_page(language, publisher, publish=True, stdout=None, style=None):
    """
    Return the draft Test page at /test/, creating and publishing it if absent.

    create_page(parent=…) requires a draft page with publisher_is_draft=True.
    """
    parent = Page.objects.drafts().filter(reverse_id=TEST_PAGE_PARENT_REVERSE_ID).first()
    if parent is None:
        parent = create_page(
            title=TEST_PAGE_PARENT_TITLE,
            template=TEST_PAGE_PARENT_TEMPLATE,
            language=language,
            slug=TEST_PAGE_PARENT_SLUG,
            reverse_id=TEST_PAGE_PARENT_REVERSE_ID,
            created_by=publisher,
            in_navigation=False,
            published=False,
        )
        if stdout and style:
            stdout.write(
                style.SUCCESS(
                    f'Created parent page /{TEST_PAGE_PARENT_SLUG}/ '
                    f'(reverse_id={TEST_PAGE_PARENT_REVERSE_ID!r}).'
                )
            )
    if publish:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', UserWarning)
            publish_page(parent, publisher, language)
    return parent
