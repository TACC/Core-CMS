"""Change site based on domain name (fallback to default site)"""
from django.conf import settings
from django.contrib.sites.models import Site

class DynamicSiteIdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            host = request.get_host()
            site = Site.objects.get(domain=host)
            settings.SITE_ID = site.id
        except Site.DoesNotExist:
            settings.SITE_ID = getattr(settings, 'DEFAULT_SITE_ID', 1)

        response = self.get_response(request)
        return response
