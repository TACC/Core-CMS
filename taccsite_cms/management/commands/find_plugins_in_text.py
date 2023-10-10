import os
import logging
import importlib

from django.core.management import BaseCommand
from django.utils.module_loading import import_string

from djangocms_text_ckeditor.cms_plugins import TextPlugin

logger = logging.getLogger('django')

class Command(BaseCommand):
    help = f'Find plugins of a given class that are in Text plugin instance(s)'

    def add_arguments(self, parser):
        parser.add_argument('plugin_paths', nargs='+', type=str, help='The Python path(s) to plugin module class(es) e.g. "djangocms_picture.cms_plugins.PicturePlugin"')

    def handle(self, *args, **options):
        for plugin_path in options['plugin_paths']:
            try:
                plugin_class = import_string(plugin_path)
            except ImportError:
                logger.error(
                    f'Error importing plugin class from path: {plugin_path}'
                )
                continue
            plugin_instances_list = self.get_parent_text_plugins(plugin_class)
            count = len(plugin_instances_list)

            logger.info(
                f'{count} instances of {plugin_class.name} in a `TextPlugin`.'
            )

            for plugin_instance in plugin_instances_list:
                logger.info(
                    f'"{plugin_instance.name}" ({plugin_instance.id})'
                )

    # !!!: This function is not accurate!
    # TODO: (A) Rewrite so that it:
    #       1. finds all instances of TextPlugin
    #       2. finds whether plugin has instances of given plugin
    # TODO: (B) Rewrite so that it:
    #       1. finds all instances of given plugin
    #       2. finds whether plugin instances are children of a TextPlugin
    def get_parent_text_plugins(self, plugin_class):
        logger.info(f'Plugin class')

        if plugin_class and issubclass(plugin_class, TextPlugin):
            plugin_instances_set = plugin_class.objects.filter(text_plugin__isnull=False)

            return list(plugin_instances_set)
        else:
            return []
