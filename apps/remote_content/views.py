import logging
import requests
from urllib.parse import urlparse, urlencode, parse_qsl
import urllib.parse

from django.conf import settings
from django.views.generic.base import TemplateView

from bs4 import BeautifulSoup

logger = logging.getLogger(f"portal.{__name__}")

class RemoteMarkup(TemplateView):
    template_name = 'remote_content/markup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        source_url = self.build_source_url()
        source_markup = self.get_source_markup(source_url)
        client_markup = self.build_client_markup(source_markup)

        context['markup'] = client_markup

        return context

    def build_source_url(self):
        source_root = settings.PORTAL_REMOTE_CONTENT_SOURCE_ROOT
        source_page = self.kwargs.get('page', '')

        root_parts = urllib.parse.urlsplit(source_root)
        page_parts = urllib.parse.urlsplit(source_page)

        query = self.request.GET.urlencode() if self.request.GET else None

        url_parts = urllib.parse.ParseResult(
            scheme=root_parts.scheme,
            netloc=root_parts.netloc,
            path=root_parts.path + page_parts.path,
            params=None,
            query=query,
            fragment=page_parts.fragment
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

    def build_client_markup(self, source_markup):
        if not source_markup:
            logger.error(f"Failed to fetch source markup")
            return None

        source = urlparse(settings.PORTAL_REMOTE_CONTENT_SOURCE_ROOT)
        source_site = source.scheme + '://' + source.netloc
        client_path = '/' + settings.PORTAL_REMOTE_CONTENT_CLIENT_PATH.strip('/') + '/'

        soup = BeautifulSoup(source_markup, 'html.parser')

        # Handle resource URLs (src attributes)
        for tag in soup.find_all(src=True):
            if tag['src'].startswith('/'):
                tag['crossorigin'] = 'anonymous'
                tag['src'] = source_site + tag['src']

        # Handle absolute URLs (href attributes)
        for tag in soup.find_all(href=True):
            if tag['href'].startswith('/'):
                tag['href'] = client_path + tag['href'].lstrip('/')

        # Parameters specific to Django-CMS
        cms_params = {
            k: v for k, v in self.request.GET.items()
            if k in ['template', 'language', 'edit', 'edit_off', 'structure', 'toolbar_off']
        }

        # Preserve parameters for relative URLs that start with ?
        if cms_params:
            for tag in soup.find_all(href=True):
                if tag['href'].startswith('?'):
                    query_params = dict(parse_qsl(tag['href'][1:]))
                    query_params.update(cms_params)
                    tag['href'] = '?' + urlencode(query_params)

        return str(soup)
