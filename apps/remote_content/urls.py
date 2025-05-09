import re

from django.urls import re_path
from django.conf import settings

from .views import RemoteMarkup


app_name = 'remote_content'

urlpatterns = [
    re_path(
        r'^' + settings.PORTAL_REMOTE_CONTENT_CLIENT_PATH.strip('/') + '/(?P<page>.*)$',
        RemoteMarkup.as_view(),
        name='remote_markup'
    ),
]
