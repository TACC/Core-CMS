import requests

from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def BlogView(request):
    return render(request, 'djangocms_blog/base.html')

def BlogRemoteView(request):
    request = requests.get('https://www.example.com/')
    request.text

    return HttpResponse(Template(request.text).render(Context({})))
