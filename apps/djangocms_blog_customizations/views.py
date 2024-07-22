import requests

from django.conf import settings
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def BlogView(request):
    return render(request, 'djangocms_blog/base.html')

def BlogRemoteView(request):
    request = requests.get(settings.PORTAL_BLOG_REMOTE_URL)
    request.text

    return HttpResponse(Template(request.text).render(Context({})))
