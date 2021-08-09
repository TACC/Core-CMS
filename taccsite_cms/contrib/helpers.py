# Get Django `models.CharField` `choices`
def get_choices(choice_dict):
    """Get a sequence for a Django model field choices from a dictionary.
    :param Dict[str, Dict[str, str]] dictionary: choice as key for dictionary of classnames and descriptions
    :return: a sequence for django.db.models.CharField.choices
    :rtype: List[Tuple[str, str], ...]
    """
    choices = []

    for key, data in choice_dict.items():
        choice = (key, data['description'])
        choices.append(choice)

    return choices



# GH-93, GH-142, GH-133: Upcoming functions here (ease merge conflict, maybe)



# Concatenate a list of CSS classes
# SEE: https://github.com/django-cms/djangocms-bootstrap4/blob/master/djangocms_bootstrap4/helpers.py
def concat_classnames(classes):
    """Concatenate a list of classname strings (without failing on None)"""
    # SEE: https://stackoverflow.com/a/20271297/11817077
    return ' '.join(_class for _class in classes if _class)



# GH-93, GH-142, GH-133: Upcoming functions here (ease merge conflict, maybe)



# Allow plugins to set max number of nested children

from django.shortcuts import render

# SEE: https://github.com/django-cms/django-cms/issues/5102#issuecomment-597150141
class AbstractMaxChildrenPlugin():
    """
    Abstract extension of `CMSPluginBase` that allows setting maximum amount of nested/child plugins.
    Usage:
    1. Extend this class,
       after extending `CMSPluginBase` or a class that extends `CMSPluginBase`.
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
        return super(AbstractMaxChildrenPlugin, self).add_view(request, form_url, extra_context)



# GH-93, GH-142, GH-133: Upcoming functions here (ease merge conflict, maybe)
