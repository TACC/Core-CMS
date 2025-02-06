"""Change CMS page template at runtime"""
import os

from cms.middleware.toolbar import ToolbarMiddleware
from cms.models.pagemodel import Page as CMS_Page

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

class CMSTemplateOverrideMiddleware(ToolbarMiddleware):
    """
    Use a different CMS template than is set for the current page

    Usage:
        http://0.0.0.0:8000/news/?raw
        http://0.0.0.0:8000/news/?template=raw.html
        Applies `raw.html` template

        http://0.0.0.0:8000/news/?template=fullwidth.html
        Applies `fulwidth.html` template

        http://0.0.0.0:8000/news/?template=misspelling.html
        Raises `TemplateDoesNotExist` error

        http://0.0.0.0:8000/news/?rawng
        http://0.0.0.0:8000/news/?template
        http://0.0.0.0:8000/news/?template=s
        No effect
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            hasattr(request, 'current_page') and
            isinstance(request.current_page, CMS_Page)
        ):
            page = request.current_page
            query_params = request.GET
            query_template = query_params.get('template', '')

            if 'raw' in query_params:
                page.template = os.path.join(TEMPLATE_DIR, 'raw.html')
            if query_template.endswith('.html'):
                page.template = os.path.join(TEMPLATE_DIR, query_template)

        response = self.get_response(request)

        return response
