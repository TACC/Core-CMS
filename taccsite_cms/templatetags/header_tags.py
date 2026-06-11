from django import template
from django.utils.safestring import mark_safe

from taccsite_cms.contrib.taccsite_header_logo.render import render as render_header

register = template.Library()


@register.simple_tag(takes_context=True)
def render_header_logo(context):
    html = render_header(context['request'], context)
    return mark_safe(html) if html else ''
