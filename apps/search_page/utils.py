import logging

from django.conf import settings

from cms.api import create_page
from cms.models.pagemodel import Page

logger = logging.getLogger(f'portal.{__name__}')

TITLE = 'Search'
SLUG = settings.PORTAL_SEARCH_PATH.strip('/')

def create_search_page():
    has_search_page = Page.objects.filter(title_set__slug=SLUG).exists()

    if not has_search_page:
        create_page(
            title=f'{TITLE} (Auto-Generated)',
            menu_title=TITLE,
            page_title=TITLE,
            reverse_id=SLUG,
            # Use a template from CMS_TEMPLATES setting
            template='standard.html',
            language='en',
            published=True,
            slug=SLUG,
            in_navigation=False,
        )
        logger.info(f'Created search page "{TITLE}" at "{SLUG}"')
    else:
        logger.info(f'Found existing search page at "{SLUG}"')
