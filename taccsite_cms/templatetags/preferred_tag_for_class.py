from django import template

from django.conf import settings

register = template.Library()

def preferred_tag_for_class(tag, classname):
    """
    Custom Template Tag Filter `preferred_tag_for_class`

    Use: Get the preferred HTML tag to use for a given class

    Load custom tag into template:
        {% load preferred_tag_for_class %}

    Template inline usage:
        {% fallback_tag|preferred_tag_for_class:classname %}

    Example:
        {% with tag=instance.tag_type|preferred_tag_for_class:classname %}
            <{{ tag }}">{% instance.tag_type %}</{{ tag }}>
        {% endwith %}
    """
    new_tag = tag

    # If user chose div, they
    if (tag == settings.DJANGOCMS_STYLE_TAGS_DEFAULT):
        if      (classname == 'o-section o-section--style-light' or
                 classname == 'o-section o-section--style-dark'):
            new_tag = 'section'
        elif    (classname == 'c-callout' or
                 classname == 'c-recognition c-recognition--style-light' or
                 classname == 'c-recognition c-recognition--style-dark'):
            new_tag = 'aside'

    return new_tag

register.filter('preferred_tag_for_class', preferred_tag_for_class)
