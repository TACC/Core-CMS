import requests

from django.conf import settings
from django.http import request
from django.template import Template, Context
from django.shortcuts import render
from django.views.generic.base import TemplateView

def BlogView(request):
    return render(request, 'djangocms_blog/base.html')

class BlogRemoteView(TemplateView):
    template_name = 'djangocms_blog_customizations/remote.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        remote_page = requests.get(settings.PORTAL_BLOG_REMOTE_URL)

        context['markup'] = remote_page.text

        return context
