from django import template
from cms.models import Page
from django.conf import settings

register = template.Library()

@register.simple_tag
def search_page_url():
    page = Page.objects.filter(reverse_id='search_page').first()

    if page:
        return page.get_absolute_url()
    else:
        return settings.PORTAL_SEARCH_PATH
