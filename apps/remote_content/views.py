import logging
import requests

from urllib.parse import urlparse, urlencode, parse_qsl
import urllib.parse

from django.conf import settings
from django.template import Template, Context
from django.shortcuts import render
from django.views.generic.base import TemplateView

logger = logging.getLogger(f"portal.{__name__}")

class RemoteMarkup(TemplateView):
    template_name = 'remote_content/markup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        source_url = self.build_source_url()
        source_markup = self.get_source_markup(source_url)
        client_markup = self.get_client_markup(source_markup)

        context['markup'] = client_markup

        return context

    def build_source_url(self):
        source_root = settings.PORTAL_REMOTE_CONTENT_SOURCE_ROOT
        source_page = self.request.GET.get('page', '')

        decoded_page = urllib.parse.unquote(source_page)
        page_parts = urllib.parse.urlsplit(decoded_page)
        root_parts = urllib.parse.urlsplit(source_root)

        url_parts = urllib.parse.ParseResult(
            scheme=root_parts.scheme,
            netloc=root_parts.netloc,
            path=root_parts.path + page_parts.path.lstrip('/'),
            params=None,
            query=page_parts.query,
            fragment=None
        )

        source_url = urllib.parse.urlunparse(url_parts)
        logger.debug(f"Attempting to fetch: {source_url}")
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
