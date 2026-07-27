from django.db import models

class DummyModel(models.Model):
    """
    Exists solely to trigger Django to send post_migrate signal (see apps.py)
    """
    class Meta:
        app_label = 'taccsite_cms'
