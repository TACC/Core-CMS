from django.contrib import admin
from cms.extensions.admin import PageExtensionAdmin

from .models import PageMenuTarget


@admin.register(PageMenuTarget)
class PageMenuTargetAdmin(PageExtensionAdmin):
    pass
