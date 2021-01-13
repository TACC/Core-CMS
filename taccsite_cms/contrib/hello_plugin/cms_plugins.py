from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

@plugin_pool.register_plugin
class HelloPlugin(CMSPluginBase):
    module = "TACC"
    model = CMSPlugin
    render_template = "hello_plugin.html"
    cache = False
