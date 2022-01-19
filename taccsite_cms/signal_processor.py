from haystack.signals import BaseSignalProcessor
from django.db import models
from django.core.management import call_command
from cms import signals
from cms.models.pagemodel import Page


class RealtimeSignalProcessor(BaseSignalProcessor):
    """
    A signal processor to make a call to the Django Haystack
    `rebuild_index` management command when a CMS document is
    published, unpublished, or deleted. This will allow the
    ElasticSearch index to remain up-to-date with the latest
    published CMS content when a user searches the site.

    Usage:
        This signal processor hooks into Haystack via the
        `HAYSTACK_SIGNAL_PROCESSOR` Django setting.
    """

    def setup(self):
        signals.post_publish.connect(self.handle_save)
        signals.post_unpublish.connect(self.handle_save)
        models.signals.post_delete.connect(self.handle_save)

    def teardown(self):
        signals.post_publish.disconnect(self.handle_save)
        signals.post_unpublish.disconnect(self.handle_save)
        models.signals.post_delete.disconnect(self.handle_save)

    def handle_save(self, **kwargs):
        if type(kwargs.get('instance')) is Page:
            call_command('rebuild_index', '--noinput')
