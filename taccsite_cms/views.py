import requests as http_client
from django.conf import settings
from django.contrib.staticfiles import finders
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

_24_HOURS = 86400


@cache_page(_24_HOURS)
def favicon(request):
    portal_favicon = getattr(settings, 'PORTAL_FAVICON', {})
    img_src = portal_favicon.get('img_file_src', '')
    is_remote = portal_favicon.get('is_remote', False)

    if not img_src:
        return HttpResponse(status=404)

    if is_remote:
        try:
            response = http_client.get(img_src, timeout=5)
            return HttpResponse(
                response.content,
                content_type='image/x-icon',
                status=response.status_code,
            )
        except http_client.exceptions.RequestException:
            return HttpResponse(status=502)

    path = finders.find(img_src)
    if not path:
        return HttpResponse(status=404)

    with open(path, 'rb') as f:
        return HttpResponse(f.read(), content_type='image/x-icon')
