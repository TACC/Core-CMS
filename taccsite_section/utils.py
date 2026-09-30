from taccsite_cms.contrib.helpers import concat_classnames


def section_type_to_class_string(section_type):
    """Map stored section type to a class string (Bootstrap Container plugin values)."""
    if not section_type or section_type == '_':
        return ''
    return section_type.strip()


def normalize_section_class_tokens(class_string):
    if not class_string:
        return ''
    parts = []
    for raw in class_string.replace(',', ' ').split():
        token = raw.strip()
        if token:
            parts.append(token)
    return concat_classnames(parts)


def attributes_str_without_class(instance):
    """Render attributes except class (class is composed on the wrapper element)."""
    attributes = dict(instance.attributes or {})
    attributes.pop('class', None)
    if not attributes:
        return ''
    return ' '.join(
        f'{key}="{value}"'
        for key, value in attributes.items()
    )
