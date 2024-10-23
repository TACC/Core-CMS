from django.http import HttpResponse
from django.conf import settings
from django.template import loader


def SearchPageView(request):
    template = loader.get_template('search_page/search_page.html')
    return HttpResponse(template.render({}, request))
