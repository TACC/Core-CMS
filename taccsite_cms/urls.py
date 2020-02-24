# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
]

urlpatterns += [
    url(r'^admin/', admin.site.urls),  # NOQA
    url(r'^frontera-top-nav/$', TemplateView.as_view(template_name='top_nav_only.html'), name='top_nav_only'),
    url(r'^api/menu/pages/markup/$', TemplateView.as_view(template_name='menu_only.html'), name='menu_pages_markup'),
    url(r'^', include('cms.urls')),
]

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ]

    urlpatterns += staticfiles_urlpatterns()

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
