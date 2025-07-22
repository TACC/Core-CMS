from django import template
import re

register = template.Library()

@register.filter
def strip_class_attribute(attributes_str):
    """
    Remove class attribute from an HTML attributes string.
    Usage: {{ instance.attributes_str|strip_class_attribute|safe }}
    """
    if not attributes_str:
        return ""

    # To remove `class="…"` or anything equivalent
    pattern = r' class\s*=\s*["\'][^"\']*["\']\s*'
    result = re.sub(pattern, ' ', attributes_str, flags=re.IGNORECASE)

    # To compress excess space
    new_attributes_str = re.sub(r'\s+', ' ', result).strip()

    return new_attributes_str
