# SEE: https://github.com/django-cms/djangocms-bootstrap4/blob/master/djangocms_bootstrap4/helpers.py
def concat_classnames(classes):
    """
    Concatenates a list of classes (without failing on None)
    """
    # SEE: https://stackoverflow.com/a/20271297/11817077
    return ' '.join(_class for _class in classes if _class)

# SEE: https://newbedev.com/how-to-insert-multiple-elements-into-a-list
def insert_at_position(position, list, list_to_insert):
    return list[:position] + list_to_insert + list[position:]

from django.shortcuts import render
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

# SEE: https://github.com/django-cms/django-cms/issues/5102#issuecomment-597150141
class CMSPluginBaseWithMaxChildren(CMSPluginBase):
    """
    Extension of `CMSPluginBase` that allows setting maximum amount of nested/child plugins. Usage:

    1. Extend this class (instead of `CMSPluginBase`)
    2. Set `max_children` to desired limit.
    """

    max_children = None

    def add_view(self,request, form_url='', extra_context=None):

        if self.max_children:
            # FAQ: Placeholders do not have a parent, only plugins do
            if self._cms_initial_attributes['parent']:
                num_allowed = len([v for v in self._cms_initial_attributes['parent'].get_children() if v.get_plugin_instance()[0] is not None])
            else:
                num_allowed = len([v for v in self.placeholder.get_plugins() if v.get_plugin_instance()[0] is not None and v.get_plugin_name() == self.name])

            if num_allowed >= self.max_children:
                return render(request , "path/to/your/max_reached_template.html", {
                    'max_children': self.max_children,
                })
        return super(CMSPluginBaseWithMaxChildren, self).add_view(request, form_url, extra_context)
