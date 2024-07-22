from django.shortcuts import render


def BlogView(request):
    return render(request, 'djangocms_blog/base.html')
