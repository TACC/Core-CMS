from django.contrib import admin
from . import models
from django import forms

# Create your models here.
class dropCapOptions(admin.ModelAdmin):
    list_display = (['your_button'])

    def your_button(self, obj):
        # Define the button here
        return '<button type="button" class="your-button-class">Your Button</button>'
    your_button.short_description = 'hello'  # Set this to an empty string to prevent the column header

admin.site.register([models.buttonToToggleDropCap], dropCapOptions)