from django import template
from cms.models import Page
from django.conf import settings

register = template.Library()

@register.simple_tag
def search_page_url():
    try:
        page = Page.objects.filter(reverse_id='search_page').first()
        if page:
            return page.get_absolute_url()
        else:
            return settings.PORTAL_SEARCH_PATH
    except Exception as e:
        # Log the error if needed
        print('Error with tag "search_page_url":', e)
        # To fallback to a default URL if the apphook isn't active
        return settings.PORTAL_SEARCH_PATH
