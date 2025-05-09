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
        source_page = self.kwargs.get('page', '')

        root_parts = urllib.parse.urlsplit(source_root)
        page_parts = urllib.parse.urlsplit(source_page)

        # Get query string from request (as-is, all params should be passed through)
        query = self.request.GET.urlencode() if self.request.GET else None
        logger.debug(f"Query string: {query}")

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

    # CAVEAT: Causes a view request for every resource (img/script/stylesheet)
    def get_client_markup(self, source_markup):
        if not source_markup:
            logger.error(f"Failed to fetch source markup from {source_site}")
            return None

        client_markup = None

        source = urlparse(settings.PORTAL_REMOTE_CONTENT_SOURCE_ROOT)
        source_site = source.scheme + '://' + source.netloc
        client_path = '/' + settings.PORTAL_REMOTE_CONTENT_CLIENT_PATH.strip('/') + '/'

        # Resource URLs
        client_markup = source_markup.replace(
            'src="/',
            'crossorigin="anonymous" src="' + source_site + '/'
        )

        # Absolute URLs
        client_markup = client_markup.replace(
            'href="/',
            f'href="{client_path}'
        )

        # Parameters specific to Django-CMS
        cms_params = {
            k: v for k, v in self.request.GET.items()
            if k in ['template', 'language', 'edit', 'edit_off', 'structure', 'toolbar_off']
        }

        # Preserve parameters
        if cms_params:
            def replace_url(match):
                # Extract URL between quotes, including the quotes
                full_attr = match.group(0)  # e.g. href="?page=3"
                quote_char = full_attr[5]  # Get the type of quote used (" or ')
                url = full_attr[6:-1]  # Get URL without quotes and href=

                if url.startswith('?'):
                    # Parse the query parameters
                    query_params = dict(parse_qsl(url[1:]))  # Skip the ? at start
                    # Add CMS params
                    query_params.update(cms_params)
                    # Rebuild the URL with updated parameters
                    new_url = f'href={quote_char}?{urlencode(query_params)}{quote_char}'
                    return new_url
                return full_attr

            # Replace relative URLs that start with ?, matching the quotes correctly
            import re
            pattern = r'href=[\'"]\?[^\'\"]*[\'"]'  # Handles both single and double quotes
            client_markup = re.sub(pattern, replace_url, client_markup)

        return client_markup
