import re

from django.urls import re_path
# from django.conf import settings

from .views import RemoteMarkup


app_name = 'remote_content'

# blogRemoteUrlPattern = r'^' + re.escape(settings.PORTAL_REMOTE_CONTENT_CLIENT_PATH)
urlpatterns = [
    # To render a blog (or any page) from another website
    # TODO: Use query parameter, not URL path
    # TODO: Use settings.PORTAL_REMOTE_CONTENT_CLIENT_PATH
    re_path(r'^markup/', RemoteMarkup.as_view(), name='remote_markup'),
]
