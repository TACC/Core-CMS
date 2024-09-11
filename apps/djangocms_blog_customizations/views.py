import requests

from django.conf import settings
from django.template import Template, Context
from django.shortcuts import render
from django.views.generic.base import TemplateView

def BlogView(request):
    return render(request, 'djangocms_blog/base.html')

class BlogRemoteView(TemplateView):
    template_name = 'djangocms_blog_customizations/remote.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        source_url = self.get_source_url()
        source_markup = self.get_source_markup(source_url)
        client_markup = self.get_client_markup(source_markup)

        context['markup'] = client_markup

        return context

    def get_source_url(self):
        client_path = settings.PORTAL_BLOG_REMOTE_CLIENT_PATH
        source_host = settings.PORTAL_BLOG_REMOTE_SOURCE_ROOT
        source_path = self.request.path.replace(client_path, '')

        return source_host + source_path

    def get_source_markup(self, url):
        response = requests.get(url)

        if response.status_code == 200:
            return response.text
        else:
            return None

    # CAVEAT: Causes request to PORTAL_BLOG_REMOTE_CLIENT_PATH for every 'href'
    def get_client_markup(self, source_markup):
        client_path_prefix = settings.PORTAL_BLOG_REMOTE_CLIENT_PATH

        # FAQ: No markup for bad URL or a resource specific to source wesbite
        if source_markup:
            return source_markup.replace('href="', 'href="' + client_path_prefix)
        else:
            return None
