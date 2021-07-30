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



# Concatenate a list of CSS classes
# SEE: https://github.com/django-cms/djangocms-bootstrap4/blob/master/djangocms_bootstrap4/helpers.py
def concat_classnames(classes):
    """Concatenate a list of classname strings (without failing on None)"""
    # SEE: https://stackoverflow.com/a/20271297/11817077
    return ' '.join(_class for _class in classes if _class)
