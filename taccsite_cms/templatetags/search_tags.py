from django import template
from cms.models import Page
from django.conf import settings
from apps.search_page.utils import get_page_url

register = template.Library()

@register.simple_tag
def search_page_url():
    return get_page_url() or settings.PORTAL_SEARCH_PATH
