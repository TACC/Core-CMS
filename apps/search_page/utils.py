import logging

from django.conf import settings
from django.urls import reverse

from cms.api import create_page
from cms.models.pagemodel import Page

from .cms_apps import SearchPageApphook


logger = logging.getLogger(f'portal.{__name__}')

TITLE = 'Search'
DEFAULT_SLUG = settings.PORTAL_SEARCH_PATH.strip('/')

def get_page():
    try:
        return Page.objects.filter(reverse_id='search_page').first()
    except Page.DoesNotExist:
        return None

def get_slug(page=None):
    if page:
        return page.get_slug()
    else:
        page = get_page()
        return get_slug(page) if page else DEFAULT_SLUG

def get_search_page_url():
    try:
        page = Page.objects.get(reverse_id='search_page')
        return page.get_absolute_url()
    except Page.DoesNotExist:
        return reverse('apps.search_page:search')

def create_search_page():
    page = get_page()
    slug = get_slug(page)

    if not page:
        page = create_page(
            title=f'{TITLE} (Auto-Generated)',
            menu_title=TITLE,
            page_title=TITLE,
            reverse_id='search_page',
            # Use a template from CMS_TEMPLATES setting
            template='standard.html',
            language='en',
            published=True,
            slug=slug,
            in_navigation=False,
            apphook=SearchPageApphook,
            apphook_namespace=SearchPageApphook.name,
        )
        logger.info(f'Created search page "{TITLE}" at "{slug}"')
    else:
        logger.info(f'Found existing search page at "{slug}"')

    return page
