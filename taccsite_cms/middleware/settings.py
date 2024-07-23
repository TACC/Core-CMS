from django.conf import settings
from urllib.parse import urlparse
from django.contrib.sites.models import Site

class DynamicSiteIdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # One-time configuration and initialization.
        try:
            current_site = Site.objects.get(domain=request.get_host())
        except Site.DoesNotExist:
            current_site = Site.objects.get(id=settings.DEFAULT_SITE_ID)

        request.current_site = current_site
        settings.SITE_ID = current_site.id

        response = self.get_response(request)
        return response
