from django.http import JsonResponse
from django.views.generic import View

from django.conf import settings

class SettingsView(View):
    def get(self, request):
        theme = settings.THEME
        themeClassName =  't-' + theme if theme else None

        return JsonResponse({
            "themeClassName": themeClassName,
            "theme": settings.THEME
        })
