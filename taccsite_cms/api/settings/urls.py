from django.conf.urls import url

from taccsite_cms.api.settings.views import SettingsView

app_name = 'settings'
urlpatterns = [
    url(r'^settings/$', SettingsView.as_view(), name='settings')
]
