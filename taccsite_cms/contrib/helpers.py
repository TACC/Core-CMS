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
# Get list of indicies of items that start with text
# SEE: https://stackoverflow.com/a/67393343/11817077
def get_indices_that_start_with(text, list):
    """
    Get a list of indices of list elements that starts with given text
    :rtype: list
    """
    return [i for i in range(len(list)) if list[i].startswith(text)]


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

        if len(err.messages):
            raise err

# Get name of field from a given model

# SEE: https://stackoverflow.com/a/14498938/11817077
def get_model_field_name(model, field_name):
    model_field_name = model._meta.get_field(field_name).verbose_name.title()

    return model_field_name
