from django.urls import re_path
from .views import CustomExampleView

app_name = 'custom_example'
urlpatterns = [
    re_path('', CustomExampleView, name='index'),
]
