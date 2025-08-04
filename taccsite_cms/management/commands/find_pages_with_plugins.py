import os
import sys
import django

# Configure Django settings to avoid errors
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taccsite_cms.settings')
django.setup()

from django.apps import apps

def find_page_using_plugin_instance(plugin_instance_id):
    try:
        CMSPlugin = apps.get_model('cms', 'CMSPlugin')
        plugin_instance = CMSPlugin.objects.get(id=plugin_instance_id)
        page = plugin_instance.placeholder.page if plugin_instance.placeholder else None
        return page
    except CMSPlugin.DoesNotExist:
        return None

# Usage example:
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python find_plugin_page.py <plugin_instance_id>")
        sys.exit(1)

    plugin_instance_id = int(sys.argv[1])
    page = find_page_using_plugin_instance(plugin_instance_id)

    if page:
        print(f"The plugin instance with ID {plugin_instance_id} is used on page '{page.get_path()}'")
    else:
        print(f"No page uses the plugin instance with ID {plugin_instance_id}")
