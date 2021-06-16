# SEE: https://github.com/django-cms/djangocms-bootstrap4/blob/master/djangocms_bootstrap4/helpers.py
def concat_classes(classes):
    """
    Merge a list of classes and return concatinated string
    """
    return ' '.join(_class for _class in classes if _class)
