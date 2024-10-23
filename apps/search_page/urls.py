from django.urls import re_path
from .views import SearchPageView

app_name = 'search_page'
urlpatterns = [
    re_path('', SearchPageView, name='index'),
]
