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



# Filter Django `models.CharField` `choices`
# SEE: get_choices
def filter_choices_by_prefix(choices, prefix):
    """Reduce sequence of choices to items whose values begin with given string

    :param List[Tuple[str, str], ...] choices: the sequence to filter
    :param str prefix: the starting text required of an item value to retain it
    :returns: a sequence for django.db.models.CharField.choices
    :rtype: List[Tuple[str, str], ...]
    """
    new_choices = []

    for choice in choices:
        should_keep = choice[0].startswith(prefix)
        if should_keep:
            new_choices.append(choice)

    return new_choices



# Concatenate a list of CSS classes
# SEE: https://github.com/django-cms/djangocms-bootstrap4/blob/master/djangocms_bootstrap4/helpers.py
def concat_classnames(classes):
    """Concatenate a list of classname strings (without failing on None)"""
    # SEE: https://stackoverflow.com/a/20271297/11817077
    return ' '.join(_class for _class in classes if _class)



# Create a list clone that has another list shoved into it
# SEE: https://newbedev.com/how-to-insert-multiple-elements-into-a-list
def insert_at_position(position, list, list_to_insert):
    """Insert list at position within another list

    :returns: New list
    """
    return list[:position] + list_to_insert + list[position:]



# Get the date from a list that is nearest
# SEE: https://stackoverflow.com/a/32237949/11817077
def get_nearest(items, pivot):
    """Get nearest date (or other arithmatic value)

    :returns: The item value nearest the given "pivot" value
    """
    return min(items, key=lambda x: abs(x - pivot))



# Get list of indicies of items that start with text
# SEE: https://stackoverflow.com/a/67393343/11817077
def get_indices_that_start_with(text, list):
    """
    Get a list of indices of list elements that starts with given text

    :rtype: list
    """
    return [i for i in range(len(list)) if list[i].startswith(text)]



# Populate class attribute of plugin instances
def add_classname_to_instances(classname, plugin_instances):
    """Add class names to class attribute of plugin instances"""
    for instance in plugin_instances:
        # A plugin must not have any class set
        if not hasattr(instance.attributes, 'class'):
            instance.attributes['class'] = ''

        # The class should occur before any CMS or user classes
        # FAQ: This keeps plugin author classes together
        instance.attributes['class'] = instance.attributes['class'] + classname



# Get date nearest today

from datetime import date

# HELP: Can this logic be less verbose?
# HELP: Is the `preferred_time_period` parameter effectual?
def which_date_is_nearest_today(date_a, date_b, preferred_time_period):
    """
    Returns whether each date is today or nearest today, and whether nearest date is past or today or future.

    Only two dates are supported. You may prefer 'future' or 'past' date(s).

    If both dates are the same date, then both are reported as True.

    :param datetime date_a: a date "A" to compare
    :param datetime date_b: a date "B" to compare
    :param str preferred_time_period: whether to prefer 'future' or 'past' dates

    :returns:
        A tuple of tuples:
        ((
            ``boolean`` of whether ``date_a`` is nearest,
            ``string`` of ``date_a`` time period ``past``/``today``/``future``
        ),
        (
            ``boolean`` of whether ``date_b`` is nearest,
            ``string`` of ``date_b`` time period ``past``/``today``/``future``
        )),
    :rtype: tuple
    """
    today = date.today()
    is_a = False
    is_b = False
    a_time_period = 'today'
    b_time_period = 'today'

    # Match preferred time

    if today == date_a:
        is_a = True
        a_time_period = 'today'

    if today == date_b:
        is_b = True
        b_time_period = 'today'

    elif preferred_time_period == 'future':
        is_a = date_a and date_a >= today
        is_b = date_b and date_b >= today
        if is_a: a_time_period = 'future'
        if is_b: b_time_period = 'future'
        if not is_a and not is_b:
            is_a = date_a and date_a < today
            is_b = date_b and date_b < today
            if is_a: a_time_period = 'past'
            if is_b: b_time_period = 'past'

    elif preferred_time_period == 'past':
        is_a = date_a and date_a < today
        is_b = date_b and date_b < today
        if is_a: a_time_period = 'past'
        if is_b: b_time_period = 'past'
        if not is_a and not is_b:
            is_a = date_a and date_a >= today
            is_b = date_b and date_b >= today
            if is_a: a_time_period = 'future'
            if is_b: b_time_period = 'future'

    # Show nearest date
    if is_a and is_b and date_a != date_b:
        nearest_date = get_nearest((date_a, date_b), today)

        if date_a == nearest_date:
            is_b = False
        if date_b == nearest_date:
            is_a = False

    return ((is_a, a_time_period), (is_b, b_time_period))



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



# Tweak validation on Django CMS `AbstractLink` for TACC

from cms.models.pluginmodel import CMSPlugin

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# SEE: https://github.com/django-cms/djangocms-link/blob/3.0.0/djangocms_link/models.py#L48
def clean_for_abstract_link(model, self):
    """
    Intercept and manipulate validation on `AbstractLink` so that it suits TACC's minimal subclassing of it. (To catch only parent validation errors, not custom ones, run this before any custom validation.)

    Usage:
    ```
    from taccsite_cms.contrib.helpers import clean_for_abstract_link

    # Validate
    def clean(self):
        clean_for_abstract_link(__class__, self)

        ...
    ```
    """

    # Bypass irrelevant parent validation
    # SEE: ./_docs/how-to-override-validation-error-from-parent-model.md
    try:
        super(model, self).clean()
    except ValidationError as err:
        # Intercept multi-field errors
        if hasattr(err, 'error_dict'):
            for field, errors in err.message_dict.items():
                # Reduce verbosity of original error message
                # FAQ: Original error message assumes more fields exist
                indices = get_indices_that_start_with(
                    'Only one of ', errors
                )
                for i in indices:
                    err.error_dict[field] = ValidationError(
                        _('Only one of External link or Internal link may be given.'), code='invalid')

        if len(err.messages) == 0:
            pass
        else:
            raise err
