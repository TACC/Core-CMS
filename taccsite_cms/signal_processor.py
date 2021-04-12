from haystack.signals import BaseSignalProcessor
from django.db import models
from django.core.management import call_command
from cms import signals


class RealtimeSignalProcessor(BaseSignalProcessor):

    def setup(self):
        signals.post_publish.connect(self.handle_save)
        signals.post_unpublish.connect(self.handle_save)
        models.signals.post_delete.connect(self.handle_save)

    def teardown(self):
        signals.post_publish.disconnect(self.handle_save)
        signals.post_unpublish.disconnect(self.handle_save)
        models.signals.post_delete.disconnect(self.handle_save)

    def handle_save(self, **kwargs):
        call_command('rebuild_index', '--noinput')
