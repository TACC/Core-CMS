def get_offset_classname(offset):
    """Get offset content class based on standard offset value."""

    # TODO: Limit input to known offsets
    # SEE: taccsite_cms.contrib.constants:OFFSET_CHOICES
    switcher = {
        'right': 'c-offset-content--right',
        'left': 'c-offset-content--left'
    }

    return switcher.get(offset, '')

# SEE: https://github.com/django-cms/djangocms-bootstrap4/blob/master/djangocms_bootstrap4/helpers.py
def concat_classnames(classes):
    """
    Concatenates a list of classes (without failing on None)
    """
    # SEE: https://stackoverflow.com/a/20271297/11817077
    return ' '.join(_class for _class in classes if _class)
