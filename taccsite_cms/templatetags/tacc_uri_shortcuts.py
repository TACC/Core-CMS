from django import template
from urllib.parse import urlparse
from django.utils.html import format_html

register = template.Library()

@register.simple_tag(takes_context=True)
def site_uri(context):
    """
    Custom Template Tag `site_uri`

    Use: Access Site URI values in Templates.

    Load custom tag into template:
        {% load tacc_uri_shortcuts %}

    Template inline usage:
        {% site_uri.absolute_uri %}
        {% site_uri.scheme %}
        {% site_uri.host %}

    Example:
        <a href="{% site_uri.absolute_uri %}">site URL (on dev)</a>
            # <a href="https://localhost:8000">site URL (on dev)</a>
        <a href="{% site_uri.absolute_uri %}">site URL (on prod)</a>
            # <a href="https://brand.tacc.utexas.edu/">site URL (on dev)</a>
    """
    request = context['request']
    absolute_uri = request.build_absolute_uri('/')
    return {
        # NOTE: Alternative is `{{ request.scheme }}://{{ request.get_host }}`
        'absolute_uri': absolute_uri,

        # WARNING: These assume context of template matches site host.
        #          To avoid this, consider the Site module.
        # SEE: https://stackoverflow.com/a/897053
        # SEE: https://docs.djangoproject.com/en/3.1/ref/contrib/sites/
        # NOTE: Alternative is `{{ request.scheme }}`
        'scheme': request.scheme,
        # NOTE: Alternative is `{{ request.get_host }}`
        'host': request.get_host(),
    }

@register.simple_tag(takes_context=True)
def target_blank(context, link_uri):
    """
    Custom Template Tag `target_blank`

    Use: Render `target="_blank"` if URI appears to be external.

    Load custom tag into template:
        {% load tacc_uri_shortcuts %}

    Template inline usage:
        {# (renders `target="_blank"`) #}
        {% target_blank absolute_uri_to_external_domain %}

        {# (renders nothing) #}
        {% target_blank relative_uri %}
        {% target_blank absolute_uri_to_same_domain %}

    Example:
        <a href="{{ absolute_uri_to_external_domain }}"
           {% target_blank absolute_uri_to_external_domain %}>other site</a>
            # <a href="https://otherwebsite.com" target="_blank">other site</a>
        <a href="{{ absolute_uri_to_same_domain }}"
           {% target_blank absolute_uri_to_same_domain %}>same site</a>
            # <a href="https://samewebsite.com/some-page">same site</a>
        <a href="{{ relative_uri }}"
           {% target_blank relative_uri %}>same site</a>
            # <a href="/some-page">same site</a>
    """
    request = context['request']
    req_uri = request.build_absolute_uri('/')

    req = urlparse(req_uri)
    link = urlparse(link_uri)

    req_origin = req.scheme + '://' + req.netloc
    link_origin = link.scheme + '://' + link.netloc

    # FAQ: I am literally double-checking, because I am unskilled in Django
    is_external = ( link_origin != req_origin and link_origin != '://' )
    is_internal = ( link.hostname == req.hostname or link.hostname == None )
    should_open_in_new_window = ( is_external and not is_internal )

    if should_open_in_new_window:
        # FAQ: Use `format_html` to not render `target="&quot;_blank&quot;"`
        return format_html('target="_blank"')
    else:
        return ''

@register.filter
def get_menu_uri(menu_item):
    """
    Custom Filter `get_menu_uri`

    Use: Render redirect URI or absolute URI for a `cms_menu` child

    Load custom tag into template:
        {% load tacc_uri_shortcuts %}

    Template inline usage:
        {{ menu_item|get_menu_uri }}

    Example:
        <a href="{{ child_which_has_internal_url|get_menu_uri }}">
            {{ child.get_menu_title }}</a>
            # <a href="https://samewebsite.com/some-page">some page here</a>
        <a href="{{ child_which_has_redirect_url|get_menu_uri }}">
            {{ child.get_menu_title }}</a>
            # <a href="https://otherwebsite.com/some-page">some page there</a>
    """
    if hasattr(menu_item.attr, 'redirect_url'):
        return menu_item.attr['redirect_url']
    else:
        return menu_item.get_absolute_url()
