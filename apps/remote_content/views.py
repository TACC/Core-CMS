import requests

from urllib.parse import urlparse, urlencode, parse_qsl

from django.conf import settings
from django.template import Template, Context
from django.shortcuts import render
from django.views.generic.base import TemplateView

class RemoteMarkup(TemplateView):
    template_name = 'remote_content/markup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        source_url = self.get_source_url()
        source_markup = self.get_source_markup(source_url)
        client_markup = self.get_client_markup(source_markup)

        context['markup'] = client_markup

        return context

    def get_source_url(self):
        source_root = settings.PORTAL_REMOTE_CONTENT_SOURCE_ROOT
        client = urlparse(self.request.build_absolute_uri())
        source = urlparse(source_root)

        client_path = settings.PORTAL_REMOTE_CONTENT_CLIENT_PATH
        source_path = source.path + client.path.replace(client_path, '')

        source_url = client._replace(
            scheme=source.scheme,
            netloc=source.netloc,
            path=source_path,
        ).geturl()
        source_url = add_query_params(source_url, {'raw':''})

        return source_url

    def get_source_markup(self, url):
        response = requests.get(url)

        if response.status_code == 200:
            return response.text
        else:
            return None

    # CAVEAT: Causes a view request for every resource (img/script/stylesheet)
    def get_client_markup(self, source_markup):
        client_markup = None

        source = urlparse(settings.PORTAL_REMOTE_CONTENT_SOURCE_ROOT)
        source_site = source.scheme + '://' + source.netloc

        # FAQ: No markup for bad URL or a resource specific to source wesbite
        if source_markup:
            client_markup = source_markup.replace(
                'src="',
                'crossorigin="anonymous" src="' + source_site
            ).replace(
                'href="' + source.path,
                'target="_blank" href="' + source_site + source.path
            )

        return client_markup

def add_query_params(url, params):
    request = requests.PreparedRequest()

    request.prepare_url(url, params)

    return request.url
