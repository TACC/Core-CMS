from django.urls import path
from . import views

app_name = 'apps.search_page'

urlpatterns = [
    path('', views.SearchPageView, name='search')
]
