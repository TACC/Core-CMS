import logging

from django.conf import settings
from django.urls import reverse, NoReverseMatch

from cms.api import create_page
from cms.models.pagemodel import Page

from .cms_apps import SearchPageApphook


logger = logging.getLogger(f'portal.{__name__}')

TITLE = 'Search'
REVERSE_ID = 'search_page'
DEFAULT_SLUG = settings.PORTAL_SEARCH_PATH.strip('/')

def get_page():
    try:
        return Page.objects.filter(reverse_id=REVERSE_ID).first()
    except Page.DoesNotExist:
        return None

def get_slug(page=None):
    if page:
        return page.get_slug()
    else:
        page = get_page()
        return get_slug(page) if page else DEFAULT_SLUG

def get_page_url():
    page = get_page()
    if page:
        return page.get_absolute_url()
    else:
        try:
            return reverse('apps.search_page:search')
        except NoReverseMatch:
            return None

def create_search_page():
    page = get_page()
    slug = get_slug(page)

    if not page:
        page = create_page(
            title=f'{TITLE} (Auto-Generated)',
            menu_title=TITLE,
            page_title=TITLE,
            reverse_id=REVERSE_ID,
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
