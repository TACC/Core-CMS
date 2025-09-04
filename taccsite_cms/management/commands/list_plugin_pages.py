from django.core.management import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = 'Finds the page that uses a specific plugin instance by its ID'

    def add_arguments(self, parser):
        parser.add_argument('plugin_instance_ids', nargs='+', type=str)

    def handle(self, *args, **options):
        for plugin_instance_id in options['plugin_instance_ids']:
            page = self.find_page_using_plugin_instance(plugin_instance_id)
            if page:
                self.stdout.write(f'Plugin instance ID {plugin_instance_id} is used on page: {page.get_path()}')
            else:
                self.stdout.write(f'No page found using plugin instance ID {plugin_instance_id}')

    def find_page_using_plugin_instance(self, plugin_instance_id):
        try:
            CMSPlugin = apps.get_model('cms', 'CMSPlugin')
            plugin_instance = CMSPlugin.objects.get(id=plugin_instance_id)
            page = plugin_instance.placeholder.page if plugin_instance.placeholder else None
            return page
        except CMSPlugin.DoesNotExist:
            return None
