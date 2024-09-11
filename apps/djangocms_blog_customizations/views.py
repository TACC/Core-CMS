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
        remote_url = self.get_remote_url()
        remote_content = self.get_remote_content(remote_url)

        context['markup'] = remote_content

        return context

    def get_remote_url(self):
        path = self.request.path.replace(
            settings.PORTAL_BLOG_REMOTE_CLIENT_PATH,
            ''
        )
        url = (
            settings.PORTAL_BLOG_REMOTE_SOURCE_ROOT
            + path
        )

        return url

    def get_remote_content(self, url):
        response = requests.get(url)

        if response.status_code == 200:
            return response.text
        else:
            return None
