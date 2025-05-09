from django.conf import settings
from django.contrib.sites.models import Site

class DynamicSiteMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Include port since dev server uses :8000
        host = request.get_host()

        try:
            # Try to find site matching the exact host with port
            site = Site.objects.get(domain=host)
            settings.SITE_ID = site.id
        except Site.DoesNotExist:
            # Fallback to default site id
            settings.SITE_ID = 1

        response = self.get_response(request)
        return response
