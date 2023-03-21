# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.views.generic.base import TemplateView
from taccsite_cms import remote_cms_auth as remote_cms_auth

from django.http import request
from django.views.generic.base import RedirectView
admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),

    url(r'^admin/', admin.site.urls),  # NOQA
    url(r'^cms/logout/', views.LogoutView.as_view(), name='logout'),

    url(r'^', include('djangocms_forms.urls')),
]

if getattr(settings, 'INCLUDES_CORE_PORTAL', True):
    urlpatterns += [
        # To allow direct access to markup for Portal and User Guide to render
        url(r'^cms/nav/search/markup/$', TemplateView.as_view(template_name='nav_search.raw.html'), name='search_bar_markup'),
        url(r'^cms/nav/pages/markup/$', TemplateView.as_view(template_name='nav_cms.raw.html'), name='menu_pages_markup'),
        url(r'^cms/header/branding/markup/$', TemplateView.as_view(template_name='header_branding.html'), name='header_branding_markup'),
        url(r'^cms/header/logo/markup/$', TemplateView.as_view(template_name='header_logo.html'), name='header_logo_markup'),

        # To support remote authentication
        url(r'^remote/login/$', remote_cms_auth.verify_and_auth, name='verify_and_auth'),
    ]

# Let custom CMS apps override any URLs below
try:
    from .urls_custom import custom_urls
    urlpatterns += custom_urls
except ImportError:
    pass

if getattr(settings, 'INCLUDES_PORTAL_NAV', True):
    urlpatterns += [
        # To provide markup when Portal is missing
        url(r'^core/markup/nav/$', TemplateView.as_view(template_name='nav_portal.raw.html'), name='portal_nav_markup'),
    ]

urlpatterns += [
    # The Django CMS urls
    url(r'^', include('cms.urls')),
]

# Error pages
# TODO: Create error page that an authorized CMS user can edit
# https://groups.google.com/g/django-cms-developers/c/FJlj_Kv8xHs
# REF: Many solutions online return 404 page, but not 404 status code
# http://www.ilian.io/custom-404-not-found-page-with-django-cms/
# https://stackoverflow.com/a/44519606/11817077
# https://blog.maestropublishing.com/2019/11/custom-404-page-for-django-cms.html
from django.utils.functional import curry
from django.views.defaults import page_not_found
handler404 = curry(page_not_found, template_name='404.html')

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ]

    urlpatterns += staticfiles_urlpatterns()

    # RFE: Would preventing cache be a good addition?
    # SEE: https://stackoverflow.com/a/59340216/11817077
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
